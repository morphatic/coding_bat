'''
Unit tests for the monkey_trouble function for [this Coding Bat problem](https://codingbat.com/prob/p120546)
'''
# pylint: disable=unused-variable

# import the code to be tested
from monkey_trouble import monkey_trouble

# begin writing tests (top-level test suite)
def describe_a_monkey_trouble_function():

  def that_determines_whether_or_not_we_are_in_trouble():
    '''
    There are 2 monkeys who may or may not be smiling. If both
    or neither of them are smiling, we are in trouble. Return
    True if we are in trouble
    '''
    assert monkey_trouble(True, True) == True # BOTH smiling ==> Trouble
    assert monkey_trouble(True, False) == False # mixed ==> OK
    assert monkey_trouble(False, True) == False # mixed ==> OK
    assert monkey_trouble(False, False) == True # NEITHER smiling ==> Trouble
    