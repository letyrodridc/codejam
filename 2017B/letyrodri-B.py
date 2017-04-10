# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(case, n):
    i = 0
    nrev = n[::-1]

    while(i < len(n)-1):
        m = max(nrev[i+1:])
        if (nrev[i] < max(nrev[i+1:])):
            n = str(int(n) - pow(10, i))
            nrev = n[::-1]
            i=0
        else:
            i=i+1


    '''
    while(i < len(n) and pos > 0):

        m = max(n[0:pos])
        if (int(n[pos]) < int(m)):
            n = str(int(n)-pow(10,i))
            pos = min(pos, len(n) - 1)
        else:
            i=i+1
            pos=pos-1
    '''
    return n

t = int(input())  # case qty
for case in range(1, t + 1):
    # Single Int: int(input())
    # Many Int: [int(s) for s in input().split(" ")]
    n = input()

    solution = solve(case, n)

    print("Case #{}: ".format(str(case)) + solution)