import sys

from maze import Maze, path_from, Node


def l1(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y-node2.y)


def a_star(maze):
    start_node = maze.find_node('S')
    end_node = maze.find_node('E')
    start_node.cost = 0;
    start_node.priority = 0;
    q = [start_node]

    while len(q) > 0:
        q.sort(key=lambda x: x.priority)
        e = q.pop(0)
        e.visited = True
        if e.type == 'E':
            return path_from(e)

        children = maze.get_possible_movements(e)
        for d in children:
            nowy_koszt = maze.move_cost(e, d) + e.cost
            if nowy_koszt < d.cost:
                d.cost = nowy_koszt
                d.parent = e
                d.priority = nowy_koszt + l1(end_node, d)
                q.append(d)




maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = a_star(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()