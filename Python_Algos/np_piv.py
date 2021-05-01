
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.kernel_ridge import KernelRidge

import tensorflow as tf
from tensorflow_probability.python.internal import tensorshape_util
from tensorflow_probability.python.internal import prefer_static

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import sys
sys.stdout = open('output_np_piv.txt','wt')

def print_line():
    print("___________________________________________________________________________________________________")


def pivoted_cholesky(matrix, max_rank, diag_rtol=1e-3, name=None):
    
    matrix_shape = np.asarray(matrix.shape)
    print("mat shape = ", matrix_shape, type(matrix_shape))
    
    matrix_diag = np.diagonal(matrix)
    print("matrix_diag = ", matrix_diag)
    
    orig_error =  np.amax(matrix_diag)
    print("orig_error = ", orig_error)  
    
    def body(m, pchol, perm, matrix_diag):
        
      print_line()
      
      print()
      print("m = ", m)
      
      print_line()
      print("pchol = \n", pchol)
      print_line()
      print("perm = ", perm)
      print_line()
      print("matrix_diag = ", matrix_diag)
      
      print(str(type(matrix_diag)))
      
      
      if str(type(matrix_diag)) != '<class \'numpy.ndarray\'>':
        matrix_diag = matrix_diag.numpy()
        
      print("permuted_diag = ", perm)
      maxi = np.argmax(matrix_diag[perm[m:]]) + m
      
      print("maxi = ", maxi)
      print_line()
      
      maxval = matrix_diag[perm][maxi]
      print("maxval = ", maxval)
      
      perm[m], perm[maxi] = perm[maxi], perm[m]
      print("perm after swap = ", perm)
      
      
      
      row = matrix[perm[m]][perm[m + 1:]]
      
      print("row = ", row, row.shape)
      
      batch_dims = tensorshape_util.rank(matrix.shape) - 2
      def batch_gather(params, indices, axis=-1):
        return tf.gather(params, indices, axis=axis, batch_dims=batch_dims)
    
      prev_rows = pchol[..., :m, :]
      prev_rows_perm_m_onward = batch_gather(prev_rows, perm[..., m + 1:])
      prev_rows_pivot_col = batch_gather(prev_rows, perm[..., m:m + 1])
      row -= tf.reduce_sum(
          prev_rows_perm_m_onward * prev_rows_pivot_col,
          axis=-2)[..., tf.newaxis, :]
      
      pivot = np.sqrt(maxval); row /= pivot
      
      row = np.concatenate([[[pivot]], row], -1)
      
      print("row after concat = ", row, "\n")
      def _invert_permutation(perm):  # TODO(b/130217510): Remove this function.
        return tf.cast(tf.argsort(perm, axis=-1), perm.dtype)
    
      paddings = tf.concat([
          tf.zeros([prefer_static.rank(pchol) - 1, 2], dtype=tf.int32),
          [[tf.cast(m, tf.int32), 0]]], axis=0)
      diag_update = tf.pad(row**2, paddings=paddings)[..., 0, :]
      reverse_perm = _invert_permutation(perm)
      
      print("diag update = ", diag_update, "reverse_perm  = ", reverse_perm )
      
      matrix_diag -= batch_gather(diag_update, reverse_perm)
      
      print("matrix diag = ", matrix_diag)
    #   matrix_diag[perm[m:]] -= row**2
      
      pchol[m, perm[m:]] = row
      pchol_shape = pchol.shape
      
      print_line()
      print("concat a :: ", pchol[..., :m, :])
      print('')
      print("rownib :: ", row)
      print('')
      print("concat c :: ", pchol[..., m + 1:, :] )
      print('')
      print_line()

      return m + 1, pchol, perm, matrix_diag
      
    m = np.int64(0)
    pchol = np.zeros(matrix_shape, dtype=matrix.dtype)[..., :max_rank, :]
    
    print_line()
    print("pchol1 = \n", pchol)
    
    perm = tf.broadcast_to(
        prefer_static.range(matrix_shape[-1]), matrix_shape[:-1])
    
    print_line()
    perm = perm.numpy()
    print("perm = ", perm)

    def check_cond(m, pchol, perm, matrix_diag):
      del pchol
      del perm
      error = np.linalg.norm(matrix_diag, ord=1, axis=-1)
      max_error = np.amax(error / orig_error)
      print("conds = ", m < max_rank, m == 0, max_error> diag_rtol)
      return ( m >= max_rank ) 

    while(1):
      m, pchol, perm , matrix_diag = body(m, pchol, perm, matrix_diag)
      if check_cond(m, pchol, perm, matrix_diag):
          break
    
    pchol = np.transpose(pchol)
    
    return pchol
    # tensorshape_util.set_shape(
    #     pchol, tensorshape_util.concatenate(matrix_diag.shape, [None]))
    # return pchol

# matA = np.array([[10, 7, 8, 6, 3], [7, 10, 2, 5, 9], [8, 2, 10, 6, 8], [6, 5, 6, 10, 9], [3, 9, 8, 9, 10]], dtype=np.float32)
# print("MatA = ", matA)

import pandas as pd
energy_set = pd.read_csv('energy.csv')


X = pd.read_csv('energy.csv', usecols=['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'])
y = pd.read_csv('energy.csv', usecols=['Y1'])

X = X.values
y = y.values

X = X[:4]
y = y[:4]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

kernel_matrix = sklearn.metrics.pairwise.laplacian_kernel(X, Y=None, gamma=None)

print("Kernel matrix = \n", kernel_matrix, "\n \n")

kernel_matrix.shape

kernel_matrix.shape, np.linalg.norm(kernel_matrix)



lr = pivoted_cholesky(
        kernel_matrix, 3)    

print_line()

print("after piv: \n")

print_line()

# lr = lr.numpy()

lr_t = np.transpose(lr)
lr_approx = np.matmul(lr, lr_t)

print("\n approx = lr * lrT = \n", lr_approx)

print("RANK = ", np.linalg.matrix_rank(lr_approx))

print_line()
print("kernel_matrix = ", kernel_matrix)

print(kernel_matrix.shape)
print("kernel_mat_norm = ", np.linalg.norm(kernel_matrix))

print(lr_approx.shape, "approx_norm = ", np.linalg.norm(lr_approx))