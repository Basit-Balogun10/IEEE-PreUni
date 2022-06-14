from math import sqrt

def solve_quadratic_eqn(a: int, b: int, c: int):
    first_sol = (-b + sqrt((b ** 2) - (4 * a * c))) / 2 * a
    second_sol = (-b - sqrt((b ** 2) - (4 * a * c))) / 2 * a
    
    return first_sol, second_sol

print(solve_quadratic_eqn(1, -1, -6))