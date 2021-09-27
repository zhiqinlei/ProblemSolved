"""
An Amazon seller is celebrating ten years in business! THey are having a sale to honor their priviledged member,
those who have pruschased from them in the past five years. These members receive the best discount indicated by andy discount
tags attached to the product.
Determine the minimum cost to purchase all porducts listed. As each potential price is calculated, round it to the nearest integer
before adding it to the total. Return  the cost to purchase all items as an integer

There are three types of dicount tags:

Type 0: discounted price, the item is sold for a given price.
Type 1: percentage discount, the customer is given a fixed percentage discount form the retail price.
Type 2: fixed discount the customer is given a fixed amount off from the retail price.

Example
Products = [['10', 'd0', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY']]
Discounts = [['d0', '1', '27'], ['d1', '2', '5']]
"""

def FindLowestPrice(products, discounts):
    dict_discounts = {}
    for i in range(len(discounts)): # create dict
        this_discount = discounts[i]
        dict_discounts[this_discount[0]] = [int(this_discount[1]), int(this_discount[2])]
    print(dict_discounts)
    total_price = 0
    for i in range(len(products)): # iterate over products
        product = products[i] # get current product
        retail = int(product[0]) # get retail price
        price_list_this_product = [] # the list of all possible disc
        for j in range(len(product)-1): # start from index 1
            if product[j+1] == 'EMPTY':
                price_list_this_product.append(retail) # if empty, add
            else:
                discount_type = dict_discounts[product[j+1]][0] # get t
                discount_number = dict_discounts[product[j+1]][1] # g
                if discount_type == 0:
                    price_list_this_product.append(type0(discount_number))
                elif discount_type == 1:
                    price_list_this_product.append(type1(retail, discount_number))
                else:
                    price_list_this_product.append(type2(retail, discount_number))
        total_price = total_price + min(price_list_this_product) # g
    return total_price
def type0(discount):
    return int(discount)
def type1(price, percentage):
    return int(price - price*percentage/100)
def type2(price, discount):
    return int(price - discount)

def findLowestPrice(products, discounts):
    # Write your code here
    maps = {}
    subtotal = 0
    for i in discounts:
        maps[i[0]] = str(i[1]) + " " + str(i[2])
    for j in products:
        price = int(j[0])
        lowest = price
        for d in j[1:]:
            if d != 'EMPTY':
                splitted = maps[d].split()
                t, am = splitted[0], int(splitted[1])
                print(t,am)
                if t == '0':
                    if am < lowest:
                        lowest = am
                elif t == '1':
                    if (price-(price*am/100)) < lowest:
                        lowest = (price-(price*am/100))
                else:
                    if (price-am) < lowest:
                        lowest = (price-am)
        subtotal += lowest
    return int(subtotal)
