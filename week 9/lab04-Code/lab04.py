from ADT import (
    make_item_stack,
    get_type,
    get_num,
    tree,
    label,
    branches,
    is_leaf,
    print_tree,
)

# ANSWER QUESTION q1


# Problem 4.1.1
def fst(p):
    return p(0)


def snd(p):
    return p(1)


def pair(x, y):
    """Return a function that represents a pair.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    """
    return lambda i: x if i == 0 else y


def change_fst(p, v):
    """Change pair p's first element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_fst(p, 3)
    >>> fst(p)
    3
    >>> snd(p)
    2
    """
    "*** YOUR CODE HERE ***"
    second=snd(p)
    return pair(v,second)


def change_snd(p, v):
    """Change pair p's second element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_snd(p, 3)
    >>> fst(p)
    1
    >>> snd(p)
    3
    """
    "*** YOUR CODE HERE ***"
    first=fst(p)
    return pair(first,v)

# Problem 4.1.2.1
def stack_verdict(s1, s2):
    """
    Return a string describing what happens when merging two stacks.

    >>> stack_verdict(make_item_stack('dirt', 40), make_item_stack('stone', 30))
    'different'
    >>> stack_verdict(make_item_stack('dirt', 40), make_item_stack('dirt', 24))
    'fits'
    >>> stack_verdict(make_item_stack('dirt', 40), make_item_stack('dirt', 25))
    'overflow'
    """
    "*** YOUR CODE HERE ***"
    if get_type(s1)!=get_type(s2):
        return 'different'
    if get_num(s1)+get_num(s2)>64:
        return 'overflow'
    return 'fits'


# Problem 4.1.2.2
def stack_up(s1, s2):
    """
    Merge two stacks into a pair of stacks.

    >>> p = stack_up(make_item_stack('dirt', 40), make_item_stack('stone', 30))
    >>> get_type(fst(p))
    'dirt'
    >>> get_num(fst(p))
    40
    >>> get_type(snd(p))
    'stone'
    >>> get_num(snd(p))
    30
    >>> p = stack_up(make_item_stack('dirt', 40), make_item_stack('dirt', 24))
    >>> get_num(fst(p))
    64
    >>> get_num(snd(p))
    0
    >>> get_type(fst(p)) == get_type(snd(p)) == 'dirt'
    True
    >>> p = stack_up(make_item_stack('dirt', 40), make_item_stack('dirt', 25))
    >>> get_num(fst(p))
    64
    >>> get_num(snd(p))
    1
    >>> get_type(fst(p)) == get_type(snd(p)) == 'dirt'
    True
    """
    "*** YOUR CODE HERE ***"
    if stack_verdict(s1,s2)=='different':
        return pair(s1,s2)
    if stack_verdict(s1,s2)=='overflow':
        s3=make_item_stack(get_type(s1),64)
        s4=make_item_stack(get_type(s1),get_num(s1)+get_num(s2)-64)
        return pair(s3,s4)
    s3=make_item_stack(get_type(s1),get_num(s1)+get_num(s2))
    s4=make_item_stack(get_type(s1),0)
    return pair(s3,s4)


# Problem 4.2.1
def deep(l):
    """Returns a deep-copy of the given list of lists.
    >>> a = [[2, 2, 2], [5, 0, 2], [5, 0, 3]]
    >>> b = deep(a)
    >>> b
    [[2, 2, 2], [5, 0, 2], [5, 0, 3]]
    >>> a is b
    False
    >>> a[0] is b[0]
    False
    >>> a[1] is b[1]
    False
    >>> a[2] is b[2]
    False
    >>> len(a) == len(b)
    True
    """
    "*** YOUR CODE HERE ***"
    return [cpy[:] for cpy in l]


# Problem 4.2.2
def my_reverse(l):
    """Returns a new list that contains the exact same elements in l with reversed order.
    >>> a = ['S', 'I', 'C', 'P']
    >>> a is my_reverse(a) # the returned list is newly created
    False
    >>> my_reverse(my_reverse(a)) == a # reverse twice equals to the original list
    True
    >>> my_reverse(a)
    ['P', 'C', 'I', 'S']
    >>> a
    ['S', 'I', 'C', 'P']
    """
    "*** YOUR CODE HERE ***"
    n=len(l)
    return l[::-1]


# Problem 4.2.3
def my_split(f, l):
    """Splits the list into two lists according to predicate f.
    >>> my_split(lambda x: True, [1, 2, 3, 4]) # All elements from l conforms to the predicate
    [[1, 2, 3, 4], []]
    >>> my_split(lambda x: x % 2 == 0, [1, 2, 3, 4]) # Split into even and odd numbers
    [[2, 4], [1, 3]]
    >>> my_split(lambda x: x < 5, [3, 1, 4, 1, 5, 9, 2])
    [[3, 1, 4, 1, 2], [5, 9]]
    >>> my_split(lambda x: not x, [True, False, True, True]) # There might be things other than integers
    [[False], [True, True, True]]
    >>> is_ldx = lambda x: not x.startswith('24')
    >>> studentIDs = ['24122', '22122', '502024', '24183']
    >>> my_split(is_ldx, studentIDs)[0]
    ['22122', '502024']
    >>> studentIDs # You should not mutate the original list
    ['24122', '22122', '502024', '24183']
    """
    "*** YOUR CODE HERE ***"
    list1=[i for i in l if f(i)]
    list2=[i for i in l if not f(i)]
    return [list1,list2]


# Problem 4.3.1
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    ans=[label(t)]
    for i in branches(t):
        ans=ans+preorder(i)
    return ans


# Problem 4.3.2
def is_binary(t):
    """Returns True if t is a binary tree (each node has at most two children).

    >>> is_binary(tree(1))
    True
    >>> is_binary(tree(1, [tree(2), tree(3)]))
    True
    >>> is_binary(tree(1, [tree(2), tree(3), tree(4)]))
    False
    >>> is_binary(tree(1, [tree(2), tree(4, [tree(5), tree(6)])]))
    True
    >>> is_binary(tree(1, [tree(2), tree(4, [tree(5, [tree(6), tree(7)]), tree(8), tree(9)])]))
    False
    """
    "*** YOUR CODE HERE ***"
    if len(branches(t))>2:
        return False
    if len(branches(t))==2:
        return is_binary(branches(t)[0]) and is_binary(branches(t)[1])
    if len(branches(t))==1:
        return is_binary(branches(t)[0])
    return True

# Problem 4.3.3
def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    ans=[]
    if is_leaf(t):
        for val in values:
            ans.append(tree(val))
    else:
        for bran in branches(t):
            ans.append(sprout_leaves(bran,values))
    return tree(label(t),ans)

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> insert_items(test_lst, 5, 7)
    >>> test_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> insert_items(large_lst, 4, 4)
    >>> large_lst
    [1, 4, 4, 8]
    >>> insert_items(large_lst, 4, 6)
    >>> large_lst
    [1, 4, 6, 4, 6, 8]
    """
    "*** YOUR CODE HERE ***"
    ans=[]
    #flag=False
    for i in lst:
        ans=ans+[i]
        if i==entry:
            ans=ans+[elem]
            #flag=True
    lst[:]=ans          
