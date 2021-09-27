"""
Given an integer denoting a total number of wheels, help Amazon Logistics find the number 
of different ways to choose a fleet fo  vehicles from an infinite supply of two-wheeled and four-whelled 
vehicles such that the group of chosen vehicles has that exact total number of wheels. Two ways of choosing vehicles
are considered to be different if and only if they contain different numbers of two-wheeled or four-wheeled bechicle

For example, if our array wheels = [4,5,6] our return arry would be res = [2, 0, 2]. Case by case, we
can have 1 four-wheel or 2 two-wheel to have 4 wheels. We cannot have 5 wheels. We can have 1
four-wheel and 1 two-wheel or 3 two-wheel vehicles in the final case
"""

"""
If the number is not a multiple of 2 then number of ways is 0. if it is, then the problems is to find the number of multiples of 4 in the range ( for building 4 wheelers ) + 1 for choosing all the vehicles to be 2 wheelers. Because number of ways depends like moving a pointer from the range choosing one part to be 2 wheelers and the other part to be 4 wheelers.
"""
def chooseFleets(fleets):
    sol = []
    for num in fleets:
        if num % 2 != 0:
            sol.append(0)
    else:
        sol.append((num / 4) + 1)
    return sol

# Time O(n) Space O(1)