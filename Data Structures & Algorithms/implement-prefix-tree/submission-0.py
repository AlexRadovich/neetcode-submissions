class Node:

    def __init__(self):
        self.next = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char in cur.next:
                cur = cur.next[char]
            else:
                cur.next[char] = Node()
                cur = cur.next[char]

        
        cur.end = True



    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char in cur.next:
                cur = cur.next[char]
            else:
                return False

        return cur.end

        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for char in prefix:
            if char in cur.next:
                cur = cur.next[char]
            else:
                return False

        return True
        
        