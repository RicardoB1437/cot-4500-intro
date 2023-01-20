1. #Print a specific 3x3 matrix where a cell is 1 if i == j, else 0 
2. #Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j  
3. #Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created

import numpy as np

if __name__ == "__main__":
    print("hello")
    array = np.identity(3)
    print(array)
    print()
    #print(array.shape)
    rows, cols = array.shape
    #print(len(array))
    for row in range(rows):
        #print(row)
        for cell in range(cols):
            #print(cell)
            if array[row][cell] == 0:
                array[row][cell] = 3
    print(array)
    print()
    #print(array.shape)
    cut_array = np.delete(array, np.s_[-1:], axis=1)
    print(cut_array)