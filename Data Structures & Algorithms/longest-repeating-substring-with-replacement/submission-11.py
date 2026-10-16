class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        res = 0
        ch = [0] * 26
        # a = -1
        while j < len(s):
            
            idx = ord(s[j]) - ord("A")
            ch[idx] += 1
            # a = j
            # print("start")
            # print(ch)
            most_freq = max(ch)
            l = j - i + 1
            # print(f"s: {s[i: j + 1]}")
            # print(f"i: {i}, j: {j}, l: {l}")
            # print(f"most_freq: {most_freq}")
            if l - most_freq <= k:
                # print("valid window")
                res = max(res, l)
                # print(f"res: {res}")
            else:
                ch[ord(s[i]) - ord("A")] -= 1
                i += 1
            j += 1
        return res
