import re

with open("../Input/input_2.txt", "r") as f:
    file_input = f.readlines()
    
def split_line(file_input):
    my_dict = {
        int(re.search(r'Game (\d+)', line).group(1)): {
            'r': [int(num) for num in re.findall(r'(\d+)\s+red', line)],
            'g': [int(num) for num in re.findall(r'(\d+)\s+green', line)],
            'b': [int(num) for num in re.findall(r'(\d+)\s+blue', line)]
        }
        for line in file_input
    }
    return my_dict

def get_sum(my_dict):
    my_sum = 0
    for game_id, colors in my_dict.items():
        if any(value > 12 for value in colors['r']):
            continue 
        if any(value > 13 for value in colors['g']):
            continue 
        if any(value > 14 for value in colors['b']):
            continue 
        my_sum += game_id
    print(my_sum)

def get_power_sum(my_dict):
    my_power_sum = 0
    for game_id, colors in my_dict.items():
        max_red = max(colors['r']) if colors['r'] else 0
        max_green = max(colors['g']) if colors['g'] else 0
        max_blue = max(colors['b']) if colors['b'] else 0 
        my_power_sum += max_red * max_green * max_blue
    print(my_power_sum)
            
split_values = split_line(file_input)
get_sum(split_values)
get_power_sum(split_values)
