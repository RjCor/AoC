import itertools
import re

with open("Input/input_3.txt", "r") as f:
    file_input = f.readlines()

def get_adjacent_lines(iterable):
    previous_line, current_line, next_line = itertools.tee(iterable, 3)
    previous_line = itertools.chain([None], previous_line)
    next_line = itertools.chain(itertools.islice(next_line, 1, None), [None])
    return zip(previous_line, current_line, next_line)

def check_adjacent_line(line, start, end):
    slice_to_check = re.sub(r'[\d.\n]', '', line[start:end])
    if len(slice_to_check) > 0:
        return True
    return False

def part_one():
    my_sum = 0
    for previous_line, current_line, next_line in get_adjacent_lines(file_input):
        # For each number in a line
        for match in re.finditer(r'\d+', current_line):
            number_str = match.group()
            start = max(match.start() - 1, 0)
            end = match.start() + len(number_str) + 1
            # Determine if its range overlaps a symbol in the previous, current, or next line.
            if previous_line:
                if check_adjacent_line(previous_line, start, end):
                    my_sum += int(number_str)
                    continue
            if next_line:
                if check_adjacent_line(next_line, start, end):
                    my_sum += int(number_str)
                    continue
            if check_adjacent_line(current_line, start, end):
                my_sum += int(number_str)        
    print(my_sum)


def check_index_range(line, start, end):
    all_matches = []
    # For each number in a line
    for match in re.finditer(r'\d+', line):
        length_of_match = len(match.group())
        # Determine if its starting index + length overlaps the symbol's range.
        if set(range(match.start(), match.start() + length_of_match)).intersection(range(start, end + 1)):
            all_matches.append(int(match.group()))
    return all_matches

def part_two():
    my_sum = 0
    for previous_line, current_line, next_line in get_adjacent_lines(file_input):
        for match in re.finditer(r'[^0-9\n\.]+', current_line):
            all_adjacent_numbers = []
            symbol_str = match.group()
            # Do not accidentally start at the end of the list... again
            start = max(match.start() - 1, 0)
            end = match.start() + len(symbol_str)
            if previous_line:
                all_adjacent_numbers.extend(check_index_range(previous_line, start, end))
            if next_line:
                all_adjacent_numbers.extend(check_index_range(next_line, start, end))
            all_adjacent_numbers.extend(check_index_range(current_line, start, end))
            # If more than one number is adjacent to a symbol, multiply them.
            if len(all_adjacent_numbers) > 1:
                result = all_adjacent_numbers[0] * all_adjacent_numbers[1]
                my_sum += result
    print(my_sum)
    
part_one()
part_two()