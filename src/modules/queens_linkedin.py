visual_callback = None

# Fungsi untuk memeriksa apakah papan yang diberikan valid
def isValid(matrix):
    # Papan kosong tidak valid
    if not matrix:
        return False
    
    num_rows = len(matrix)
    unique_colors = set()
    for row in matrix:
        # Memeriksa apakah papan persegi
        if len(row) != num_rows:
            return False
        
        # Memeriksa apakah setiap emelemn adalah huruf kapital 
        for char in row:
            if not isinstance(char, str) or not char.isalpha() or not char.isupper():
                return False
            unique_colors.add(char)
    
    if len(unique_colors) != num_rows:
        return False
        
    return True

# Fungsi untuk memeriksa apakah aman untuk meletakkan queen pada baris new_row
def isSafe(current_p, new_row, colored_board): 
    current_col = len(current_p) 

    new_color = colored_board[new_row][current_col]

    # Melakukan iterasi dari kolom pertama hingga kolom terakhir sebelum kolom yang akan diisi
    for prev_col, queen_row in enumerate(current_p):
        # Cek Baris 
        if queen_row == new_row:
            return False
            
        # Cek Warna 
        if colored_board[queen_row][prev_col] == new_color:
            return False
    
    # Cek apakah queen pada kolom sebelumnya bersinggungan dengan queen sekarang
    if current_col > 0:
        prev_row = current_p[current_col - 1]
        if abs(prev_row - new_row) == 1:
            return False

    return True

# Fungsi untuk memeriksa apakah susunan queen pada papan aman
def isSolution(p, colored_board):
    region_used = set()
    current_p = []
    for col in range(len(p)):
        row = p[col]

        if not isSafe(current_p, row, colored_board):
            return False

        current_p.append(row)
    return True

# Fungsi yang menyelesaikan permainan Queens LinkedIn secara rekursif dengan pruning (backtracking)
def recursiveWithPruning(n, current_p, colored_board):
    global i, visual_callback
    
    if len(current_p) == n:
        return current_p
    
    for row in range(n):
        i+=1

        if i % 100000 == 0:
            visual_callback(current_p + [row])
        if isSafe(current_p, row, colored_board):
            result = recursiveWithPruning(n, current_p + [row], colored_board)
        
            if result is not None:
                return result
    
    return None

# Fungsi yang menyelesaikan permainan Queens LinkedIn secara rekursif tanpa pruning (exhaustive search)
def recursiveWithoutPruning(n, current_p, colored_board):
    global i, visual_callback
    if len(current_p) == n:
        i+=1

        if i % 25000000 == 0:
            visual_callback(current_p + [row])
            
        if isSolution(current_p, colored_board):
            return current_p
        return None

    for row in range(n):
        
        result = recursiveWithoutPruning(n, current_p + [row], colored_board)
        if result is not None:
            return result
            
    return None

# Fungsi untuk menemukan susunan queen pertama yang aman
def findFirstSolution(n, colored_board, use_pruning=True):
    global i
    i = 0
    if use_pruning:
        return recursiveWithPruning(n, [], colored_board)
    else:
        return recursiveWithoutPruning(n, [], colored_board)
