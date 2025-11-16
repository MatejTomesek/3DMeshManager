import os

class Mesh:
    def __init__(self, name: str):
        self.name = name
        self.vertices = 0
        self.faces = 0

        self.min_x = float("inf")
        self.min_y = float("inf")
        self.min_z = float("inf")
        self.max_x = float("-inf")
        self.max_y = float("-inf")
        self.max_z = float("-inf")

    def update_bounds(self, x, y, z):
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        self.min_z = min(self.min_z, z)

        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)
        self.max_z = max(self.max_z, z)

    @property
    def width(self):
        return self.max_x - self.min_x
    @property
    def height(self):
        return self.max_y - self.min_y
    @property
    def depth(self):
        return self.max_z - self.min_z


class OBJLoader:
    def load(filepath: str) -> Mesh:
        name = os.path.basename(filepath)
        mesh = Mesh(name)

        try:
            with open(filepath, "r") as f:
                for line in f:
                    if line.startswith("v "):  # vertex line
                        mesh.vertices += 1
                        parts = line.strip().split()
                        try:
                            x = float(parts[1])
                            y = float(parts[2])
                            z = float(parts[3])
                            mesh.update_bounds(x, y, z)
                        except:
                            pass
                    elif line.startswith("f "):  # face line
                        mesh.faces += 1

        except Exception as e:
            print(f"[ERROR] Failed to read OBJ file: {filepath}")

        return mesh

class MeshLibrary:
    def __init__(self):
        self.meshes = []

    def load_from_directory(self, directory: str):
        try:
            files = os.listdir(directory)
        except FileNotFoundError:
            print(f"[ERROR] Directory not found: {directory}")
            return
        except PermissionError:
            print(f"[ERROR] Permission denied: {directory}")
            return

        for filename in os.listdir(directory):
            if filename.endswith(".obj"):
                filepath = os.path.join(directory, filename)
                mesh = OBJLoader.load(filepath)
                self.meshes.append(mesh)
            else:
                print(f" - {filename} is not a .obj file. Please convert to .obj and try again.")

    def summary(self):
        text = ["Mesh Library Summary"]

        print("Mesh Library Summary")
        for mesh in self.meshes:

            mesh.width_cm = mesh.width * 100
            mesh.height_cm = mesh.height * 100
            mesh.depth_cm = mesh.depth * 100

            print(f" - {mesh.name}: {mesh.vertices} vertices and {mesh.faces} faces")
            print(f"   Dimensions (cm) of {mesh.name}: {mesh.width_cm:.0f}×{mesh.height_cm:.0f}×{mesh.depth_cm:.0f}")

            text.append(f" - {mesh.name}: {mesh.vertices} vertices and {mesh.faces} faces")
            text.append(
                f" - Dimensions (cm): {mesh.width_cm:.0f}x{mesh.height_cm:.0f}x{mesh.depth_cm:.0f}\n"
            )


        with open("mesh_data.txt", "w") as f:
            f.write("\n".join(text))
        print(f"Data of {len(self.meshes)} meshes were saved to mesh_data.txt")

if __name__ == "__main__":
    directory = input("Enter directory path containing .obj files: ")
    directory = os.path.abspath(directory)

    library = MeshLibrary()
    library.load_from_directory(directory)
    library.summary()


