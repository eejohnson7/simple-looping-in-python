'''
You are given an integer n where n ranges from 1 to 10^8, inclusive. Your task is to write a function that calculates and 
returns the product of the odd digits of n, without converting n into a string.

For example, if n equals 43172, the output should be 21, because the product of the odd digits 3, 1, and 7 is 21.

Please note that if n has no odd digits, your function should return 0.

You are expected to solve this task by using a while loop. Good luck!
'''

def solution(n):
    # TODO: implement
    odds = []
    
    while n > 0:
        digit = n % 10
        
        if digit % 2 != 0:
            odds.append(digit)
            
        n = n // 10
        
    if odds == []:
        return 0
        
    product = 1
    for odd in odds:
        product = product * odd
    
    return product