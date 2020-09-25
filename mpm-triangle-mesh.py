# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:56:32 2020

@author: Артур
"""

from sympy import true, false

# Для заданной треугольной сетки определяет,
# в какой треугольник попала точка

# Узлы сетки
Mx = [0, 1, 2, 0, 1, 2]
My = [0, 0, 0, 2, 2, 2]

# Треугольники сетки
# (каждый задается номерами вершин)
T = [[0, 3, 4], [0, 1, 4], [1, 2, 5], [1, 4, 5]]


# Функция - критерий принадлежности точки треуг-ку
# Треугольный элемент сетки (т.е. треугольник АВС)
# и барицентрические координаты в качестве N1, N2, N3
def Belongs(xa, ya, xb, yb, xc, yc, xp, yp):
    # Матрица коэффициентов
    a11 = xa - xc
    a12 = xb - xc
    a21 = ya - yc
    a22 = yb - yc

    # Находим обратную к ней
    det = a11 * a22 - a12 * a21
    b11 = a22 / det
    b12 = -a12 / det
    b21 = -a21 / det
    b22 = a11 / det

    # Находим барицентрич.координаты точки P
    N1 = b11 * (xp - xc) + b12 * (yp - yc)
    N2 = b21 * (xp - xc) + b22 * (yp - yc)
    N3 = 1 - N1 - N2

    if (N1 >= 0) & (N2 >= 0) & (N3 >= 0):
        return true
    else:
        return false


# координаты интересующей нас точки Р
xp = 0.5
yp = 1

# print(Belongs(xa,ya,xb,yb,xc,yc,xp,yp))

for n in range(0, 4):
    # Определяем координаты вершин n-го треугольника
    T1 = T[n]
    print('Треугольник №', n, 'имеет вершины с номерами:')  # Массив из номеров вершин 1-го тр-ка
    i = T1[0]
    j = T1[1]
    k = T1[2]
    print(i, j, k)
    print('Координаты этих вершин:')
    print('x:', Mx[i], Mx[j], Mx[k])
    print('y:', My[i], My[j], My[k])
    xa = Mx[i]  # координаты точки А
    ya = My[i]

    xb = Mx[j]  # координаты точки В
    yb = My[j]

    xc = Mx[k]  # координаты точки С
    yc = My[k]

    print('Верно ли, что точка Р(', xp, ',', yp, ') принадлежит данному треугольнику? -->',
          Belongs(xa, ya, xb, yb, xc, yc, xp, yp))
    print('========================')
