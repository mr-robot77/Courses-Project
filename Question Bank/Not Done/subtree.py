from collections import defaultdict

def count_subtrees(graph, node):
    visited = set()
    result = [0]
    
    def dfs(current, parent):
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor == parent:
                continue
            
            if neighbor not in visited:
                dfs(neighbor, current)
                
            if len(graph[neighbor]) == 1:
                result[0] += 1
                
    dfs(node, None)
    return result[0]

def main():
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    answer = count_subtrees(graph, 1) % (10**9 + 7)
    
    print(answer)

if __name__ == "__main__":
    main()