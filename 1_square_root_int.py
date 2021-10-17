"""
Problem 1: Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example, if the given number is 16, then the answer would be 4.

If the given number if 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`
"""
def floor(number):

    return number - number%1
"""
i < j
"""
def sqrt_recursive(number, i, j):
    i = floor(i)
    j = floor(j)

    if j*j == number:
        return j

    if i*i == number:
        return i

    if number > j*j:
        return j

    if number > i*i and number < j*j:
        mid = floor((j+i)/2)
        if mid*mid == number:
            return mid
        
        if mid*mid > number and mid*mid < number:
            output = sqrt_recursive(number, mid, j-1)
        
        else:
            output = sqrt_recursive(number, i+1, mid)
    elif number < i*i:
        output = sqrt_recursive(number, i/2, i-1)
    return output

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    if number == 0:
        return 0

    if number <= 3:
        return 1

    return sqrt_recursive(number, number/4, number/2)


### TEST CASES ###

# prints "Pass"
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (6 == sqrt(37)) else "Fail")
print ("Pass" if  (5 == sqrt(35)) else "Fail")
