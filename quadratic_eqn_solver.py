# THIS IMPORTS THE sqrt FUNCTION from the math module which is comes built-in with python
from math import sqrt

# WE IMPLEMENT THE FAMOUS QUADRATIC FORMULA LOGIC IN THE FUNCTION BELOW
def solve_quadratic_eqn(a: int, b: int, c: int):
    """This function takes two three arguments a, b and c as described below.
    And all three arguments are expected to be integers.

    Args:
        a (int): The coefficient of the unknown term raised to the power of 2 (e.g x^2) in the quadratic equation
        b (int): The coefficient of the unknown (e.g x) in the quadratic equation
        c (int): The constant term in of the quadratic equation

    Returns:
        tuple(iterable): A tuple of the two solutions/roots of the quadratic equation
    """
    
    # THE NEXT TWO LINES CALCULATES THE FIRST AND SECOND ROOTS OF THE QUADRATIC EQUATION
    first_sol = (-b + sqrt((b ** 2) - (4 * a * c))) / 2 * a
    second_sol = (-b - sqrt((b ** 2) - (4 * a * c))) / 2 * a
    
    return first_sol, second_sol

a = int(input('Enter a: ')) # WE REQUIRE AN INPUT FROM THE USER FOR a
b = int(input('Enter b: ')) # WE REQUIRE AN INPUT FROM THE USER FOR b
c = int(input('Enter c: ')) # WE REQUIRE AN INPUT FROM THE USER FOR c

# WE CALL THE solve_quadratic_eqn FUNCTION DEFINED ABOVE AND PRINT OUT THE VALUE RETURNED.
print(solve_quadratic_eqn(a, b, c)) # prints out something in the form: (root1, root2)