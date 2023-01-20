from typing import Iterable
# See if you were to modify this to count animal OR fruit
# which one you would have more confident in not screwing up?

############ BAD ################
def count_animal(filename: str, output: str) -> int:
    count = 0
    with open(filename) as f:  # open file
        for line in f:  # for each line
            if line.lower().strip() in ['ant', 'bat', 'cat', 'dog']:  # clean and check if it's animal
                count += 1

    with open(output, 'w') as f: # write output to a file
        f.write(str(count))


############ Better ##########################


def clean_line(s: str) -> str:
    return s.lower().strip()


def is_animal(s: str) -> bool:
    return s in ['ant', 'bat', 'cat', 'dog']


def better_count_animal_from_list(lines: Iterable[str]) -> int:
    count = 0
    for line in lines:
        should_be_counted = is_animal(clean_line(line))
        if should_be_counted:
            count += 1
    return count

def write_output(output: str, count: int):
    with open(output, 'w') as f:
        f.write(str(count))


def better_count_animal_from_file(filename: str, output: str):
    with open(filename) as f:
        count = better_count_animal_from_list(f)

    write_output(output=output, count=count)
