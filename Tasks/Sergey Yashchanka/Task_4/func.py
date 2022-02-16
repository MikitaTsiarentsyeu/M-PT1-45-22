def add_gaps(w, l):
    """add gaps in the string"""
    for _ in range(w):
        for i_d, symbol in enumerate(l):
            if len("".join(l).rstrip()) == w:
                break
            if symbol != " ":
                l.insert(i_d + 1, " ")


def write_file(file, l):
    """writes any string to any file"""
    file.write("".join(l) + "\n")