
def utopianTree(a):
    n = 0
    h=1
    if(a==0):
        return h
    else:
        while(n<a):
            if(n%2==0):
                h*=2
                n+=1
            else:
                h+=1
                n+=1
        return h

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        h = int(input())

        print(utopianTree(h))


