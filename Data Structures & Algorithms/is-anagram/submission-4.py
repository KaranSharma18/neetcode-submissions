class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        alp = "abcdefghijklmnopqrstuvwxyz"
        arr = [0] * 26
        
        for ch1, ch2 in zip(s, t):
            arr[alp.index(ch1)] += 1
            arr[alp.index(ch2)] -= 1
        
        for elem in arr:
            if elem != 0:
                return False
        return True