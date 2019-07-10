def isPalin(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]: return False
    return True


def palindromeIndex(s):
    for i in range((len(s) + 1) // 2):
        if s[i] != s[len(s) - i - 1]:
            if isPalin(s[:i] + s[i + 1:]):
                return i
            else:
                print("HERE")
                return len(s) - i - 1
    return -1


for i in range(0, int(input())):
    x = input()
    result = palindromeIndex(x)
    print(result)