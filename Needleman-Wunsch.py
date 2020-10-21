#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:53:43 2020

@author: Fabian Robledo @fabianry97
"""

# Secuencias a alinear
DNA_TO_ALIGN1 ="AAAAAATTCGAATCA" 
DNA_TO_BE_ALIGNED = "TATTTTCCCGAATCA"

# Puntuación
MATCH = 1
GAP_PENALTY = -1
MISMATCH = 0


# Inicialización de la matriz
score_matrix = list()
for i, base1 in enumerate(DNA_TO_ALIGN1):
    score_matrix.append(list())
    for base2 in DNA_TO_BE_ALIGNED:
        if base1 == base2:
            score_matrix[i].append(MATCH)
        else:
            score_matrix[i].append(MISMATCH)

# Tenemos una matriz de puntuación con NxM siendo N y M el numero de bases de cada secuencia
# La matriz se inicializa con todo 0s, excepto la primera fila y columna,
# Ambas van desde 0 hasta -N (N igual al numero de nucleotidos de cada secuencia)
similarity_matrix = list()
for i in range(len(DNA_TO_ALIGN1)+1):
    similarity_matrix.append(list())
    for j in range(len(DNA_TO_BE_ALIGNED)+1):
        # Primera fila
        if i == 0:
            similarity_matrix[i].append(-j)
        # Primera columna
        elif j == 0:
            similarity_matrix[i].append(-i)
        # Cualquier otra celda
        else:
            top_left = similarity_matrix[i-1][j-1] + score_matrix[i-1][j-1]
            top = similarity_matrix[i-1][j]+GAP_PENALTY
            left = similarity_matrix[i][j-1]+GAP_PENALTY
            max_value = max(top, left, top_left)
            similarity_matrix[i].append(max_value)

# Recorremos ambas string para hacer ambas combinaciones
alignment1 = ""
alignment2 = ""

i = len(DNA_TO_ALIGN1)
j = len(DNA_TO_BE_ALIGNED)


# Aqui viene la Magia
# Empezando en la celda NxM, nos movemos a aquella a (i-1)x(j), (i)x(j-1) o (i-1)x(j-1), a la que tenga el valor mas alto
# En caso de empate, es irrelevante cual de los dos coger, pues ambos alineamientos son igual de buenos
while (i > 0 or j > 0):
    values = dict()
    if (i != 0 and j != 0):
        value = similarity_matrix[i][j-1]
        key = -1
        if(similarity_matrix[i-1][j] >= value): 
            key = 1
        if(similarity_matrix[i-1][j-1] >= value): 
            key = 0
    elif (i == 0 and j == 0):
        break
    elif (i == 0): # Si i == 0 solo puede ir en vertical
        key = -1
    elif (j == 0): # Si j == 0 solo puede ir en horizontal
        key = 1
    print(i, j, key)
    if (key == -1):
        alignment1 += DNA_TO_ALIGN1[i-1]
        alignment2 += '-'
        if j != 0:
            j -= 1 
    elif (key == 0):
        alignment1 += DNA_TO_ALIGN1[i-1]
        alignment2 += DNA_TO_BE_ALIGNED[j-1]
        if i != 0:
            i -= 1 
        if j != 0:
            j -= 1 
    else:
        alignment1 += '-'
        alignment2 += DNA_TO_BE_ALIGNED[j-1]
        if i != 0:
            i -= 1 

print(alignment1[::-1], DNA_TO_ALIGN1)
print(alignment2[::-1], DNA_TO_BE_ALIGNED)