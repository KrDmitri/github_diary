def fittingTile():
    n = int(input())

    d = [0] * 10000
    d[0] = 1
    d[1] = 1
    for i in range(2, 10000):
        d[i] = d[i - 1] + d[i - 2] * 2

    print(d[n])

def combianteMoney():
    n, m = map(int, input().split())
    moneys = []
    for i in range(n):
        moneys.append(int(input()))
    moneys.sort()
    d = [999] * 1000
    d[0] = 0
    leastMoney = moneys[0]

    for i in range(1, 1000):
        # 애초에 나타낼 수 없는 돈은 -999로
        if i < leastMoney:
            d[i] = -999
        # 가장 작은 단위보다 큰 수부터
        else:
            # 나누어 떨어지는 경우
            for money in moneys:
                if i >= money and i % money == 0:
                    temp = i // money
                    d[i] = min(d[i], temp)

            # 조합하는 경우
            for bigMoney in range(i-1, 0, -1):
                if d[bigMoney] > 0 and d[i - bigMoney] > 0:
                    temp = d[bigMoney] + d[i - bigMoney]
                    d[i] = min(d[i], temp)

    if d[i] > 0:
        print(d[m])
    else:
        print(-1)

def combinateMoney2():
    n, m = map(int, input().split())
    array = []
    for i in range(n):
        array.append(int(input()))

    d = [10001] * (m + 1)
    d[0] = 0

    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array] + 1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])


### test code ###
combianteMoney()
