def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial: ", factorial(10))
# Time Complexity = O(log(n))
# Space Complexity = O(log(n)) + θ(1) = O(log(n))
