if __name__ == '__main__':
    string, k = input(), int(input())
    loop = len(string) // k
    for i in range(0, len(string), k):
        a = string[i:i + k]
        print("".join(dict(zip(a, a)).keys()))