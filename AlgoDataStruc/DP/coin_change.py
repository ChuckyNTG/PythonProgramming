
l1 = map(int,raw_input().split(" "))
s = l1[0]
size = l1[1]
coins = map(int,raw_input().split(" "))

dp_arr = [1] + [0] * s

for i in range(s+1):
    for j in range(len(coins)):
        try:
            dp_arr[i] += dp_arr[i - coins[j]]
        except IndexError:
            pass

print dp_arr

