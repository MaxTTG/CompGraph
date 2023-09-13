import collections

import numpy as np
import pywavefront

import toolkit
from MyImage import MyImage, Color



class MyModel:
    def __init__(self, file_name: str):
        scene = pywavefront.Wavefront(file_name, create_materials=True, collect_faces=True)
        self.vertices = scene.vertices.copy()
        self.initial_vertices = scene.vertices.copy()
        self.faces = scene.mesh_list[0].faces.copy()

    def vertices(self) -> collections.Iterable:
        return self.vertices

    def faces(self) -> collections.Iterable:
        return self.faces

    def normals(self) -> collections.Iterable:
        vertices = self.vertices
        result = []
        for face in self.faces:
            dot_1_index = face[0]
            dot_2_index = face[1]
            dot_3_index = face[2]
            normal = toolkit.normal(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_1_index][2],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            vertices[dot_2_index][2],
                            vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            vertices[dot_3_index][2])
            result.append(normal)
        return result

    def bend(self, ax, ay, u0, v0, t0):
        initial_vertices = np.copy(self.vertices)

        for i in range(len(self.initial_vertices)):
            ver = initial_vertices[i]
            x = ver[0]
            y = ver[1]
            z = ver[2]
            res = np.array([[ax, 0, u0],
                            [0, ay, v0],
                            [0, 0, 1]]).dot(
                np.array([x, y, z + t0]))
            self.vertices[i] = (res[0], res[1], z)

    def rotate(self, alpha, betta, gamma):
        initial_vertices = np.copy(self.vertices)

        R1 = np.array([[1, 0, 0],
                       [0, np.cos(alpha), np.sin(alpha)],
                       [0, -np.sin(alpha), np.cos(alpha)]])
        R2 = np.array([[np.cos(betta), 0, np.sin(betta)],
                       [0, 1, 0],
                       [-np.sin(betta), 0, np.cos(betta)]])
        R3 = np.array([[np.cos(gamma), np.sin(gamma), 0],
                       [-np.sin(gamma), np.cos(gamma), 0],
                       [0, 0, 1]])
        R = np.dot(R1, np.dot(R2, R3))

        for i in range(len(initial_vertices)):
            self.vertices[i] = np.dot(R, initial_vertices[i])

    def draw_faces(self, image: MyImage, color: Color, magnification=1):
        vertices = self.vertices
        for face in self.faces:
            dot_1_index = face[0]
            dot_2_index = face[1]
            dot_3_index = face[2]
            image.draw_line(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            color,
                            magnification=magnification)
            image.draw_line(vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            color,
                            magnification=magnification)
            image.draw_line(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            color,
                            magnification=magnification)

    def draw_trianlges(self, image: MyImage, step=0.3, color=None, magnification=1):
        vertices = self.vertices
        faces = self.faces
        normals = self.normals()
        for i in range(len(faces)):
            face = faces[i]
            normal = normals[i]
            cos = toolkit.find_cos(normal)
            if cos > 0:
                dot_1_index = face[0]
                dot_2_index = face[1]
                dot_3_index = face[2]
                image.draw_triangle(x0=vertices[dot_1_index][0],
                                    y0=vertices[dot_1_index][1],
                                    x1=vertices[dot_2_index][0],
                                    y1=vertices[dot_2_index][1],
                                    x2=vertices[dot_3_index][0],
                                    y2=vertices[dot_3_index][1],
                                    z0=vertices[dot_1_index][2],
                                    z1=vertices[dot_2_index][2],
                                    z2=vertices[dot_3_index][2],
                                    step=step,
                                    color=Color(255 * cos, 0, 0) if color is None else color,
                                    magnification=magnification,
                                    cos=cos)
