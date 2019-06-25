def kaprekarNumbers(p, q):
    out = []
    for i in range(p, q+1):
        l = len(str(i))
        sq = list(str((i ** 2)))
        dif = len(sq) - l
        l = ''.join(sq[:dif])
        r = ''.join(sq[dif:])
        l = 0 if l=="" else int(l)
        if(l+int(r)==i): out.append(i)
    if len(out)==0:
        print("INVALID RANGE")
    else: print(*out)
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)