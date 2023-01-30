import open3d as o3d
import numpy as np
triangular_mesh = o3d.io.read_triangle_mesh("FC.STL")
triangular_mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([triangular_mesh])