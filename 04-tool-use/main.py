from decimal import Decimal, getcontext

def greeting():
    print("Hi there")


def calculate_pi_5_digits():
    """
    Calculate pi to the 5th digit using the Machin formula:
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: pi approximated to 5 decimal places (3.14159)
    """
    # Set precision high enough for accurate calculation
    getcontext().prec = 50
    
    # Machin's formula: pi = 16*arctan(1/5) - 4*arctan(1/239)
    one = Decimal(1)
    five = Decimal(5)
    two_three_nine = Decimal(239)
    
    # Calculate arctan using Taylor series
    def arctan(x, num_terms=100):
        """Calculate arctan(x) using Taylor series"""
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    pi = 4 * (4 * arctan(one / five) - arctan(one / two_three_nine))
    
    # Round to 5 decimal places
    pi_5_digits = float(pi)
    return round(pi_5_digits, 5)


def calculate_pi_5_digits_simple():
    """
    Alternative simpler method using the Bailey–Borwein–Plouffe formula approximation.
    This uses a series summation approach.
    
    Returns:
        float: pi approximated to 5 decimal places (3.14159)
    """
    from decimal import Decimal, getcontext
    
    getcontext().prec = 50
    
    # Using Chudnovsky algorithm (simplified version)
    pi = Decimal(0)
    for k in range(100):
        term = (Decimal(-1) ** k) * (Decimal(6*k).factorial()) * (Decimal(545140134*k + 13591409))
        term /= (Decimal(3*k).factorial() * (Decimal(k).factorial() ** 3) * (Decimal(640320) ** (Decimal(3*k + Decimal(3/2)))))
        pi += term
    
    pi = 1 / (12 * pi)
    return round(float(pi), 5)