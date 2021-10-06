def count(g):
    h, w = len(g), len(g[0])
    d, u = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]
    r, l = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            d[i][j] = (g[i][j] + d[i - 1][j] if g[i][j] else 0) if i else g[i][j]
            r[i][j] = (g[i][j] + r[i][j - 1] if g[i][j] else 0) if j else g[i][j]
            u[-1 - i][j] = (g[-1 - i][j] + u[-i][j] if g[-1 - i][j] else 0) if i else g[-1 - i][j]
            l[i][-1 - j] = (g[i][-1 - j] + l[i][-j] if g[i][-1 - j] else 0) if j else g[i][-1 - j]
    result = 0
    for i in range(h):
        for j in range(w):
            result += max(0, min(d[i][j], r[i][j] // 2) + min(d[i][j] // 2, r[i][j]) - 2)
            result += max(0, min(d[i][j], l[i][j] // 2) + min(d[i][j] // 2, l[i][j]) - 2)
            result += max(0, min(u[i][j], r[i][j] // 2) + min(u[i][j] // 2, r[i][j]) - 2)
            result += max(0, min(u[i][j], l[i][j] // 2) + min(u[i][j] // 2, l[i][j]) - 2)
    return result


def reader():
    for case_no in range(int(input())):
        r, c = map(int, input().strip('\n').split())
        grid = [[int(n) for n in input().strip('\n').split()] for _ in range(r)]
        print(f'Case #{case_no + 1}: {count(grid)}')


if __name__ == '__main__':
    reader()
