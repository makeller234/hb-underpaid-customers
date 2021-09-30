# create a function that takes in the name of the file and the current price of melons
def incorrect_pay(file_name, melon_cost):
    """Parameters are the file name and the current price of melons
    This function determines if the seller received the correct pay
    
    Looks at each line, breaks it up by the | symbol, figures out if the seller
    got paid the right amount.
    """
    # open the file and assign it the variable
    the_file = open(file_name)

    #create an empty list that will hold all the incorrect payment information
    incorrect_payments = []

    # loop through the file, removing extra whitespace characters at the end and separating the line based on the | symbol
    for line in the_file:
        line = line.rstrip()

        word = line.split('|')

        # separate out each word by the index to get the information we need
        # note for future Melissa can do it this way: order_num, full_name, emlon_qty, amt_paid = word
        seller_name = word[1]
        melons_sold = float(word[2])
        payment_rec = float(word[3])

        # calculate the correct payment they should have received based on sales and current melon price
        correct_pay = melon_cost * melons_sold

        # if the corret pay is NOT what they received, add them to the incorrect payments list
        if payment_rec != correct_pay:
            incorrect_payments.append(f'{seller_name} was paid ${payment_rec:.2f}, expected ${correct_pay:.2f}.')

    #close the file because we are done with it
    the_file.close()

    #return the contents of the incorrect payments list, one line at a time
    return ("\n".join(incorrect_payments))

# test the function to see if it works

melon_cost = 1
print(incorrect_pay('customer-orders.txt', melon_cost))


## Original Code
# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00


# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
