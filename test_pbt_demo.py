import unittest
from hypothesis import given
from hypothesis.strategies import text, lists, integers, floats, tuples, booleans, sampled_from
from hypothesis import example
from hypothesis import note
from hypothesis import assume
from math import isnan
from hypothesis import find

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

#####################################################################################


@given(s=text())
@example(s='')
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
    assert len(s.upper()) == len(s)


#####################################################################################


@given(integers(), integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x


@given(x=integers(), y=integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x


@given(lists(integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys


@given(tuples(booleans(), text(alphabet='abcdef', min_size = 3, max_size = 5)))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], basestring)


@given(a = sampled_from(['AZ-adbf', 'AX-ss', ''])
     , b = text(alphabet='abcdef', min_size = 0, max_size = 3)
     , c = text(alphabet='abcdef', min_size = 0, max_size = 3)
     , d = integers(1, 65535))
def test_look_tuples_work_too(a, b, c, d):
    #assume(sum(1 for var in [a,b,c] if var == '') == 1)
    #print str([a, b, c, d])
    pass


@given(integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    assert i % 2 == 0


@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):
    assume(not isnan(x))
    assert x == -(-x)


@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):
    #assume(False)
    #assert x == -(-x)
    pass


#####################################################################################

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print find(lists(integers()), lambda x: sum(x) >= 10)
        #print tuples(integers(), integers()).example()



class TestTryReallyHard(unittest.TestCase):
    @given(integers())
    def test_something(self, i):
        pass

    def execute_example(self, f):
        f()
        return f()

