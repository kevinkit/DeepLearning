# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:48:29 2016

@author: kevin

#Labor 2
"""

from numpy.linalg import inv
from numpy.linalg import lstsq
from numpy.linalg import norm
import numpy as np


#random seed
np.random.seed(1)
A = np.random.randn(2,2)

#1...12
#eine Matrix A der Dimension 3x4 und füllen sie diese mit den Zahlen 1...12 im Floatformat
A = np.arange(1,13).reshape(3,4);
print A
print A.dtype

# eine Matrix B der Dimension 3x4 und füllen Sie diese mit Zufallszahlen.
B = np.random.randn(3,4);
print B
print B.dtype


# Geben Sie das Ergebnis der Inversion von A aus. 
A1 = np.ones((4,4));
A1[0:3,0:4] = A;
inv(A1)

#Transponieren Sie B
BT = np.transpose(B)

#- Bilden Sie das Punktprodukt von A und B.

DOT = np.dot(B,A1);


#- Multiplizieren Sie A und B elementweise.
ELE = np.multiply(A,B);


#Summieren Sie alle Spalten von B
colsumb = np.sum(B,1);

#- Berechnen Sie den Mittelwert von B.
avgb = np.average(B);

#Geben sie Spalten von B aus, die in den ersten beiden Elementen der ersten Zeile von A stehen
#“array ([[ 4., 5., 6.], [ 7., 8., 9.]])“
print B[A[0,0]]
print B[A[0,1]]


#Führen Sie die Matrixmultipikationen AB und BA aus, geben Sie die Dimensionen der
#Ergebnisse aus
AB = A*B;
print AB.shape
BA = B*A;
print BA.shape


#Überscheiben Sie B mit den elementweisen Quadratwurzeln von A.
B = np.sqrt(A)

#Überscheiben Sie B mit B*B und vergleichen Sie danach elementweise A mit B. Was stellen Sie
#fest?
B = B*B;


#Geben Sie den kleinsten Wert von B aus.
print np.amin(B)


#- Geben Sie den Index des Wertes von B aus, welcher am weitesten von 0 entfernt ist.
print np.argmax(np.abs(B))


#Geben Sie alle ungeraden Zahlen aus A in umgekehrter Reihenfolge aus.

sh = A.shape;

for i in range(sh[0] -2,-1,-1):
    for j in range(sh[1] -1,-1,-1):
        if np.mod(A[i,j],2) != 0:
            print A[i,j]
        

#Erweitern sie A um [13 , 14 , 15, 16], so das A nun die Dimension 4x4 hat.

At = np.append(A,[13,14,15,16]);

A = At.reshape(4,4);
print A


#- Generieren Sie die Vektoren v und b aus Einsen, sodass die Operation Av + b möglich ist und
#einen Vektor ergibt. 


v = np.ones(shape=(4,1));
b = np.ones(shape=(4,1));
 
print A.dot(v) + b




#
#Berechnen Sie die L1 und L2 Distanzen zwischen A und B.
B = np.append(B,[0,0,0,0]);

B = B.reshape(4,4);





L1 = norm(A -B); 


#L2 fehlt wird aber wohl kaum gebraucht,....






