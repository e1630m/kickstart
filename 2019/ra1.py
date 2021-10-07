def coach(len_s, pick, skills, ans=float('inf')):
    s = sorted(skills, reverse=True)
    h, p = sum(s[0] - skill for skill in s[1:pick]), pick - 1
    for i in range(1, len_s - p):
        ans = min(ans, h)
        h += s[i] - s[i + p] - p * (s[i - 1] - s[i])
    return min(ans, h)


def reader():
    for case_no in range(int(input())):
        n, p = map(int, input().split())
        s = [int(i) for i in input().split()]
        print(f'Case #{case_no + 1}: {coach(n, p, s)}')


if __name__ == '__main__':
    reader()
