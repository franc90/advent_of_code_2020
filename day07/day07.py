import networkx as nx

from advent_utils import read_lines


def parse_to_graph(lines):
    def remove_meaningless_words(line):
        return line.replace("bags contain ", "").replace("bags", "bag").replace("bag.", "").replace("bag, ", "")

    def create_node_name(part1, part2):
        return f"{part1} {part2}"

    g = nx.DiGraph()
    lines = filter(lambda l: "bags contain no other bags." not in l, lines)
    lines = map(lambda l: remove_meaningless_words(l), lines)
    words_in_lines = map(lambda l: l.split(), lines)

    for words in words_in_lines:
        from_node = create_node_name(words[0], words[1])
        words = words[2:]

        while len(words) > 0:
            to_node = create_node_name(words[1], words[2])
            g.add_edge(from_node, to_node, weight=int(words[0]))
            words = words[3:]
    return g


def possible_holders_of_my_bag(g, my_bag="shiny gold"):
    predecessors = set()
    for parent in g.predecessors(my_bag):
        predecessors.add(parent)
        predecessors = predecessors.union(possible_holders_of_my_bag(g, parent))
    return predecessors


def count_bags_inside(g, my_bag="shiny gold"):
    def count_required_bags_inside(g, my_bag):
        count = 1
        for child in g.successors(my_bag):
            count += g[my_bag][child]["weight"] * count_required_bags_inside(g, child)
        return count

    return count_required_bags_inside(g, my_bag) - 1


test_lines = read_lines('test')
test_graph = parse_to_graph(test_lines)

parent_colors_cnt_test = possible_holders_of_my_bag(test_graph)
bags_in_test_bag = count_bags_inside(test_graph)
assert 4 == len(parent_colors_cnt_test), f"4 != {len(parent_colors_cnt_test)}"
assert 32 == bags_in_test_bag, f"32 != {bags_in_test_bag}"

lines = read_lines('input')
graph = parse_to_graph(lines)
parent_colors_cnt = len(possible_holders_of_my_bag(graph))
bags_in_my_bag = count_bags_inside(graph)
print(f"Possible parent colors: {parent_colors_cnt}")
print(f"Required bags: {count_bags_inside(graph)}")
