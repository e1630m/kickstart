def update(m, h, w, fr):
    updated = []
    for r in range(h):
        line, limit = [], 0
        for c in range(w):
            c = -1 - c if fr in 'rd' else c
            limit = max(limit, m[r][c]) if fr in 'lr' else max(limit, m[c][r])
            line.append(limit)
            limit -= 1
        if fr in 'rd':
            line.reverse()
        updated.append(line)
    return updated


def four_ways(m, h, w):
    left, right = update(m, h, w, 'l'), update(m, h, w, 'r')
    up, down = update(m, w, h, 'u'), update(m, w, h, 'd')
    return [[max(left[r][c], right[r][c], up[c][r], down[c][r])
             for c in range(w)] for r in range(h)]


def counter(m, h, w):
    copy = four_ways([[i for i in line] for line in m], h, w)
    copy = four_ways(copy, h, w)
    boxes = 0
    for r in range(h):
        for c in range(w):
            boxes += copy[r][c] - m[r][c]
    return boxes


def reader():
    for case_no in range(int(input())):
        r, c = map(int, input().strip('\n').split())
        g = [[int(n) for n in input().strip('\n').split()] for _ in range(r)]
        print(f'Case #{case_no + 1}: {counter(g, r, c)}')


if __name__ == '__main__':
    reader()
