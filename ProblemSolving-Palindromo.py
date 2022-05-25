
def isPalindrome(x):
        
        number = str(x)

        if number == number[::-1]:
            return True
        else:
            return False

def isPalindrome_number(x):
    n = x
    rev = 0

    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10

    if x == rev:
        return True
    else:
        return False


print(isPalindrome(121))

print(isPalindrome_number(121))

