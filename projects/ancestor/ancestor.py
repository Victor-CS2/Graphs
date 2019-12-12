from util import Stack, Queue


class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    # build the graph
    graph = Graph()

    for ancestor in ancestors:  # for each pair in ancestors...
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])

        # build the edges in reverse because we want to link the kids to the parents
        graph.add_edges(ancestor[1], ancestor[0])


# BFS because we're looking for the shortest path
    queue = Queue()
    queue.enqueue([starting_node])
    max_path_length = 1  # keeps track of the longest path - tells you when it is completed
    earliest_ancestor = -1  # the last one

    while queue.size() > 0:  # while it isnt empty
        path = queue.dequeue()  # dequeue the path
        vertex = path[-1]  # end of the path

        # the first part catches the lowest numeric value answer
        if (len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            # catching a tie
            earliest_ancestor = vertex
            max_path_length = len(path)

        for neighbor in graph.vertices[vertex]:
            path_copy = path.copy()  # Can also do list(path) to copy the path.
            path_copy.append(neighbor)  # add neighbor to the copied path
            queue.enqueue(path_copy)  # enqueue onto the new path

    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))
