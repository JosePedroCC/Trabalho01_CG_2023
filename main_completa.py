import tkinter as tk
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np

import global_edges
import global_vertices

x = 0
y = 0
z = 0

# Defina a função de rotação 3D
def rotate(vertices, angle_x, angle_y):
    cos_x, sin_x = np.cos(angle_x), np.sin(angle_x)
    cos_y, sin_y = np.cos(angle_y), np.sin(angle_y)
    rotation_x = np.array([[1, 0, 0, 0],
                           [0, cos_x, -sin_x, 0],
                           [0, sin_x, cos_x, 0],
                           [0, 0, 0, 1]])
    rotation_y = np.array([[cos_y, 0, sin_y, 0],
                           [0, 1, 0, 0],
                           [-sin_y, 0, cos_y, 0],
                           [0, 0, 0, 1]])
    rotated_vertices = rotation_y @ rotation_x @ vertices
    return rotated_vertices

# Função para desenhar o cubo
def draw_cube(x, y, z):

    edges = global_edges.edges_cubo
    vertices = np.array(global_vertices.vertices_cubo).transpose()

    mTranslate = np.identity(4)
    mTranslate[0][3] = 2
    mTranslate[1][3] = 0
    mTranslate[2][3] = 0

    vertices = mTranslate @ vertices

    vertices = rotate(vertices, x, y)

    mTranslate[0][3] = -2
    mTranslate[1][3] = 0
    mTranslate[2][3] = 0
    vertices = mTranslate @ vertices

    vertices = vertices.transpose()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            #glColor3f(1.0, 0.0, 0.0) #Para colorir
            glVertex4dv(vertices[vertex])
    glEnd()

#Função para desenhar o cilindro
def draw_cilindro(x, y, z):

    edges = global_edges.edges_cilindro
    vertices = np.array(global_vertices.vertices_cilindro).transpose()

    vertices = rotate(vertices, x, y)

    vertices = vertices.transpose()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            #glColor3f(1.0, 0.0, 0.0) #Para colorir
            glVertex4dv(vertices[vertex])
    glEnd()

# Função para desenhar o objeto sem nome
def draw_objeto(x, y, z):

    edges = global_edges.edges_objeto
    vertices = np.array(global_vertices.vertices_objeto).transpose()

    mTranslate = np.identity(4)
    mTranslate[0][3] = -2
    mTranslate[1][3] = 0
    mTranslate[2][3] = 0

    vertices = mTranslate @ vertices

    vertices = rotate(vertices, x, y)

    mTranslate[0][3] = 2
    mTranslate[1][3] = 0
    mTranslate[2][3] = 0
    vertices = mTranslate @ vertices

    vertices = vertices.transpose()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            #glColor3f(1.0, 0.0, 0.0) #Para colorir
            glVertex4dv(vertices[vertex])
    glEnd()

def atualizar_x(valor):
    global x
    x = float(valor)

def atualizar_y(valor):
    global y
    y = float(valor)

def atualizar_z(valor):
    global z
    z = float(valor)


# ----------------MAIN----------------------------#

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
display = (largura, altura)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Configuração de visualização 3D
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Crie uma janela principal
root = tk.Tk()
root.title("Barra Deslizante")

# Crie a barra deslizante (Scale)
bd = tk.Scale(root, from_=0.0, to=3.0, orient="horizontal", command=atualizar_x, resolution=0.01, length=500, label="X:")
bd.set(0.01)
bd.pack()

# Crie a barra deslizante (Scale)
bd = tk.Scale(root, from_=0.0, to=3.0, orient="horizontal", command=atualizar_y, resolution=0.01, length=500, label="Y:")
bd.set(0.01)
bd.pack()

# Crie a barra deslizante (Scale)
bd = tk.Scale(root, from_=0.0, to=3.0, orient="horizontal", command=atualizar_z, resolution=0.01, length=500, label="Z:")
bd.set(0.01)
bd.pack()

clock = pygame.time.Clock()
# Loop principal
valor2 = 0.01
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    # Limpa a tela
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Desenha o cubo
    draw_cube(x, y, z)
    draw_cilindro(x, y, z)
    draw_objeto(x, y, z)

    # Atualiza a tela do Pygame
    pygame.display.flip()
    root.update()  # Atualiza a interface gráfica do Tkinter

    # Limitador de FPS
    clock.tick(60)