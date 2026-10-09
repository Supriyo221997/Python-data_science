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