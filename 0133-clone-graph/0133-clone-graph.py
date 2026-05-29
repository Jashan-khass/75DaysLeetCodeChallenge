from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]

def build_graph(adjList):
    if not adjList:
        return None

    nodes = [Node(i + 1) for i in range(len(adjList))]

    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]

    return nodes[0]

def graph_to_adjlist(node):
    if not node:
        return []

    visited = {}
    queue = deque([node])

    while queue:
        current = queue.popleft()

        if current.val in visited:
            continue

        visited[current.val] = sorted([n.val for n in current.neighbors])

        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)

    return [visited[i] for i in range(1, len(visited) + 1)]

adjList1 = [[2,4],[1,3],[2,4],[1,3]]
graph1 = build_graph(adjList1)
cloned1 = Solution().cloneGraph(graph1)
print(graph_to_adjlist(cloned1))

adjList2 = [[]]
graph2 = build_graph(adjList2)
cloned2 = Solution().cloneGraph(graph2)
print(graph_to_adjlist(cloned2))

adjList3 = []
graph3 = build_graph(adjList3)
cloned3 = Solution().cloneGraph(graph3)
print(graph_to_adjlist(cloned3))