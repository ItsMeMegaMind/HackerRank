# Enter your code here. Read input from STDIN. Print output to STDOUT
# def solve(R, C, G, r, c, P):
#     for i in range(R - r + 1):
#         for j in range(C - c + 1):
#             found = True
#             for k in range(r):
#                 if P[k] != G[i + k][j:j + c]:
#                     found = False
#                     break
#             if found:
#                 return "YES"
#     return "NO"
#
#
# T = int(input())
# for _ in range(T):
#     R, C = (int(x) for x in input().strip().split())
#     G = [input().strip() for i in range(R)]
#
#     r, c = (int(x) for x in input().strip().split())
#     P = [input().strip() for i in range(r)]
#
#     print(solve(R, C, G, r, c, P))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        out = "No"
        for i in range(R - r + 1):
            for j in range(C - c + 1):
                found = True
                for k in range(r):
                    if P[k] != G[i + k][j:j + c]:
                        found = False
                        break
                if found:
                    out = "YES"
                    break
        print(out)
