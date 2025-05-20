import pytest
import math
from geometry.shapes import Circle, Triangle
from geometry.area_calculator import calculate_area


def test_circle_area():
    c = Circle(3)
    expected = math.pi * 9
    assert math.isclose(c.area(), expected)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)


def test_right_triangle():
    t = Triangle(5, 3, 4)
    assert t.is_right()


def test_not_right_triangle():
    t = Triangle(3, 4, 6)
    assert not t.is_right()


def test_calculate_area_circle():
    c = Circle(2)
    assert math.isclose(calculate_area(c), math.pi * 4)


def test_calculate_area_triangle():
    t = Triangle(7, 8, 9)
    assert math.isclose(calculate_area(t), t.area())


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 100)


def test_invalid_object():
    class Fake:
        pass

    with pytest.raises(TypeError):
        calculate_area(Fake())
