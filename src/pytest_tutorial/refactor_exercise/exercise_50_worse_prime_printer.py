import math
from typing import List, Optional

numbers = [2]

col_per_page = 5
row_per_page = 10
column_width = 10

numbers_per_page = col_per_page * row_per_page

n_primes =136
number_to_check = 3

pages: List[List[List[Optional[int]]]] = []
current_page = None

#build prime list
while True:
    if len(numbers) >= n_primes:
        break
    is_prime = True
    for n in numbers:
        if n > math.sqrt(number_to_check):
            is_prime = True
            break
        elif number_to_check % n == 0:
            is_prime = False
            break
    if is_prime:
        numbers.append(number_to_check)
    number_to_check += 2

#put in array
for inum, number in enumerate(numbers):
    if inum % numbers_per_page == 0:
        new_page = [[None] * col_per_page for _ in range(row_per_page)]
        pages.append(new_page)
        current_page = new_page
    row_no = (inum % numbers_per_page) % row_per_page
    col_no = (inum % numbers_per_page) // row_per_page
    current_page[row_no][col_no] = number

# print pages
for ipage, page in enumerate(pages):
    print(f'===Page {ipage + 1}===')
    for row in page:
        for number in row:
            if number is not None:
                print(f'{number: 6}', end='')
        print('\n')
