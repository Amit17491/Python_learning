# calculate the factorial using the recursion.
def fact(n):
    # base case
    if (n == 0 or n == 1):
        return 1
    else:
        big_problem = n * fact(n-1)
        return big_problem
num = 5
fact_answer = fact(num)
print(fact_answer)