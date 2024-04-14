def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")
    num_iterations = 0
    while (b - a) / 2 > tol and num_iterations < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c, num_iterations
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        num_iterations += 1
    root = (a + b) / 2
    return root, num_iterations
def get_user_function():
    expression = input("Enter the function in terms of 'x': ")
    return lambda x: eval(expression)
def main():
    try:
        # Get user input
        function = get_user_function()
        a = float(input("Enter the lower bound of the interval: "))
        b = float(input("Enter the upper bound of the interval: "))
        #tolerance = float(input("Enter the tolerance: "))
        #max_iterations = int(input("Enter the maximum number of iterations: "))
        # Perform bisection method
        root, iterations = bisection_method(function, a, b, tol=1e-6, max_iter=100)
        # Print the result
        print(f"Approximate root: {root}")
        print(f"Iterations performed: {iterations}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

main()
