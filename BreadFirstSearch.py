# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int startNode)
# traverses vertices reachable from startNode.
from collections import defaultdict
from pprint import pprint

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, startNode):
        # Create a list to store the visited vertices
        visited = []
        # Create a queue for BFS
        queue = []

        # Check if the list contain the start node. If not, Add the source node to the visited list
        if visited.__contains__(startNode) == False:
            visited.append(startNode)

        #enqueue the start node
        queue.append(startNode)
        
        #while the quene contains some items
        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.pop(0)
            print(currentNode, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. 
            # If a adjacent has not been visited, then mark it visited and enqueue it
            
            for i in self.graph[currentNode]:
                if visited.__contains__(i) == False:
                    queue.append(i)
                    visited.append(i)

# Driver code
# Create a graph corresponding to the given graph

g = Graph()
g.addEdge('Start', 'A')
g.addEdge('Start', 'B')
g.addEdge('Start', 'D')
g.addEdge('A', 'Start')
g.addEdge('A', 'C')
g.addEdge('B', 'Start')
g.addEdge('B', 'D')
g.addEdge('C', 'A')
g.addEdge('C', 'D')
g.addEdge('C', 'Goal')
g.addEdge('D', 'Start')
g.addEdge('D', 'B')
g.addEdge('D', 'C')
g.addEdge('D', 'Goal')

print("states Expanded") 
g.BFS('Start')