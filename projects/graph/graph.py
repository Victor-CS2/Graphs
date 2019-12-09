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
        self.vertices[vertex] = set()

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
        print(vertex_id)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        create a queue
        create list of visited nodes
        put starting node in the queue
        While: queue not empty
        pop first node out of queue
        if not visited
            mark as visited
            get adjacent edges and add to list
        get to top of loop
        """
        queue = Queue()
        # set() is used to convert any of the iterable to the distinct element and sorted sequenece of iterable elements, commmonly called set.
        visited_nodes = []
        queue.enqueue(starting_vertex)
        while queue.size() > 0:  # while queue isnt empty...
            vertex = queue.dequeue()
            if vertex not in visited_nodes:  # if the vertex has not been visited...
                # add the vertex as a visited node
                visited_nodes.append(vertex)
                # mark the vertex as visited and get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited_nodes = []
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited_nodes:
                visited_nodes.append(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
        print(", ".join(str(i) for i in visited_nodes))

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited_nodes == None:
            visited_nodes = []
        visited_nodes.append(starting_vertex)
        print(starting_vertex)
        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited_nodes:
                self.dft_recursive(next_vert, visited_nodes)
        # printStatement = ", ".join(str(i) for i in visited_nodes)
        # return printStatement

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex is destination_vertex:
                return path
            elif vertex not in visited:
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
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

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


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
