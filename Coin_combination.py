"""You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1."""



def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # use as many 5-rupee coins as possible
    five_needed = min(no_of_five, rupees_to_make // 5)
    remainder = rupees_to_make - five_needed * 5

    # if remaining amount can be paid with available 1-rupee coins
    if remainder <= no_of_one:
        one_needed = remainder
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

# Test the sample cases from the problem statement
print(make_amount(21, 4, 2) )  # expected: No. of Five needed : 4  ; No. of One needed : 1
print(make_amount(11, 2, 11) ) # expected: No. of Five needed : 2  ; No. of One needed : 1
print(make_amount(19, 3, 3) )  # expected: -1
