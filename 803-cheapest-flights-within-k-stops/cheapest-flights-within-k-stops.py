class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0

        for i in range(k + 1):
            copyPrice = price.copy()
            for f, t, p in flights:
                if price[f] == float('inf'):
                    continue
                
                if price[f] + p < copyPrice[t]:
                    copyPrice[t] = price[f] + p
            price = copyPrice
        
        return price[dst] if price[dst] != float('inf') else -1