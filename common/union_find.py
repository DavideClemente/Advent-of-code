class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}  # Each item is its own parent
        self.size = {item: 1 for item in items}       # Each starts with size 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Merge smaller into larger
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True
    
    def get_component_sizes(self):
        roots = {}
        for item in self.parent:
            root = self.find(item)
            if root not in roots:
                roots[root] = self.size[root]
        return list(roots.values())