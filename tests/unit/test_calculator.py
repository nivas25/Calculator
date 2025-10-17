"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
# Added 'multiply' to the import list
from src.calculator import add, divide, subtract, multiply, power, square_root

class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# Implemented the TODO below
# TODO: Students will add TestMultiplyDivide class

class TestMultiplyDivide:
    """Test multiplication and division operations."""

    def test_multiply(self):
        """Test multiplication of various numbers."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(-5, -5) == 25
        assert multiply(10, 0) == 0

    def test_divide(self):
        """Test standard division."""
        assert divide(10, 2) == 5
        assert divide(20, -4) == -5
        # Test for floating point results
        assert divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        """Test that division by zero raises a ValueError."""
        # After
        with pytest.raises(ValueError, match="Cannot divide 10 by zero"):
            divide(10, 0)


class TestAdvancedOperations: 
    """Test power and square root operations""" 
     
    def test_power_positive_numbers(self): 
        """Test power with positive numbers""" 
        assert power(2, 3) == 8 
        assert power(5, 2) == 25 
     
    def test_power_zero_exponent(self): 
        """Test power with zero exponent""" 
        assert power(5, 0) == 1 
        assert power(0, 0) == 1 
     
    def test_square_root_positive_numbers(self): 
        """Test square root of positive numbers""" 
        assert square_root(4) == 2 
        assert square_root(9) == 3 
        assert square_root(16) == 4 
     
    def test_square_root_negative_raises_error(self): 
        """Test that square root of negative raises ValueError"""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative"): 
            square_root(-4)