def tower_builder(n_floors):
    if type(n_floors) != int:
        return "Must be int."
    the_tower = []
    for i in range(1, n_floors + 1):
        the_tower.append(
            ' ' * (n_floors - i) + '*' * (2 * i - 1) + ' ' * (n_floors - i)
        )
    return the_tower
