"""FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.
Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
Distance in kms
Delivery charge in Rs per km

For first 3kms 0

For next 3kms 3

For the remaining 6

Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer. 

The below information must be used to check the validity of the data provided by the customer: 

Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.

Distance in kms must be greater than 0.

Quantity ordered should be minimum 1.

If any of the input is invalid, the bill amount should be considered as -1."""

#lex_auth_012693782475940832141
def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0

    # validate inputs
    if (food_type not in ('V', 'N')) or (quantity_ordered < 1) or (distance_in_kms <= 0):
        return -1

    # determine cost per plate
    if food_type == 'V':
        cost_per_plate = 120
    else:
        cost_per_plate = 150

    # food cost
    food_cost = cost_per_plate * quantity_ordered

    # delivery charge calculation
    delivery_charge = 0
    remaining_distance = distance_in_kms

    # first 3 kms: no charge
    if remaining_distance > 3:
        remaining_distance -= 3
    else:
        remaining_distance = 0

    # next 3 kms: Rs 3 per km
    if remaining_distance > 0:
        next_segment = min(remaining_distance, 3)
        delivery_charge += next_segment * 3
        remaining_distance -= next_segment

    # remaining kms: Rs 6 per km
    if remaining_distance > 0:
        delivery_charge += remaining_distance * 6

    # total bill
    bill_amount = food_cost + delivery_charge
    return bill_amount

# example
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)
