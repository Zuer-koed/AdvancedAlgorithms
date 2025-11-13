def factorial(n):
    """
    Calculate the factorial of a given number n.

    Args:
        n (int): The number to calculate factorial for

    Returns:
        int: The factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
BIG-O TIME COMPLEXITY ANALYSIS:

Time Complexity: O(n) - Linear time complexity

Explanation:
- The function performs a constant number of operations per iteration
- Number of iterations grows linearly with input size n
- Total operations = 1 + 3n (1 assignment + n iterations × 3 operations)
- Therefore, time complexity is O(n)
"""

if __name__ == "__main__":
    # Test the factorial function
    print("Factorial Function Test:")
    print(f"5! = {factorial(5)}")
    print(f"10! = {factorial(10)}")