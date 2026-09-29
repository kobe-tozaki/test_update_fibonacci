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
def quadnacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3: 
        retur 3
    else :
        return quadnacci(n-1)+quadnacci(n-2)+quadnacci(n-3)+quadnacci(n-4)

n=int(input("n = "))
print(fibonacci(n))
m=int(input("m = "))
print(tribonacci(m))
l=int(input("l = "))
print(quadnacci(l))
