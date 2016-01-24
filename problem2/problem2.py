__author__ = 'parvez'
def col_sort(matrix_array, col_index):
    # column wise sort
    for i in range(1,len(matrix_array)):
        key = matrix_array[i][col_index]
        j = i-1
        while j >= 0 and matrix_array[j][col_index] > key :
            matrix_array[j+1][col_index] = matrix_array[j][col_index]
            j -= 1
        matrix_array[j+1][col_index] = key
    # row wise sort
    row_index = 0
    while row_index < 4:
        for i in range(1, len(matrix_array[row_index])-1):
            key = matrix_array[row_index][i]
            # print(key)
            j = i-1
            while j >= 0 and matrix_array[row_index][j] > key:
                matrix_array[row_index][j+1] = matrix_array[row_index][j]
                j -= 1
            matrix_array[row_index][j+1] = key
        row_index += 1


# Delete function
def delete(matrix_array, key):
    key_found = False
    row_index = 0
    col_index = len(matrix_array[row_index])-1
    # search element and replace it with zero
    while row_index < len(matrix_array) and col_index >= 0:
        if matrix_array[row_index][col_index] == key:
            matrix_array[row_index][col_index] = 0
            col_sort(matrix_array, col_index)
            key_found = True
            break
        elif matrix_array[row_index][col_index] > key:
            col_index -= 1
        else:
            row_index += 1
    # for row_index in range(0, len(matrix_array)):
    #     for col_index in range(0, len(matrix_array[row_index])):
    #         if matrix_array[row_index][col_index] == key:
    #             matrix_array[row_index][col_index] = 0
    #             # matrix_array[row_index].pop(col_index)
    #             key_found = True
    #             break
    #         else:
    #             key_found = False
    #     if key_found is True:
    #         break
    if key_found is True:
        print(key, "is deleted")
    elif key_found is False:
        print(key, "is not found")


def matrix():
    array = [[1, 13, 21, 56, 70],
             [3, 15, 25, 60, 73],
             [5, 18, 30, 63, 75],
             [9, 20, 35, 69, 88]]
    print("Original matrix")
    for i in array:
        print(i)
    delete(array, 21)
    delete(array, 63)
    delete(array, 63)
    delete(array, 60)
    delete(array, 35)
    delete(array, 18)
    delete(array, 15)
    delete(array, 5)
    print("After Deletion : Matrix ")
    for i in array:
        print(i)


def main():
    matrix()


if __name__ == '__main__':
    main()
