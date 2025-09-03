# #---iterative------
# def factorial(n):
#     f = 1
#     while(n != 0):
#         f = f * n
#         n -= 1
#     return f

# print(factorial(10))

#----recursive---

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        n = n * factorial_recursive(n-1)
        return n

print(factorial_recursive(7))

