# graph is in adjacent list representation
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }


def bfs(graph, start, search):
    queue = [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == search:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print bfs(graph, '1', '12')