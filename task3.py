import numpy as np

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector

def decrypt_message_(encrypted_vector, key_matrix):
    eigvals, eigvecs = np.linalg.eig(key_matrix)
    inv_eigvals = 1 / eigvals
    inv_diag_key_mat= np.dot(np.dot(eigvecs, np.diag(inv_eigvals)), np.linalg.inv(eigvecs))
    dec_vec = np.dot(inv_diag_key_mat, encrypted_vector)
    dec_vec = np.round(np.real(dec_vec)).astype(int)
    dec_msg = "".join([chr(val) for val in dec_vec])
    return dec_msg 


ref = "Hello, World!"
key_matrix = np.random.randint(0, 256, (len(ref), len(ref)))
enc = encrypt_message(ref, key_matrix)
dec = decrypt_message_(enc, key_matrix)
print("Original Message:", ref)
print("Encrypted Message:", enc)
print("Decrypted Message:", dec)