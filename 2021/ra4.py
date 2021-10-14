def checksum(n, a, cost, rc, cc):
    tc, nodes = 0, set()
    neigh = [[0] * (2 * n) for _ in range(2 * n)]
    for r in range(n):
        for c in range(n):
            if a[r][c] == -1:
                neigh[r][c + n] = neigh[c + n][r] = cost[r][c]
                nodes.add(r)
                nodes.add(c + n)
                tc += cost[r][c]
    ln = len(nodes)
    nodes, maxi, checked = list(nodes), [0] * ln, [False] * ln
    for _ in range(ln):
        target = -1
        for i in range(ln):
            if checked[i]:
                continue
            if target == -1 or maxi[i] > maxi[target]:
                target = i
        checked[target] = True
        tc -= maxi[target]
        for i in range(ln):
            if neigh[nodes[target]][nodes[i]] > maxi[i]:
                maxi[i] = neigh[nodes[target]][nodes[i]]
    return tc


def reader():
    for case_no in range(int(input())):
        n = int(input())
        a = [[int(i) for i in input().split()] for _ in range(n)]
        b = [[int(i) for i in input().split()] for _ in range(n)]
        r = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        print(f'Case #{case_no + 1}: {checksum(n, a, b, r, c)}')


if __name__ == '__main__':
    reader()
