# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(case, n,k):
    dist = [ [0,0,False] for x in range(0,n+2)]
    dist[0][2] = True
    dist[n+1][2] = True

    for person in range(0,k):
        # Calculates distances
        for stall in range(0,n+2):
            # Search occupied left
            i = stall-1
            occupied = False
            while(i >= 0 and not occupied):
                if not dist[i][2]:
                    dist[stall][0] = dist[stall][0] +1
                else:
                    occupied = True
                i = i-1

            # Search occupied right
            i = stall+1
            occupied = False
            while (i < n+2 and not occupied):
                if not dist[i][2]:
                    dist[stall][1] = dist[stall][1] + 1
                else:
                    occupied = True

                i = i+1

        # Occupy
        minRL = [(min(x[0],x[1]),max(x[0], x[1]), i) for i,x in enumerate(dist) if not x[2]]

        m1 = max(minRL)

        candidates = [(y,x,z) for x,y,z in minRL if x == m1[0]]

        #selected = max(candidates)
        selected = candidates[0]

        for c in candidates:
            if selected[0] < c[0]:
                selected = c

        #selected = candidates[0]
        dist[selected[2]][2] = True

        dist = [[0, 0, dist[x][2]] for x in range(0, n+2)]

    return selected[0],selected[1]

t = int(input())  # case qty
for case in range(1, t + 1):
    # Single Int: int(input())
    # Many Int: [int(s) for s in input().split(" ")]
    n,k =  [int(s) for s in input().split(" ")]


    solution = solve(case, n,k)

    print("Case #{}:".format(str(case)), " ".join([str(x) for x in solution]))
