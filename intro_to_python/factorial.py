
#My not elegant solution
# def factorial(n):
#     facto = 1
#     result = 1
#     while facto <= n:
#         result = result * facto
#         facto += 1
#         print(result)
#     return result
# num = factorial(7)
# print(num)

def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number