class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        in_degree = {c: 0 for word in words for c in word}
        adj = defaultdict(set)
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        in_degree[w2[j]] += 1
                        adj[w1[j]].add(w2[j])
                    break
        
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        order = []
        
        while queue:
            c = queue.popleft()
            order.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -=  1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) != len(in_degree):
            return ""
            
        return "".join(order)
        