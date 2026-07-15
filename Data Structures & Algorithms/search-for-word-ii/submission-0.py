class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res_words = []
        
        for word in words:
            self.insert(word)
        
        def backtrack(i, j, node):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            
            ch = board[i][j]
            if ch == "#" or ch not in node.children:
                return 
            
            board[i][j] = "#"
            next_node = node.children[ch]
            if next_node.word:
                res_words.append(next_node.word)
                next_node.word = None
                
             
            backtrack(i - 1, j, next_node) 
            backtrack(i + 1, j, next_node) 
            backtrack(i, j - 1, next_node)
            backtrack(i, j + 1, next_node)
            
            board[i][j] = ch
        
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, self.root)
        
        return res_words
        