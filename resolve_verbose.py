def resolve(x, y, width, height):
    sise_of_corner = min(width - 1, height - 1)                 # Size of corner
    diagonal_index = x + y                                      # Diagonal index
    inv_diagonal_index = width + height - 2 - diagonal_index    # Reverse diagonal index
    inv_y = height - 1 - y                                      # Reverse y
    shift = inv_y if width > height else x                      # Shift direction
    triangle_sum = lambda base: base * (base + 1) // 2          # Triangle number t(n)=(n.n+1)/2

    # Upper-left corner
    if diagonal_index < sise_of_corner:
        return triangle_sum(diagonal_index) + x + 1
    # Bottom-right corner
    elif inv_diagonal_index < sise_of_corner:
        return width * height - triangle_sum(inv_diagonal_index + 1) + inv_y + 1
    # Anything else
    else:
        return triangle_sum(sise_of_corner) + (diagonal_index - sise_of_corner) * (sise_of_corner + 1) + shift + 1