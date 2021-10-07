def buy_houses(length, budget, houses):
    houses.sort()
    bought = 0
    for i in range(length):
        if budget >= houses[i]:
            budget -= houses[i]
            bought += 1
    return bought
    

def reader():
    for case_no in range(int(input())):
        n, b = map(int, input().split())
        a = [int(i) for i in input().split()]
        print(f'Case #{case_no + 1}: {buy_houses(n, b, a)}')


if __name__ == '__main__':
    reader()
