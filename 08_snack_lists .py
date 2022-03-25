# Initialise snack lists

names = ['ryan', 'troy', 'toby', 'shawn', 'harish']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1,'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]    
]

count = 0
for cliet_order in test_data:

    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    # print snack lists

    #get order(hard coded for easy testing)
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = snack_menu_dict[to_find]
            add_list[-1] = amount

print(snack_lists)