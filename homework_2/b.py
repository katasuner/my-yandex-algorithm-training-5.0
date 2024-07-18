N, K = map(int, input().split())
prices = [int(price) for price in input().split()]
max_profit = 0

for i in range(N):
    max_price = max(prices[i+1:min(i+1+K, N)], default=0)
    max_profit = max(max_profit, max_price - prices[i])
    
print(max_profit)