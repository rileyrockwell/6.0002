def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
    
for i in range(3, 9):
    print(factorial(i))