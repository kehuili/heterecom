'''
Created on 2016-4-5

@author: huikeli
'''
from numpy import * 

def normMat(mat):
    a = map(sum, mat * mat)
    a = array(a) ** 0.5
    a = tile(a, (shape(mat)[1], 1))
    a = a.T
    mat = mat / a
    return mat
    
def calHete(mat1, mat2):
    a = map(sum, mat1 * mat1)
    a = array([a])
    a = a.T
    b = mat2.T
    b = map(sum, b*b)
    b = array([b])
    
    heteSim = dot(mat1, mat2) / (dot(a, b)) ** 0.5
    return heteSim

if __name__ == '__main__':
    mat = array([[1,1,0,0],[0,1,1,1],[0,0,0,1]])
    mat = normMat(mat)
    mat2 = mat.T
    print calHete(mat, mat2)