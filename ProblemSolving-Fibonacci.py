import numpy as np

def  FibLineal(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        print(a)
        a = b
        b = c
        
def FibRecursivo(n):
    if n < 2 :
        return n
    return FibRecursivo(n-1) + FibRecursivo(n-2)

# Exponenciacion rapida
def exp(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return exp(x*x, n//2)
    return x * exp(x*x, n//2)


#Fibonacci Logaritmico
def FibLog(n):
    for i in range(n):
        print(E(i))
def E(n):
    if n <= 1:
        return n 
    F = np.array([[1, 1],
                  [1, 0]])
    F = ExpRap(F, n - 1) 
    return F[0][0]
def ExpRap(M, n):
    if n == 1:
        return M
    if n % 2 == 0:
        return ExpRap(np.dot(M,M), n//2)
    return np.dot(M,ExpRap(np.dot(M,M), n//2))


if __name__ == '__main__': 
    NumerosEnLaSerie = 5

    print("Fibonacci Lineal")
    FibLineal(NumerosEnLaSerie)
    
    print("Fibonacci Recursivo")
    print(FibRecursivo(NumerosEnLaSerie - 1))
    
    print("Fibonacci Logaritmico")
    FibLog(NumerosEnLaSerie) 
