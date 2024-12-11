import numpy as np
import random

# Verifica se uma sequência é um palíndromo
def is_palindrome(sequence):
    return sequence == sequence[::-1]

# Gera palíndromos de 3 dígitos, excluindo aqueles com três números iguais
def generate_palindromes():
    palindromes = [[i, j, i] for i in range(1, 10) for j in range(1, 10) if i != j]
    random.shuffle(palindromes)
    return palindromes

# Verifica se o palíndromo já foi usado
def is_valid_palindrome(palindrome, used_palindromes):
    return palindrome not in used_palindromes

# Preenche as diagonais principais dos subquadrantes 3x3 com palíndromos
def fill_palindromes(board):
    palindromes = generate_palindromes()
    used_palindromes = []
    for sq_row in range(3):
        for sq_col in range(3):
            for palindrome in palindromes:
                if is_valid_palindrome(palindrome, used_palindromes):
                    for k in range(3):
                        board[sq_row*3 + k][sq_col*3 + k] = palindrome[k]
                    used_palindromes.append(palindrome)
                    break
            else:
                return False
    return True

# Verifica se um número pode ser inserido no subquadrante
def can_add_to_subquadrant(subquadrant, num, palindrome, duplicate_counts):
    if num in palindrome or np.count_nonzero(subquadrant == num) >= 2:
        return False
    if num not in duplicate_counts and len(duplicate_counts) >= 2:
        return False
    return True

# Preenche o restante das células em cada subquadrante
def fill_subquadrants(board):
    for sq_row in range(3):
        for sq_col in range(3):
            start_row, start_col = sq_row * 3, sq_col * 3
            subquadrant = board[start_row:start_row+3, start_col:start_col+3]
            palindrome = [subquadrant[i, i] for i in range(3)]
            duplicate_counts = {num for num in subquadrant.flatten() if np.count_nonzero(subquadrant == num) > 1 and num not in palindrome}
            for row in range(3):
                for col in range(3):
                    if subquadrant[row, col] == 0:
                        for num in random.sample(range(1, 10), 9):
                            if can_add_to_subquadrant(subquadrant, num, palindrome, duplicate_counts):
                                subquadrant[row, col] = num
                                if fill_subquadrants(board):
                                    return True
                                subquadrant[row, col] = 0
                        return False
    return True

# Gera os primeiros n tabuleiros que atendem às restrições
def generate_boards(n):
    boards = []
    attempts = 0
    while len(boards) < n and attempts < 5000:
        board = np.zeros((9, 9), dtype=int)
        if fill_palindromes(board) and fill_subquadrants(board):
            if not any(np.array_equal(board, b) for b in boards):
                boards.append(board.copy())
        attempts += 1
    if attempts >= 5000:
        print("Aviso: Número máximo de tentativas atingido!")
    return boards

# Função para exibir o tabuleiro
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 20)
        row = "|"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "|"
            row += f"{board[i][j]} "
        print(row)

# Geração e exibição dos tabuleiros
n = 1
boards = generate_boards(n)
for i, board in enumerate(boards, start=1):
    print(f"\nTabuleiro {i}:")
    print_board(board)
