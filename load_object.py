def load_object(filepath):
    vertices, faces = 0, 0
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith("v "):      # vertex line
                vertices += 1
            elif line.startswith("f "):    # face line
                faces += 1
    return vertices, faces



