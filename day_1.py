import re

with open("Input/input_1.txt", "r") as f:
    file_input = f.readlines()

string_value = {
    "zero": "0", "one": "1", "two": "2", "three":"3", "four":"4", 
    "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"
}

answer_one = 0
answer_two = 0

only_numbers = [re.findall(r'[0-9]+', line) for line in file_input]

for line in only_numbers:
    value = int(line[0][0] + line[-1][-1])
    answer_one += value


def get_first_index_value(line, value_dict):
    first_num = re.search(r'\d', line)
    first_int = first_num.start() if first_num else None
    first_key_index = 1 + len(line)
    first_key = ''
    for key in value_dict:
        try:
            index = line.index(key)
            if index < first_key_index:
                first_key_index = index
                first_key = key
        except ValueError:
            pass    
    return line[first_int] if (first_int is not None and first_int < first_key_index) else value_dict[first_key]

for line in file_input:
    first_int = get_first_index_value(line, string_value)
    reversed_string_dict = {key[::-1]: value for key, value in string_value.items()}
    reversed_line = line[::-1]
    last_int = get_first_index_value(reversed_line, reversed_string_dict)
    answer_two += int(first_int + last_int)

print(answer_one)
print(answer_two)
