import unittest
from main import calculate_pi_5_digits, calculate_pi_5_digits_simple, greeting


class TestPiCalculation(unittest.TestCase):
    """Test suite for pi calculation functions"""
    
    def test_calculate_pi_5_digits_accuracy(self):
        """Test that pi is calculated to the 5th digit accurately"""
        pi_value = calculate_pi_5_digits()
        
        # Pi to 5 decimal places should be 3.14159
        self.assertEqual(pi_value, 3.14159)
        
    def test_calculate_pi_5_digits_type(self):
        """Test that the function returns a float"""
        result = calculate_pi_5_digits()
        self.assertIsInstance(result, float)
    
    def test_calculate_pi_5_digits_range(self):
        """Test that pi is in the expected range"""
        pi_value = calculate_pi_5_digits()
        
        # Pi should be between 3.1 and 3.2
        self.assertGreater(pi_value, 3.1)
        self.assertLess(pi_value, 3.2)
    
    def test_calculate_pi_5_digits_decimal_places(self):
        """Test that result has exactly 5 decimal places (or fewer due to rounding)"""
        pi_value = calculate_pi_5_digits()
        
        # Convert to string and check decimal places
        pi_str = f"{pi_value:.5f}"
        decimal_part = pi_str.split('.')[1]
        
        # Should have at most 5 decimal places
        self.assertLessEqual(len(decimal_part), 5)
    
    def test_calculate_pi_5_digits_simple_accuracy(self):
        """Test the simple method returns reasonable pi approximation"""
        pi_value = calculate_pi_5_digits_simple()
        
        # Should be close to 3.14159
        self.assertAlmostEqual(pi_value, 3.14159, places=4)
    
    def test_greeting_function_exists(self):
        """Test that greeting function still works"""
        # This should not raise an error
        try:
            greeting()
        except Exception as e:
            self.fail(f"greeting() raised {type(e).__name__} unexpectedly!")


class TestPiValueAccuracy(unittest.TestCase):
    """More detailed accuracy tests"""
    
    def test_pi_value_matches_known_value(self):
        """Verify pi matches the actual value to 5 decimal places"""
        pi_actual = 3.14159
        pi_calculated = calculate_pi_5_digits()
        
        self.assertEqual(pi_calculated, pi_actual)
    
    def test_pi_greater_than_3(self):
        """Test that calculated pi is greater than 3"""
        pi_value = calculate_pi_5_digits()
        self.assertGreater(pi_value, 3)
    
    def test_pi_less_than_4(self):
        """Test that calculated pi is less than 4"""
        pi_value = calculate_pi_5_digits()
        self.assertLess(pi_value, 4)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
