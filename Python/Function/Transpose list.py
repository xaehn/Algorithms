def transpose_list(_list, col = None, row = None):
    if col == None:
        col = len(_list)

    if row == None:
        row = len(_list[0])

    transposed_list = [col * [None] for _ in range(row)]
    for index_col in range(col):
        for index_row in range(row):
            transposed_list[index_row][index_col] = _list[index_col][index_row]

    return transposed_list