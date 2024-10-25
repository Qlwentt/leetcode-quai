
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_folder(self, folder):
        current = self.root
        words = [word for word in folder.split("/") if word != ""]
        for word in words:
            if word not in current.children:
                current.children[word] = TrieNode()
            current = current.children[word]
        current.end = True
    
    def get_base_folders(self):
        bases = []
        def dfs(current, cur_folders):
            if current.end:
                bases.append("/"+"/".join(cur_folders))
                return
            for child in current.children:
                cur_folders.append(child)
                dfs(current.children[child],cur_folders)
                cur_folders.pop()
        dfs(self.root, [])
        return bases
        
                
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add_folder(f)
        return trie.get_base_folders()
        
        