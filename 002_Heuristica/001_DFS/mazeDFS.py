def find_next_position(position, visited_positions):
    return 0, 0


def item_value(position):
    return maze[position[0]][position[1]]


def deep_first_search(position, visited_positions, value_to_find):
    if item_value(position) == value_to_find:
        return True

    next_position = find_next_position(position, visited_positions)
    if next_position:
        return deep_first_search(next_position, visited_positions + [position], value_to_find)
