#Matrix Mutliplication

#importing numpy module
import numpy as np

#matrix a
matrix_a=([[1,2],[3,4]])
print(matrix_a)

#matrix b
matrix_b=([[2,3],[4,2]])
print(matrix_b)

#Matrix multiplication or dot multiplication
matrix_multiplication=np.dot(matrix_a,matrix_b)
print("The matrix multiplication of two matrices are : ",matrix_multiplication)

#transpose of matrix a
matrix_transpose_a=np.transpose(matrix_a)
print("Transpose of matrix A : ",matrix_transpose_a)

#transpose of matrix b
matrix_transpose_b=np.transpose(matrix_b)
print("Transpose of matrix B : ",matrix_transpose_b)
