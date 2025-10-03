
# WIP

import trimesh
import pyrender
import matplotlib.pyplot as plt
import numpy as np

# Load the OBJ mesh
mesh_trimesh = trimesh.load("humanoid.obj")

# Convert to pyrender mesh
mesh = pyrender.Mesh.from_trimesh(mesh_trimesh)

# Create scene and add mesh
scene = pyrender.Scene()
scene.add(mesh)

# Add camera
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
cam_node = scene.add(camera, pose=np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, -0.5],
    [0.0, 0.0, 1.0, 2.0],
    [0.0, 0.0, 0.0, 1.0]
]))

# Add a light so the mesh is visible
light = pyrender.DirectionalLight(color=np.ones(3), intensity=3.0)
scene.add(light, pose=cam_node.matrix)

# Render offscreen
r = pyrender.OffscreenRenderer(640, 480)
color, depth = r.render(scene)

# Display
plt.imshow(color)
plt.axis('off')
plt.show()