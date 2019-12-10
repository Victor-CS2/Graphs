"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        # set() is used to convert any of the iterable to the distinct element and sorted sequenece of iterable elements, commmonly called set.
        queue.enqueue(starting_vertex)
        visited_nodes = set()
        while queue.size() > 0:  # while queue isnt empty...
            vertex = queue.dequeue()  # vertex gets dequeued
            if vertex not in visited_nodes:  # if the vertex has not been visited...
                # add the vertex as a visited node
                # print(vertex)
                visited_nodes.add(vertex)
                # mark the vertex as visited and get adjacent edges and add to list
                for next_vert in self.get_neighbors(vertex):
                    queue.enqueue(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create a Set to store visited vertices
        visited_nodes = set()
        # While the stack is not empty...
        while stack.size() > 0:
            # Pop the first vertex
            vertex = stack.pop()
            # If that vertex has not been visited...
            if vertex not in visited_nodes:
                # Mark it as visited...
                # print(vertex)
                visited_nodes.add(vertex)
                # Then add all of its neighbors to the top of the stack
                for next_vert in self.get_neighbors(vertex):
                    stack.push(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft_recursive(self, starting_vertex, visited_nodes=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if visited has been initialized
        if visited_nodes is None:
            # if not, initialize into an empty set
            visited_nodes = set()
        # Mark the node as visited
        print(starting_vertex)
        visited_nodes.add(starting_vertex)
        # Call DFT recursive on each neighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited_nodes:
                self.dft_recursive(neighbor, visited_nodes)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A Path to the starting vertex id
        queue = Queue()
        # we do ([starting_vertex]) to store the path
        queue.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited_nodes = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first path
            path = queue.dequeue()
            # Grab the last vertex from the path
            vertex = path[-1]
            # If that vertex is the destination vertex, return the path
            if vertex is destination_vertex:
                return path
            # Else if the vertex has not been visited...
            elif vertex not in visited_nodes:
                # add that vertex into the visited nodes
                visited_nodes.add(vertex)
                # and create a new path
                for next_vert in self.get_neighbors(vertex):
                    # copy the path
                    new_path = path.copy()
                    # append the neighbor to the back
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        # Inside a list in order to grab the last item later in the function (line 122)
        stack.push([starting_vertex])
        visited = set()  # using set to not have duplicates in visited
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex is destination_vertex:
                return path
            elif vertex not in visited:
                visited.add(vertex)  # vertex gets added to the visited
                # for the next one our vertex points to...
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)  # create a new test path
                    # add our next vert to our test path
                    new_path.append(next_vert)
                    stack.push(new_path)  # push the path into the stack

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Init path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at the target value, return the path
        if starting_vertex == target_vertex:
            return path
        # Otherwise, call DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(
                    neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
