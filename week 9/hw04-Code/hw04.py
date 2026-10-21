"""Homework 4: Data Abstraction and Trees"""

from copy import deepcopy
from ADT import tree, label, branches, is_leaf, print_tree, copy_tree

#####################
# Required Problems #
#####################


# Problem 1.1
def fn_empty():
    """Return an empty function.

    >>> fn_empty()
    []
    """
    return []

def fn_remap(fn, x, y):
    """Return a new function that is the same as fn except that it maps x to y.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> f
    [[1, 2]]
    >>> fn_remap(f, 1, 3)
    [[1, 3]]
    >>> fn_remap(f, 2, 3)
    [[1, 2], [2, 3]]
    """
    result=[]
    for i in fn:
        if i[0]!=x:
            result=result+[deepcopy(i)]
    result=result+[[x,deepcopy(y)]]
    return result

def fn_domain(fn):
    """Return a sorted list of all the inputs (domain) of fn.
    Note that if fn maps x to None, then x is not in the domain of fn.

    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3))
    [1, 2]
    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 2, 3), 1, 2))
    [1, 2]
    >>> fn_domain(fn_empty())
    []
    >>> fn_domain(fn_remap(fn_empty(), 1, None))
    []
    """
    ans=[]
    for i in fn:
        if i[1] is not None and i[0] not in ans:
            ans+=[i[0]]
    return sorted(ans)

def fn_call(fn, x):
    """Return the result of applying fn to x.
    If fn does not map x to a value, return None.

    >>> fn_call(fn_remap(fn_empty(), 1, 2), 1)
    2
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 2)
    3
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 1)
    2
    >>> fn_call(fn_empty(), 1) is None
    True
    """
    for i in fn:
        if i[0]==x:
            #if i[1] is not None:
            return i[1]
    return None

# Problem 1.2
def fn_ext(fn1, fn2):
    """Return whether fn1 and fn2 represent the same function.
    Two functions are the same if and only if they have the same domain
    and output the same value for each input in the domain.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> g = fn_remap(fn_empty(), 2, 3)
    >>> fn_ext(f, g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), fn_remap(g, 1, 2))
    True
    """
    if fn_domain(fn1)!=fn_domain(fn2):
        return False
    for i in fn_domain(fn1):
        if fn_call(fn1,i)!=fn_call(fn2,i):
            return False
    return True


def fn_compose(fn1, fn2):
    """Return a new function that is the composition of fn1 and fn2.
    The composition of two functions fn1 and fn2 is a function fn such that
    fn(x) = fn1(fn2(x)) for every x in the domain of fn2.

    >>> f = fn_remap(fn_empty(), 2, 3)
    >>> g = fn_remap(fn_empty(), 1, 2)
    >>> h = fn_compose(f, g)
    >>> fn_call(h, 1)
    3
    >>> fn_call(h, 2) is None
    True
    """
    ans=fn_empty()
    for x in fn_domain(fn2):
        y=fn_call(fn2,x)
        z=fn_call(fn1,y)
        z=fn_call(fn1,y)
        if z is not None:
            ans=fn_remap(ans,x,z)
    return ans


def fn_inverse(fn):
    """Return a new function that is the inverse of fn.
    The inverse of a function fn is a function fn_inv such that
    fn_inv(y) = x if and only if fn(x) = y.
    If fn is not invertible, return None.

    >>> f = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3)
    >>> fn_call(fn_inverse(f), 3)
    2
    >>> g = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 2)
    >>> fn_inverse(g) is None
    True
    """
    ans=fn_empty()
    for x in fn_domain(fn):
        y=fn_call(fn,x)
        if fn_call(ans,y)is not None:
            return None
        ans=fn_remap(ans,y,x)
    return ans


# Problem 2.1
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    new_label=label(t1)+label(t2)
    b1=branches(t1)
    b2=branches(t2)
    n=min(len(b1),len(b2))
    shared=[]
    for i in range(n):
        shared+=[add_trees(b1[i],b2[i])]
    leftovers=[]
    for i in range(n,len(b1)):
        leftovers+=[copy_tree(b1[i])]
    for i in range(n,len(b2)):
        leftovers+=[copy_tree(b2[i])]
    return tree(new_label,shared+leftovers)


# Problem 2.2
def egg_between(t):
    """Return a new tree, where a 0 is inserted between every node and its branch node
    when they have the same label.
    All labels in t are guaranteed to be positive integers.

    >>> t = tree(1, [tree(2, [tree(2), tree(5)])])
    >>> print_tree(t)
    1
      2
        2
        5
    >>> print_tree(egg_between(t))
    1
      2
        0
          2
        5
    >>> print_tree(t)     # Do not mutate the original tree!
    1
      2
        2
        5
    >>> print_tree(egg_between( \
        tree(9, [tree(9, [tree(9)]), tree(8, [tree(8)]), tree(8), tree(9)]) \
    ))
    9
      0
        9
          0
            9
      8
        0
          8
      8
      0
        9
    """
    "*** YOUR CODE HERE ***"
    new_branches=[]
    for b in branches(t):
        if label(b)==label(t):
            new_branches+=[tree(0,[egg_between(b)])]
        else:
            new_branches+=[egg_between(b)]
    return tree(label(t),new_branches)


# Problem 2.3
def bigpath(t, n):
    """Return the number of rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    if label(t) >= n:
        total = 1
    else:
        total = 0
    for b in branches(t):
        total = total + bigpath(b, n - label(t))
    return total


def bigger_path(t, n):
    """Return the number of general rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    total = bigpath(t, n)
    for b in branches(t):
        total = total + bigger_path(b, n)
    return total


# Problem 2.4
def has_path(t, word):
    """Return whether there is a rooted path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."
    if label(t) != word[0]:
        return False
    if len(word) == 1:
        return True
    for b in branches(t):
        if has_path(b, word[1:]):
            return True
    return False


##########################
# Just for fun Questions #
##########################


# Problem 3
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"


def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def has_path_fold(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path_fold(greetings, 'h')
    True
    >>> has_path_fold(greetings, 'i')
    False
    >>> has_path_fold(greetings, 'hi')
    True
    >>> has_path_fold(greetings, 'hello')
    True
    >>> has_path_fold(greetings, 'hey')
    True
    >>> has_path_fold(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."

    def base_func(l):
        return "YOUR EXPRESSION HERE"
    def merge_func(l, bs):
        return "YOUR EXPRESSION HERE"

    return fold_tree(t, base_func, merge_func)(word)
