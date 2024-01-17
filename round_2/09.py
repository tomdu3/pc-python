# Matrix Transposer: Write a function that transposes a matrix
# represented as a list of lists.

def transpose(matrix):
    transposed_matrix = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for col in range(num_cols):
        transposed_matrix.append([matrix[row][col] for row in range(num_rows)])
        
    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))
