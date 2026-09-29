def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
def tribonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else :
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

n=int(input("n = "))
print(fibonacci(n))
m=int(input("m = "))
print(tribonacci(m))
