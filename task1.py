import numpy as np

def eigvals_vecs(matrix):
    eigvals, eigvecs = np.linalg.eig(matrix)
    eigvals= np.real(eigvals)
    eigvecs = np.real(eigvecs)

    print("Eigenvalues:", eigvals)
    print("Eigenvectors:\n", eigvecs)

    for x in range(len(eigvals)):
        lambda_ = eigvals[x]
        v = eigvecs[:, x]  
        Av = np.dot(matrix, v)
        lambdav = lambda_ * v
        if np.allclose(Av, lambdav):
            is_equal = True
        else: is_equal = False
        
        print(f"Equality for eigval {lambda_:.4f} and eigvec {v}: {is_equal}")
        
    return eigvals, eigvecs

A = np.array([[5, 6], [5, 9]])
print("Test mat. A:\n", A)
vals, vecs = eigvals_vecs(A)