"""
    Calculate the nth Fibonacci number.

    Parameters:
        n (int): The position of the desired Fibonacci number.
    
    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If the input is not a positive integer.

    Example:
        >>> fibonacci(1)
        0
        >>> fibonacci(2)
        1
        >>> fibonacci(6)
        5
        >>> fibonacci(10)
        34
    """

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq[-1]