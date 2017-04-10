# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(case, s,k):
    r = get_rep(s)
    print(k)
    print(s)
    print(r)
    more = True
    flip = 0
    change = True
    it = 0

    while(change and it < 1000 and len(r) > 1):
        it = it+1
        change = False


        i = 0
        while (i < len(r)-1 and not change):
            if sign(r[i]) == sign(r[i+1]):
                r[i] = r[i]+r[i+1]
                r.pop(i+1)

                change = True
            i = i+1

        i = 0
        end = False
        while (i < len(r) - 1 and not end and not change):
            if abs(r[i])+abs(r[i + 1]) == k:
                r[i] = r[i]*-1
                r[i+1] = r[i+1] * -1
                flip = flip +1
                end = True
                change = True
            i=i+1
        i=0
        while (i < len(r) - 1 and not end and not change):
            if abs(r[i]) == k:
                r[i] = r[i]*-1
                flip = flip +1
                change = True
            i=i+1

        i=0
        print(r)
        while (i < len(r) - 1  and not change):
            if abs(r[i]) % k == 0:
                r[i] = r[i]*-1
                flip = flip +int(abs(r[i]) / k )

            i=i+1

    impossible = False

    for e in r:
        if e < 0:
            if not abs(e) % k == 0:
                impossible = True
            else:
                flip = flip+int(abs(e) / k)

    if (impossible):
        return 'IMPOSSIBLE'
    else:
        return str(flip)

def sign(i):
    return i >= 0

def get_rep(s):
    count = 1
    actual = s[0]
    res = []

    for i in range(1, len(s)):
        if (s[i] == actual):
            count = count+1
        else:
            if actual == '-':
                res.append(count*-1)
            else:
                res.append(count)
            count = 1
            actual = s[i]

    if actual == '-':
        res.append(count * -1)
    else:
        res.append(count)

    return res

t = int(input())  # case qty
for case in range(1, t + 1):
    # Single Int: int(input())
    # Many Int: [int(s) for s in input().split(" ")]

    info = input().split(" ")
    s = info[0]
    k = int(info[1])

    solution = solve(case, s, k)

    print("Case #{}: ".format(str(case)) + solution)