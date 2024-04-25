from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    distances = {vertex: float('inf') for vertex in graph}
    num_edges = {vertex: float('inf') for vertex in graph}
    parents = {vertex: None for vertex in graph}
    
    distances[source] = 0
    num_edges[source] = 0
    
    queue = deque([source])
    
    while queue:
        current_vertex = queue.popleft()
        for neighbor, weight in graph[current_vertex]:
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor] or (new_distance == distances[neighbor] and num_edges[current_vertex] + 1 < num_edges[neighbor]):
                distances[neighbor] = new_distance
                num_edges[neighbor] = num_edges[current_vertex] + 1
                parents[neighbor] = current_vertex
                queue.append(neighbor)
    
    shortest_paths = {vertex: (distances[vertex], num_edges[vertex]) for vertex in graph}
    return shortest_paths
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {source: None}
    queue = deque([source])
    
    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex]:
            if neighbor not in parents:
                parents[neighbor] = current_vertex
                queue.append(neighbor)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current_vertex = destination
    
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parents[current_vertex]
    
    path.pop()
    path.reverse()
    return ' -> '.join(path)
