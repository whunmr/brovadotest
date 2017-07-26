import unittest
from hypothesis import given, settings, Verbosity
from hypothesis.strategies import *
from hypothesis import example
from hypothesis import note
from hypothesis import assume
from math import isnan
from hypothesis import find
from dateutil.parser import parse

# # https://hypothesis.readthedocs.io/en/master/quickstart.html
#
# # pip install hypothesis
#

def encode(input_string):
    if not input_string:
        return []

    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q

# #####################################################################################


# @given(s=text())
# @example(s= 'hello')
# @example(s= 'hello dsdf')
# @example(s= 'hello sdfsdfsadfd')
# def test_decode_inverts_encode(s):
#     print s
#     assert decode(encode(s)) == s


# #####################################################################################
#
#
# @given(integers(), integers())
# def test_ints_are_commutative(x, y):
#     print (x, y)
#     assert x + y == y + x
#
#

# @given(x=integers(), y=integers())
# def test_ints_cancel(x, y):
#     assert (x + y) - y == x

#
#

# @given(lists(booleans()))
# def test_reversing_twice_gives_same_list(xs):
#     print xs
#     ys = list(xs)
#     ys.reverse()
#     ys.reverse()
#     assert xs == ys

#
#

# @given(tuples(booleans(), text(alphabet='xyz', min_size = 8, max_size = 8)))
# @settings(max_examples=5)
# def test_look_tuples_work_too(t):
#     # A tuple is generated as the one you provided, with the corresponding
#     # types in those positions.
#     print t
#     assert len(t) == 2
#     assert isinstance(t[0], bool)
#     assert isinstance(t[1], basestring)
#
#
# @given(a = sampled_from(['AZ-adbf', 'AX-ss', ''])
#      , b = text(alphabet='abcdef', min_size = 0, max_size = 3)
#      , c = text(alphabet='abcdef', min_size = 0, max_size = 3)
#      , d = integers(1, 65535))
# def test_look_tuples_work_too(a, b, c, d):
#     assume(sum(1 for var in [a,b,c] if var == '') == 1)
#     assume(d >= 60000)
#     assume(False)
#     print str([a, b, c, d])

#
#
# @given(integers().filter(lambda x: x % 2 == 0))
# def test_even_integers(i):
#     print i
#
#
# @given(floats())
# def test_negation_is_self_inverse_for_non_nan(x):
#     assume(not isnan(x))
#     assert x == -(-x)
#
#
# @given(floats())
# def test_negation_is_self_inverse_for_non_nan(x):
#     #assume(False)
#     #assert x == -(-x)
#     pass
#
#
# #####################################################################################
#
#
# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#         print find(lists(integers()), lambda x: sum(x) >= 10)
#         print find(lists(integers()), lambda x: sum(x) >= 10 and len(x) >= 3)
#         print find(sets(integers()), lambda x: sum(x) >= 10 and len(x) >= 3)
#         #print tuples(integers(), integers()).example()
#         #find(integers(), lambda x: False)
#         #print find(lists(integers()), any, settings=settings(verbosity=Verbosity.verbose))
#         #x = st.deferred(lambda: st.booleans() | st.tuples(x, x))
#
#
# class TestTryReallyHard(unittest.TestCase):
#     @given(integers())
#     def test_something(self, i):
#         pass
#
#     def execute_example(self, f):
#         f()
#         return f()
#
#
# #####################################################################################
# @given(lists(integers()))
# @settings(max_examples=5)
# def test_sorting_list_of_integers(xs):
#     assume(len(xs) > 1)
#     res = sorted(xs)
#     assert isinstance(res, list)
#     assert all(x <= y for x, y in zip(res, res[1:]))
#
#
# @given(just(3))
# def test_just(i):
#     assert i == 3
#
#
# @given(one_of(just(3), just(4)))
# def test_one_of(i):
#     assert i == 3 or i == 4

#
# @given(dictionaries(integers() ,integers()))
# @settings(max_examples=1)
# def test_justx(i):
#     assume(len(i.keys()) == 1)
#     assert len(i.keys()) == 1
#
#
# @given(characters())
# def test_characters(i):
#     assert len(i) == 1
#
# #
# @given(recursive(booleans(), lists))
# def test_recursive(i):
#     print i
#
#
# @given(times())
# def test_times(i):
#     print i
#
#
# @given(uuids())
# def test_uuids(i):
#     assert len(str(i)) > 0
#
#
# #####################################################################################

# from hypothesis.types import Stream
# x = Stream(iter(integers().example, None))
# x[2]


# #####################################################################################

#integers().filter(lambda x: x > 11)

# @given(lists(integers()).map(sorted))
# def test_uuids(i):
#     print i
#



class TestStringMethods1(unittest.TestCase):
    def test_upper(self):
        rectangle_lists = integers(min_value=0, max_value=10).flatmap(lambda n: lists(lists(integers(), min_size=n, max_size=n)))
        print find(rectangle_lists, lambda x: True)
        print find(rectangle_lists, lambda t: len(t) >= 3 and len(t[0]) >= 3)
        from string import printable
        from pprint import pprint
        json = recursive(none() | booleans() | floats() | text(printable),lambda children: lists(children) | dictionaries(text(printable), children))
        print json.example()
        print recursive(booleans(), lists, max_leaves=5).example()


