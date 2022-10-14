"""
CAPP 121: Language shifts
Test code for median_language_shift_length function
"""

import os
import sys
import pytest

timeout = 60

# Handle the fact that the grading code may not 
# be in the same directory as language.py
sys.path.insert(0, os.getcwd())

# Get the test files from the same directory as
# this file
BASE_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(BASE_DIR, "tests")

# Keep pylint from complaining aboutenerated code.
#pylint: disable-msg=wrong-import-position
#pylint: disable-msg=missing-docstring

from language import median_language_shift_length
import test_helpers
import utility

def helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps):
    """
    Do one simulation with the specified parameters and
      match the actual frequencies with expected frequencies
    
    Inputs:
     nput_filename (string): the gridile
      R (int): neighborhood radius
      threshold_list (list of tuples): a list of language state transition
        thresholdsA, B, C)
      centerslist of tuples): a list of community centersn the
        region
      max_stepsint): maximum number of steps
      expected_medium_num_steps (int): the expected medium language shift length
    """

    input_filename = os.path.join(TEST_DIR, input_filename)
    actual_grid, centers = utility.read_grid(input_filename)
    actual_medium_num_steps = median_language_shift_length(actual_grid, R, threshold_list, centers, max_steps)
    
    recreate_msg = "To recreate this testn ipython3 run:\n"
    recreate_msg += "    region, centers = utility.read_grid('{}')\n"
    recreate_msg += "    threshold_list = {}\n"
    recreate_msg += "    language.median_language_shift_length(region, {}, threshold_list, centers, {})"
    recreate_msg = recreate_msg.format(input_filename, threshold_list, R, max_steps)

    if actual_medium_num_steps != expected_medium_num_steps:
        msg = "Actual and expected medium number of steps don't match.\n"
        msg= "    Actual: {}\n"
        msg= "    Expected: {}\n"
        msg = msg.format(actual_medium_num_steps, expected_medium_num_steps)
        msg = msg + "\n" + recreate_msg
        pytest.fail(msg)

def test_median_language_shift_length_1():
    input_filename = 'writeup-grid.txt'
    R = 1
    threshold_list = [(0.6, 0.6, 1.6), (0.6, 0.8, 1.6), (0.6, 1.0, 1.6), (0.6, 1.2, 1.6), (0.6, 1.4, 1.6)]
    max_steps = 20
    expected_medium_num_steps = 3
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_2():
    input_filename = 'writeup-grid.txt'
    R = 1
    threshold_list = [(0.6, 0.8, 1.6), (0.8, 0.8, 1.6), (0.8, 0.8, 1.4), (0.6, 1.0, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  4
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_3():
    input_filename = 'writeup-grid.txt'
    R = 2
    threshold_list = [(0.8, 1.0, 1.2), (0.8, 1.2, 1.4), (0.8, 1.2, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  3
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_4():
    input_filename = 'writeup-grid-with-cc.txt'
    R = 1
    threshold_list = [(0.6, 0.6, 1.6), (0.6, 0.8, 1.6), (0.6, 1.0, 1.6), (0.6, 1.2, 1.6), (0.6, 1.4, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  3
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_5():
    input_filename = 'writeup-grid-with-cc.txt'
    R = 2
    threshold_list = [(0.6, 0.8, 1.6), (0.8, 0.8, 1.6), (0.8, 0.8, 1.4), (0.6, 1.0, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  3
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_6():
    input_filename = 'writeup-grid-with-cc.txt'
    R = 3
    threshold_list = [(0.8, 1.0, 1.2), (0.8, 1.2, 1.4), (0.8, 1.2, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  2
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_7():
    input_filename = 'medium-grid.txt'
    R = 1
    threshold_list = [(0.6, 0.6, 1.6), (0.6, 0.8, 1.6), (0.6, 1.0, 1.6), (0.6, 1.2, 1.6), (0.6, 1.4, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  4
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_8():
    input_filename = 'medium-grid.txt'
    R = 2
    threshold_list = [(0.6, 0.8, 1.6), (0.8, 0.8, 1.6), (0.8, 0.8, 1.4), (0.6, 1.0, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  4
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_9():
    input_filename = 'large-grid.txt'
    R = 3
    threshold_list = [(0.6, 0.6, 1.6), (0.6, 0.8, 1.6), (0.6, 1.0, 1.6), (0.6, 1.2, 1.6), (0.6, 1.4, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  4
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)

def test_median_language_shift_length_10():
    input_filename = 'large-grid.txt'
    R = 5
    threshold_list = [(0.6, 0.8, 1.6), (0.8, 0.8, 1.6), (0.8, 0.8, 1.4), (0.6, 1.0, 1.6)]
    max_steps = 20
    expected_medium_num_steps =  3
    helper_test_median_language_shift_length(input_filename, R, threshold_list, max_steps, expected_medium_num_steps)
