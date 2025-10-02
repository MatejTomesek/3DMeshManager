import os
import pytest
from main import Mesh, OBJLoader, MeshLibrary

# Helper - create virtual temporary file for testing

def create_obj_file(path, content: str):
    file_path = path / "test.obj"
    file_path.write_text(content)
    return str(file_path)

# Tests

# Try to count faces and vertices inside simple obj text block
def test_objloader_counts_correctly(tmp_path):
    obj_file = create_obj_file(
        tmp_path,
        "v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n"
    )
    mesh = OBJLoader.load(obj_file)
    assert mesh.vertices == 3
    assert mesh.faces == 1

# Try to load empty obj file
def test_objloader_empty_file(tmp_path):
    obj_file = create_obj_file(tmp_path, "")
    mesh = OBJLoader.load(obj_file)
    assert mesh.vertices == 0
    assert mesh.faces == 0

# Try to interact with empty library wihtout meshes
def test_library_initializes_empty():
    lib = MeshLibrary()
    assert lib.meshes == []

# Test if program writes summary of meshes correctly
def test_summary_writes_file(tmp_path):
    obj_file = create_obj_file(tmp_path, "v 0 0 0\nf 1 1 1\n")
    lib = MeshLibrary()
    lib.load_from_directory(str(tmp_path))
    os.chdir(tmp_path)  # so it writes mesh_data.txt here
    lib.summary()

    output_file = tmp_path / "mesh_data.txt"
    assert output_file.exists()
    content = output_file.read_text()
    assert "Mesh Library Summary" in content
    assert "test.obj: 1 vertices and 1 faces" in content