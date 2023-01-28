def find_next_possible_positions(maze, position1, position2, visited_positions):
    return 0, 0


def breadth_first_search(maze, value_to_find):
    if maze:
        queue = [(0, 0)]
        visited_positions = []
        while queue:
            position1, position2 = queue.pop(0)

            # se é o nó esperado
            if maze[position1][position2] == value_to_find:
                return True

            # importante guardar para nao analisar caminhos ja visitados
            visited_positions.append((position1, position2))

            queue += find_next_possible_positions(maze,
                                                  position1, position2, visited_positions)
