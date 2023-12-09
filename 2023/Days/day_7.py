from collections import Counter

# key = len(set((hand)), len(duplicate_keys)) idk y but it made sense to me tho
HAND_TYPE = {
    (1, 1): 'Five of a Kind',
    (2, 1): 'Four of a Kind',
    (2, 2): 'Full House',
    (3, 1): 'Three of a Kind',
    (3, 2): 'Two Pair',
    (4, 1): 'One Pair',
    (5, 0): 'High card'
}

FACE_VALUE = {
    'A':14, 'K':13, 'Q':12, 'J':11, 'T':10
}


def open_file():
    with open('../Input/input_7.txt', 'r') as f:
        file_input = f.readlines()
    return file_input


def part_one(output, joker=False):
    ordered_hand = get_ordered_hand(output, joker)
    rank = 0
    for hand in ordered_hand:
        rank += len(ordered_hand[hand])
    total_winngs = 0
    for hand_type in ordered_hand:
        for hand in ordered_hand[hand_type]:
            bid = hand[1] * rank
            rank -= 1
            total_winngs += bid
    print(total_winngs)

# Return dict of repeated letters and their count when count > 1
def get_duplicates(hand) -> dict[str, int]:
    char_count = Counter(hand)
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates

# Returns each card's value in a list in the order they appear in the hand
def get_hand_value(hand) -> list[int]:
    global FACE_VALUE
    return [int(char) if char.isdigit() else FACE_VALUE.get(char, 0) for char in hand]
 
# Writing this return type has awakened something inside of me, but I also wont fix it
def insert_in_order(existing_list_tuple, new_list_tuple) -> list[(str, int, list[int])]:
    insert_position = len(existing_list_tuple)
    for index, current_tuple in enumerate(existing_list_tuple):
        for i in range(min(5, len(current_tuple[2]), len(new_list_tuple[2]))):
            if new_list_tuple[2][i] > current_tuple[2][i]:
                insert_position = index
                return existing_list_tuple[:insert_position] + [new_list_tuple] + existing_list_tuple[insert_position:]
            elif new_list_tuple[2][i] < current_tuple[2][i]:
                break
    return existing_list_tuple + [new_list_tuple]


# Identify the highest value card and replace 'J' with it.
def get_highest_card(hand, card_values) -> str:
    max_value = max(card_values)
    max_index = card_values.index(max_value)
    card_to_copy = hand[max_index]
    return card_to_copy
    

# Returns a new hand after 'J' has been converted to the best type.
def convert_joker(hand, duplicates, value) -> str:
    # Case where 'J' is the only repeated character.
    if 'J' in duplicates and duplicates['J'] == max(duplicates.values()) and len(set(duplicates)) == 1:
        card_to_copy = get_highest_card(hand, value)
        print(f'Hand: {hand}, Card to copy: {card_to_copy}')
    # Case where there are multiple repeated characters
    elif duplicates:
        duplicate_keys = [key for key in duplicates.keys()]
        hand_of_keys = ''.join(duplicate_keys)
        key_value = get_hand_value(hand_of_keys)
        max_value = max(key_value)
        max_index = value.index(max_value)
        card_to_copy = hand[max_index]
    # Case where there are no repeated characters
    else:
        card_to_copy = get_highest_card(hand, value)
    hand = hand.replace('J', card_to_copy)
    return hand

# I'm not proud, but it works.
def get_ordered_hand(hands, joker):
    global HAND_TYPE, FACE_VALUE
    if joker:
        FACE_VALUE['J'] = 1
    card_category = {value: [] for value in HAND_TYPE.values()}
    for hand, bid in hands:
        card_key = len(set(hand))
        card_duplicates = get_duplicates(hand)
        hand_value = get_hand_value(hand)
        if joker and 'J' in hand:
            hand = convert_joker(hand, card_duplicates, hand_value)
            card_key = len(set(hand))
            card_duplicates = get_duplicates(hand)
        card_type = HAND_TYPE[(card_key, len(card_duplicates))]
        hand_info = (hand, bid, hand_value)
        new_tuple = insert_in_order(card_category[card_type], hand_info)
        card_category[card_type] = new_tuple
    print(card_category)
    return card_category


def main():
    file_input = open_file()
    output = [(line.split()[0], int(line.split()[1])) for line in file_input]
    part_one(output)
    part_one(output, True)
        
main()