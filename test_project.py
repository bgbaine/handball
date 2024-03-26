#################################################
#    cs50p/fproject/project/test_project.py/    #
#    Final project                              #
#################################################

import pytest
from project import ensure_color, set_color, set_speed


# Test ensure_color for different color inputs
def test_ensure_color():
    with pytest.raises(SystemExit):
        ensure_color('211')

    assert ensure_color(-1) == 0
    assert ensure_color(256) == 255
    assert ensure_color(211) == 211


# Test set_color for different tuples
def test_set_color():
    with pytest.raises(SystemExit):
        set_color('211', 211, 211)

    assert set_color(-1, -1, -1) == (0, 0, 0)
    assert set_color(256, 256, 256) == (255, 255, 255)
    assert set_color(211, 211, 211) == (211, 211, 211)


# Test set_speed for different objects and speeds
def test_set_speed():
    with pytest.raises(SystemExit):
        set_speed(0, '12')
        set_speed(1, '18')

    assert set_speed(0, 5) == 12
    assert set_speed(0, 16) == 12
    assert set_speed(0, 12) == 12
    assert set_speed(1, 11) == 18
    assert set_speed(1, 26) == 18
    assert set_speed(1, 18) == 18
