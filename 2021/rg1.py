def num_ops(n, d, c, m, s):
    for animal in s:
        if animal == 'D':
            if not d or c < 0:
                return 'NO'
            d, c = d - 1, c + m
        else:
            c -= 1
    return 'YES'


def reader():
    for case_no in range(int(input())):
        n, d, c, m = map(int, input().strip().split())
        s = input().strip()
        print(f'Case #{case_no + 1}: {num_ops(n, d, c, m, s)}')


if __name__ == '__main__':
    reader()
