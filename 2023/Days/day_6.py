import re

def open_file():
    with open('../Input/input_6.txt', 'r') as f:
        file_input = f.read()
    return file_input


def count_ways_to_win(time, distance):
    sum_of_wins = 0
    possible_wins, remainder = divmod(time, 2)
    for i in range(possible_wins + remainder):
        if i * (time - i) > distance:
            sum_of_wins += 2
    if not remainder:
        sum_of_wins += 1
    return sum_of_wins

def main():
    file_input = open_file()
    
    clean_input = [[int(item) for item in re.findall(r'\d+', line)] for line in file_input.split('\n') if re.findall(r'\d+', line)]
    part_one_numbers = [tuple(pair) for pair in zip(*clean_input)]
    part_two_numbers = [int(''.join(re.findall(r'\d+', line))) for line in file_input.split('\n') if line.strip()]
        
    part_one_wins = 1
    for time, distance in part_one_numbers:  
        part_one_wins *= count_ways_to_win(time, distance)

    time, distance = part_two_numbers[0], part_two_numbers[1]
    part_two_wins = count_ways_to_win(time, distance)

    print(f'{part_one_wins}\n{part_two_wins}')

main()