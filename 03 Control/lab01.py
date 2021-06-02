# Q4: Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    i = 1
    result = n
    if k == 0:
        result = 1
    else:
        while i < k:
            result = result * (n-1)
            n -= 1
            i += 1
    return result

  
# Q5: Sum Digits
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    n = 1
    sum = y % pow(10,n)
    while y // (pow(10,n)) != 0:
        sum = sum +( y // (pow(10,n)) ) % 10
        n += 1
    return sum


# Q7: Double Eights
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***" 
    i = 0
    while n // (pow(10,i)) != 0:
        dig1 =( n // (pow(10,i)) ) % 10
        dig2 =( n // (pow(10,i+1)) ) % 10
        if dig1 == dig2 ==8:
            return True
        else:
            i += 1
    return False



$ python3 ok -q falling
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Backup... 100% complete
Backup past deadline by 340 days, 8 hours, 15 minutes, and 29 seconds
Backup successful for user: ____


$ python3 ok -q sum_digits
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Backup... 100% complete
Backup past deadline by 340 days, 8 hours, 16 minutes, and 54 seconds
Backup successful for user: ____
    

$ python3 ok -q double_eights
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Backup... 33.33% complete




