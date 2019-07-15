
if __name__ == '__main__':
    string, k = input(), int(input())
    i = 0
    for i in range(0, len(string), k):
        s = (string[i:i + k])
        uniqs = ''
        for x in s:
            if not (x in uniqs):
                uniqs = uniqs + x
        print(uniqs)