""" Homework 2: Higher-Order Functions"""

from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
double = lambda x: 2 * x
triple = lambda x: 3 * x
increment = lambda x: x + 1
is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
is_positive = lambda x: x > 0
greater_than_three = lambda x: x > 3


#####################
# Required Problems #
#####################


def make_power(f, n):
    """Return f^n, the n-th functional power of f,
    such that f^n(x) = f(f(...f(x)...)) where f appears n times.
    
    >>> square2 = make_power(square, 2)
    >>> square2(2)
    16
    >>> add_three = make_power(increment, 3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    temp=lambda x:x
    for i in range(0,n):
        temp=lambda x,prev=temp:f(prev(x))
    return temp


def product(n, f):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    f -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    ans=1
    for i in range(1,n+1):
        ans*=f(i)
    return ans


def accumulate(combiner, base, n, f):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are f(1), f(2), ..., f(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    for i in range(1,n+1):
        base=combiner(base,f(i))
    return base


def summation_using_accumulate(n, f):
    """Returns the sum of f(1) + ... + f(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add,0,n,f)


def product_using_accumulate(n, f):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul,1,n,f)


def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
    >>> # Failed attempts: 0
    >>> my_secret = my_secret("hax0r_1")
    INCORRECT PASSWORD
    >>> # Failed attempts: 1
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love NJU
    >>> # Failed attempts: 1
    >>> my_secret = my_secret("hax0r_2")
    INCORRECT PASSWORD
    >>> # Failed attempts: 2
    >>> my_secret = my_secret("hax0r_3")
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    def get_secret(password_attempt,fail=0):
        "*** YOUR CODE HERE ***"
        if fail>=num_attempts:
            print('SECRET LOCKED')
            return lambda attempt,f=fail:get_secret(attempt,fail=f)

        if password_attempt==password:
            print(secret)
            return lambda attempt,f=fail:get_secret(attempt,fail=f)

        print('INCORRECT PASSWORD')
        return lambda attempt,f=fail+1:get_secret(attempt,fail=f)
    
    return get_secret


def filter_digits(f, n):
    """Return a number formed by digits from `n` that satisfy the predicate `f`.
    
    >>> filter_digits(is_even, 123456)
    246
    >>> filter_digits(greater_than_three, 12345678)
    45678
    """
    "*** YOUR CODE HERE ***"
    ans=0
    l=0
    temp=n
    digits=0
    while(temp):
        l+=1
        temp//=10
    
    for i in range(l):
        cur=n%10
        if f(cur):
            ans+=cur*pow(10,digits)
            digits+=1
        n//=10

    return ans


church_true = lambda x: lambda y: x
church_false = lambda x: lambda y: y


def not_church(p):
    """Return the negation of the Church boolean p.

    >>> not_church(church_true)(1)(2)
    2
    >>> not_church(church_false)(1)(2)
    1

    >>> import ast, inspect
    >>> [type(s).__name__ for s in ast.parse(inspect.getsource(not_church)).body[0].body]
    ['Expr', 'Return']
    >>> from construct_check import check
    >>> # ban Python's own booleans and branching: you are implementing them
    >>> check('hw02.py', 'not_church',
    ...       ['If', 'IfExp', 'And', 'Or', 'Not', 'BoolOp', 'Compare'])
    True
    """
    return _______


def and_church(p, q):
    """Return the conjunction (logical and) of the Church booleans p and q.

    >>> and_church(church_true, church_true)(1)(2)
    1
    >>> and_church(church_true, church_false)(1)(2)
    2
    >>> and_church(church_false, church_true)(1)(2)
    2
    >>> and_church(church_false, church_false)(1)(2)
    2

    >>> import ast, inspect
    >>> [type(s).__name__ for s in ast.parse(inspect.getsource(and_church)).body[0].body]
    ['Expr', 'Return']
    >>> from construct_check import check
    >>> # ban Python's own booleans and branching: you are implementing them
    >>> check('hw02.py', 'and_church',
    ...       ['If', 'IfExp', 'And', 'Or', 'Not', 'BoolOp', 'Compare'])
    True
    """
    return _______


def or_church(p, q):
    """Return the disjunction (logical or) of the Church booleans p and q.

    >>> or_church(church_true, church_false)(1)(2)
    1
    >>> or_church(church_false, church_true)(1)(2)
    1
    >>> or_church(church_false, church_false)(1)(2)
    2

    >>> import ast, inspect
    >>> [type(s).__name__ for s in ast.parse(inspect.getsource(or_church)).body[0].body]
    ['Expr', 'Return']
    >>> from construct_check import check
    >>> # ban Python's own booleans and branching: you are implementing them
    >>> check('hw02.py', 'or_church',
    ...       ['If', 'IfExp', 'And', 'Or', 'Not', 'BoolOp', 'Compare'])
    True
    """
    return _______


def if_church(p, t, e):
    """Return t if the Church boolean p is true, and e otherwise.

    Both t and e are already evaluated when this function is called, exactly
    like if_function in the last homework.

    >>> if_church(church_true, 'yes', 'no')
    'yes'
    >>> if_church(church_false, 'yes', 'no')
    'no'

    >>> import ast, inspect
    >>> [type(s).__name__ for s in ast.parse(inspect.getsource(if_church)).body[0].body]
    ['Expr', 'Return']
    >>> from construct_check import check
    >>> # ban Python's own booleans and branching: you are implementing them
    >>> check('hw02.py', 'if_church',
    ...       ['If', 'IfExp', 'And', 'Or', 'Not', 'BoolOp', 'Compare'])
    True
    """
    return _______


def church_to_bool(p):
    """Convert the Church boolean p into a Python bool.

    Together with bool_to_church this is the bridge between the two
    representations, so these two functions may use Python's True and False.

    >>> church_to_bool(church_true)
    True
    >>> church_to_bool(church_false)
    False
    """
    return _______


def bool_to_church(b):
    """Convert the Python bool b into a Church boolean.

    >>> bool_to_church(True)(1)(2)
    1
    >>> bool_to_church(False)(1)(2)
    2
    """
    return _______


##########################
# Just for fun Questions #
##########################


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
