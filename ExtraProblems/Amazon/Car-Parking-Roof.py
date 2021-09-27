# https://leetcode.com/discuss/interview-question/1317796/amazon-oa-2021-hackerrank
"""
 You are given an List of positions of cars as to where they are parked. You are also given an integer K. 
 The cars needs to be covered with a roof. You have to find the minimum length of roof that takes to cover K cars.
 
 Input : 12,6,5,2      K = 3
 
 Explanation :  There are two possible roofs that can cover K cars. One that covers the car in 2,5,6 parking spots and
 another roof which covers 5,6,12 parking spots. The length of these two roofs are 5 and 8 respectively. Return 5
 since that's the roof with minimum length that covers K cars.

 Output : 5

"""

def carParkingRoof(cars, k):
    # Write your code here
    # sliding window algorithm. window size = k
    cars = sorted(cars)
    window = cars[0 + k - 1] - cars[0] + 1
    result = window
    for i in range(1, len(cars) - k):
        j = i + k - 1
        window = cars[j] - cars[i] + 1
        result = min(result, window)
    
    return result
cars, k = [1, 2, 3, 10], 4
print(carParkingRoof(cars, k)) # 9
#
#
cars, k = [2, 10, 8, 17], 3
print(carParkingRoof(cars, k)) # 9
#
cars, k = [1, 2, 3, 10, 4], 4
print(carParkingRoof(cars, k)) # 10
cars, k = [7, 100, 50], 2
print(carParkingRoof(cars, k)) # 44
#My Testcase 
cars,k = [6,2,12,7],3
print("MINE: ",carParkingRoof(cars, k)) # 6