# leetcode = 190

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')
        split_it = list(binary)
        split_it.reverse()
        join_it = "".join(split_it)
        reversed_n = int(join_it, 2)
        return reversed_n
        

