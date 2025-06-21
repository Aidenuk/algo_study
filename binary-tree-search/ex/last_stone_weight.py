def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort() 
        last = stones.pop()   
        second_last = stones.pop() 
        if last != second_last:
            stones.append(last - second_last)  

    return stones[0] if stones else 0
