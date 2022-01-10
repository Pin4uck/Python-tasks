def search_in_matrix(string_letters, word):
    matrix_size = int(len(string_letters) ** 0.5)  # вычисляем размер стороны квадратной матрицы
    matrix = numpy.array(list(string_letters)).reshape(matrix_size, matrix_size).tolist()  # создаем матрицу
    num_row = len(matrix)  # число строк матрицы
    num_column = len(matrix[0])  # число столбцов матрица, 4 и 5 строки кода можем объединить, так как матрица квадратная
    word_length = len(word)
    result = []

    def search_word(row, column, index_in_word):
        if index_in_word == word_length:  # если индекс вышел за длинну слова, то мы нашли слово.
            return True
        elif 0 <= row < num_row and 0 <= column < num_column and matrix[row][column] == word[index_in_word]:  # следим за диапазоном и ловим нужную букву
            value = matrix[row][column]  # запомним значение, на случай если мы нашли нужную букву, но не слово
            result.append([row, column])
            matrix[row][column] = None  # вместо букв найденного слова будет значение None
            if search_word(row+1, column, index_in_word+1) or search_word(row-1, column, index_in_word+1) or search_word(row, column+1, index_in_word+1) or search_word(row, column-1, index_in_word+1):
                return True
            result.pop()
            matrix[row][column] = value  # возращаем значение на место, так как нашли не то, что нужно
        return False
    for row_index in range(num_row):
        for column_index in range(num_column):
            if search_word(row_index, column_index, 0):
                return result


if __name__ == '__main__':
    import numpy
    inp_string_letters = input('Enter a string of letters:\n').upper()  # валидацию данных я не делал, алгоритм ожидает что данные будут введены верно
    inp_word = input('Enter your word:\n').upper()
    print(*search_in_matrix(inp_string_letters, inp_word))
