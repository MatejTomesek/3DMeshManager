import os

class Mesh:
    def __init__(self, name: str, vertices: int = 0, faces: int = 0):
        self.name = name
        self.vertices = vertices
        self.faces = faces

class OBJLoader:
    def load(filepath: str) -> Mesh:
        vertices = 0
        faces = 0
        name = os.path.basename(filepath)

        with open(filepath, "r") as f:
            for line in f:
                if line.startswith("v "):  # vertex line
                    vertices += 1
                elif line.startswith("f "):  # face line
                    faces += 1

        return Mesh(name=name, vertices=vertices, faces=faces)

class MeshLibrary:
    def __init__(self):
        self.meshes = []

    def load_from_directory(self, directory: str):
        for filename in os.listdir(directory):
            if filename.endswith(".obj"):
                filepath = os.path.join(directory, filename)
                mesh = OBJLoader.load(filepath)
                self.meshes.append(mesh)
            else:
                pass
                print(f" - {filename} is not a .obj file. Please convert to .obj and try again.")

    def summary(self):
        print("Mesh Library Summary")
        for mesh in self.meshes:
            print(f" - {mesh.name}: {mesh.vertices} vertices and {mesh.faces} faces")


if __name__ == "__main__":
    library = MeshLibrary()

    library.load_from_directory("meshes")
    library.summary()



# dodat exception try-except a errory pokud soubor obj nebude citelny napriklad - asi do samostatneho folderu??
# dovolit jako variantu?? uzivatlsky vstup = directory s meshema a to osetrit podminkami v samostatnem souboru?


