import re

with open('Input/input_4.txt', 'r') as f:
    file_input = f.readlines()

card_dict = {}

def get_match_count(line):
    formatted_line = re.findall(r'\d+|\|', line)
    split_index = formatted_line.index('|')
    game_numbers = formatted_line[:split_index]
    player_numbers = formatted_line[split_index + 1:]
    total_matches = 0
    for number in player_numbers:
        if number in game_numbers:
            total_matches+=1
    return total_matches

def update_dict(key, count):
    if key not in card_dict:
        card_dict[key] = 1
    total_copies = card_dict[key]
    while total_copies > 0:
        increase_range(key + 1, count)
        total_copies -= 1

def increase_range(key, count):
    for i in range(count):
        temp_key = key + i
        if temp_key not in card_dict:
            card_dict[temp_key] = 1
        card_dict[temp_key] += 1

def day_4():
    part_one_sum = 0
    part_two_sum = 0
    for line in file_input:
        card_points = 0
        game_card = line.split(':')
        key = int(re.findall(r'\d+', game_card[0])[0])
        total_matches = get_match_count(game_card[1])
        update_dict(key, total_matches)
        if total_matches > 0:
            card_points = 1 << total_matches - 1
        part_one_sum += card_points

    for key in card_dict:
        part_two_sum += card_dict[key]
    print(part_one_sum)
    print(part_two_sum)
    