def naive(m, h, w):
    heights, highest, boxes = {}, 0, 0
    for r in range(h):
        for c in range(w):
            highest = max(highest, m[r][c])
            heights[m[r][c]] = heights.get(m[r][c], []) + [(r, c)]
    queue = sorted(list(heights.keys()))[::-1]
    while queue:
        height = queue.pop(0)
        new_heights = []
        while heights[height]:
            r, c = heights[height].pop(0)
            nh = height - 1
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < h and 0 <= nc < w and m[nr][nc] < nh):
                    continue
                heights[m[nr][nc]].remove((nr, nc))
                boxes += nh - m[nr][nc]
                m[nr][nc] = nh
                heights[nh] = heights.get(nh, []) + [(nr, nc)]
                if len(heights[nh]) == 1:
                    new_heights.append(nh)
        if new_heights:
            queue += new_heights
            queue.sort(reverse=True)
    return boxes


def reader():
    for case_no in range(int(input())):
        r, c = map(int, input().strip('\n').split())
        grid = [[int(n) for n in input().strip('\n').split()] for _ in range(r)]
        print(f'Case #{case_no + 1}: {naive(grid, r, c)}')


if __name__ == '__main__':
    reader()
