# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
from typing import Iterator


def build_histogram(lines: Iterator[str]) -> dict[str, int]:
    counter = {}
    for line in lines:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 0
    return counter


def find_max_key(counter: dict[str, int]) -> str:
    max_key = None
    max_counter = 0
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
    return max_key


def find_min_key(counter: dict[str, int]) -> str:
    min_key = None
    min_counter = 0
    for k, v in counter.items():
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v
    return min_key


def compute_message(min_key: str, min_count: int, max_key: str, max_count: int):
    return f'Min Key = {min_key} with count = {min_count}' + f'Max Key = {max_key} with count = {max_count}'


def find_min_max_key(fname: str) -> None:
    # fill up histogram
    with open(fname, 'r') as f:
        counter = build_histogram(f)

    # find max key
    max_key = find_max_key(counter)
    min_key = find_min_key(counter)
    print(compute_message(min_key, counter[min_key], max_key, counter[max_key]))


def main():
    parser = argparse.ArgumentParser(
        description='compute the entry with the most occurrence and the least occurrence form a file')
    parser.add_argument('fname', metavar='N', type=str,
                        help='filename to compute the histogram')
    args = parser.parse_args()
    find_max_key(args.fname)


if __name__ == '__main__':
    main()
