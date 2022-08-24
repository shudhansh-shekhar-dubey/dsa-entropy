def fib(n):
    identity = carry = [[1,0],[0,1]]
    single = matrix = [[1,1],[1,0]] 
    power = 1
    if n == 0:
        return 0
    while n > 1: 
        if n % 2 != 0:
            n = (n-1) / 2
            if power > 1: 
                carry = multiply(carry, matrix) 
            else:
                carry = single
        else:
            n = n / 2      
        matrix = multiply(matrix, matrix)
        power = power * 2
    if carry != identity:
        matrix = multiply (matrix, carry)
      
    return matrix[0][1]
          

def multiply(a, b):
    result = [[1, 1], [1, 0]]
    result[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    result[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    result[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    result[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1] 
    return result
