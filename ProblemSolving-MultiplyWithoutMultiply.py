def multiply(a,b):
    result = 0
    for x in range(0, abs(b)):
        result = result + a

    if abs(a) + a + abs(b) + b == 0 or abs(a) + a + abs(b) + b == a + a + b + b:
        return abs(result)

    return -(abs(result))

print(multiply(-50,-10))
