triple = [[],[],[]]
print(triple)
triple[1].append("abc")
triple[1].append(123)
print(triple)

jank = [[]]*3
print(jank)
jank[1].append('jank')
print(jank)



# returns a single (concatenated) list instead of nested
notnested = list(['x','y','z']*3)
# the surrounding 'list()' has no effect on either of these, by the way
nested = list([['x','y','z']]*3)

[['w','t','f']]*2 == [['w', 't', 'f'], ['w', 't', 'f']]
[['w','t','f']*2] == [['w','t','f', 'w','t','f']]

# multiplying a list by zero always collapses into a completely empty list
[[['a','b','c']], [1,2,3]]*0 == []
[[[],[]]]*0 == []

# empty lists are not auto-collapsed during these operations
[[[]]]*1 != []
[[[],[]]]*1 != []
# it's not actually inconsistent, just unintuitive
[[[],[]]*0] == [[]]
[[[],[]]*1] == [[[], []]]

# it's repeating the elements inside of the inner list
[1]*3 == [1, 1, 1]
[[1]*3] == [[1, 1, 1]]
[[1]]*3 == [[1], [1], [1]]
# multiplying an empty list or tuple does nothing
[[]*3] == [[]]
[[]]*3 == [[], [], []]


## tuple syntax pitfalls ##
# behavior is consistent with lists
('a','b')*2 == ('a', 'b', 'a', 'b')

# unless you only have one element (syntax lmao)
('a')*2 == 'aa'     # result is NOT a tuple
('a',)*2 == ('a', 'a')  # this is what you want
# and of course, you can't wrap the whole thing in a tuple by just adding parentheses;
# remember, you still need a comma to create the outermost tuple, otherwise you miss a nesting level
([['a']]*2) != ([['a']]*2,)  # the first one does not create a tuple!


# wrapping in a tuple 
([['a']]*2,) == ([['a'], ['a']],)
([['a']],)*2 == ([['a']], [['a']])


# lmao operator precedence
([['a']]*2,) == [['a']]*2,  # (False,)
([['a']]*2,) == ([['a']]*2),  # (False,)


# Here, two tuples are created with the same values, but with different syntax
# performing an equality test between the variables passes, but
# an equality between the expressions used to create them fails (due to operator precedence)
synone = (['lol']*2,)
syntwo = ['lol']*2,
# both variables are equal to: (['lol', 'lol'],)
synone == syntwo
# direct comparison returns (False,)
(['lol']*2,) == ['lol']*2,
# (['lol']*2,) == 2*['lol'],  # still '(False,)'
(['lol']*2,) == (2*['lol'],)  # True


# TODO: abuse this syntax somehow
((),) == ((),)
(),   == ((),)


# nesting tuples gets incredibly ugly
((('a','b'),)*2,) == ((('a', 'b'), ('a', 'b')),)
((('a','b'),),)*2 == ((('a', 'b'),), (('a', 'b'),))


# with tuples, you can't nest by just add more parentheses (tuples must contain a comma)
((((('a','b'))))*2) == ('a', 'b', 'a', 'b')


[['w','t','f']]*0 == []
[['w','t','f']*0] == [[]]


True, True, True == (True, True, True)
# (True, True, False)
(True, True, True,) == True, True, True,
# (False, True, True)




