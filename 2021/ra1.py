def num_ops(n, k, s):
    return abs(k - sum(s[i] != s[n - i - 1] for i in range(n // 2)))


if __name__ == '__main__':
    for case_no in range(int(input())):
        N, K = map(int, input().strip().split())
        S = input().strip()
        print(f'Case #{case_no + 1}: {num_ops(N, K, S)}')
