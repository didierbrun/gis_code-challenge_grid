def resolve(x, y, w, h):
    s = min(w - 1, h - 1)               # Size of corner
    n = x + y                           # Diagonal index
    m = w + h - 2 - n                   # Reverse diagonal index
    ny = h - 1 - y                      # Reverse y
    sh = ny if w > h else x             # Shift direction
    t = lambda i: i * (i + 1) // 2      # Triangle number t(n)=(n.n+1)/2

    # Upper-left corner
    if n < s:
        return t(n) + x
    # Bottom-right corner
    elif m < s:
        return w * h - t(m + 1) + ny
    # Anything else
    else:
        return t(s) + (n - s) * (s + 1) + sh