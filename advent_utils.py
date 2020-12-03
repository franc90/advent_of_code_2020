def read_lines(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))
