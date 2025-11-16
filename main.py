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

        try:
            with open(filepath, "r") as f:
                for line in f:
                    if line.startswith("v "):  # vertex line
                        vertices += 1
                    elif line.startswith("f "):  # face line
                        faces += 1
        except Exception as e:
            print(f"[ERROR] Failed to read OBJ file: {filepath}")

        return Mesh(name=name, vertices=vertices, faces=faces)

class MeshLibrary:
    def __init__(self):
        self.meshes = []

    def load_from_directory(self, directory: str):
        try:
            files = os.listdir(directory)
        except FileNotFoundError:
            print(f"[ERROR] Directory not found: {directory}")
        except PermissionError:
            print(f"[ERROR] Permission denied: {directory}")

        for filename in os.listdir(directory):
            if filename.endswith(".obj"):
                filepath = os.path.join(directory, filename)
                mesh = OBJLoader.load(filepath)
                self.meshes.append(mesh)
            else:
                pass
                print(f" - {filename} is not a .obj file. Please convert to .obj and try again.")

    def summary(self):
        text = ["Mesh Library Summary"]

        print("Mesh Library Summary")
        for mesh in self.meshes:

            print(f" - {mesh.name}: {mesh.vertices} vertices and {mesh.faces} faces")
            text.append(f" - {mesh.name}: {mesh.vertices} vertices and {mesh.faces} faces")


        with open("mesh_data.txt", "w") as f:
            f.write("\n".join(text))
        print(f"Data of {len(self.meshes)} meshes were saved to mesh_data.txt")

if __name__ == "__main__":
    directory = input("Enter directory path containing .obj files: ")
    directory = os.path.abspath(directory)

    library = MeshLibrary()
    library.load_from_directory(directory)
    library.summary()


