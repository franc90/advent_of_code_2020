use std::fs::File;
use std::io::{BufReader, BufRead};
use std::option::Option::Some;
// use std::iter::Skip;

fn main() -> std::io::Result<()> {
    let file = File::open("input")?;
    let readr = BufReader::new(file);
    let mut v: Vec<i32> = readr.lines()
        .map(|l| l.unwrap())
        .filter(|x| !x.is_empty())
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    println!("{:?}", compute(&mut v));

    Ok(())
}

fn compute(v: &mut Vec<i32>) -> Option<i32>{
    for x in 0..v.len() - 1 {
        let first = v.get(x).unwrap();
        let mut skipped = 1;
        let mut vector1 = v.iter().skip(x + skipped);
        while let Some(second) = vector1.next() {
            let mut vector2 = v.iter().skip(x + skipped + 1);
            skipped += 1;
            while let Some(third) = vector2.next() {
                if first + second + third == 2020 {
                    return Some(first * second * third)
                }
            }
        }
    }
    return None
}