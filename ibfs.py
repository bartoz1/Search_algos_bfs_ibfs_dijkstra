import sys

from maze import Maze, path_from

def l1(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y-node2.y)


def ibfs(maze):
    start_node = maze.find_node('S')
    q = [start_node]
    E = maze.find_node('E')

    while len(q) > 0:
        q.sort(key=lambda x: x.priority)
        node = q.pop(0)  # FIFO
        node.visited = True

        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                child.priority = l1(E, child)
                q.append(child)

    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = ibfs(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()