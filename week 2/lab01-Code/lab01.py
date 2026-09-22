# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def factorial(n):
    """Return the factorial of a non-negative integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    ans=1
    for i in range(2,n+1):
        ans=ans*i
    return ans


def is_right_triangle(a, b, c):
    """Given three integers (maybe non-positive), judge whether the three
    integers can form the three sides of a right triangle.

    >>> is_right_triangle(2, 1, 3)
    False
    >>> is_right_triangle(5, -3, 4)
    False
    >>> is_right_triangle(5, 3, 4)
    True
    """
    "*** YOUR CODE HERE ***"
    if a<=0 or b<=0 or c<=0:
        return False
    if a*a+b*b==c*c:
        return True
    if a*a+c*c==b*b:
        return True
    if b*b+c*c==a*a:
        return True
    return False


def number_of_k(n, k):
    """Return the number of occurrences of k in each digit of a non-negative
    integer n.

    >>> number_of_k(999, 9)
    3
    >>> number_of_k(1234321, 2)
    2
    """
    "*** YOUR CODE HERE ***"
    ans=0
    while n//10:
        cur=n%10
        if cur==k:
            ans+=1
        n//=10
    if n==k:
        ans+=1
    return ans


def count_squares(a, b):
    """Count squares cut from an a-by-b rectangle, taking the largest each time.

    a and b are positive integers.

    >>> count_squares(13, 5)
    6
    >>> count_squares(1, 5)
    5
    """
    "*** YOUR CODE HERE ***"
    ans=0
    if a<b:
        c=a
        a=b
        b=c
    while b:
        sum=a//b
        ans+=sum
        a-=sum*b
        if a<b:
            c=a
            a=b
            b=c
    return ans