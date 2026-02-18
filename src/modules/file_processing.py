import numpy as np
from PIL import Image, ImageDraw
import os

# Fungsi untuk membaca file sebagai matrix
def readFile(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)
        
    return matrix

color_map = {
    'A': [109, 158, 235], 
    'B': [147, 196, 125], 
    'C': [255, 153, 0],    
    'D': [142, 124, 195], 
    'E': [224, 102, 102], 
    'F': [255, 217, 102],  
    'G': [230, 184, 175], 
    'H': [111, 168, 220], 
    'I': [255, 123, 172], 
    'J': [118, 165, 175], 
    'K': [180, 167, 214], 
    'L': [213, 166, 189],  
    'M': [160, 190, 50], 
    'N': [61, 133, 198], 
    'O': [166, 77, 121],  
    'P': [246, 178, 107], 
    'Q': [204, 0, 0], 
    'R': [69, 129, 142],  
    'S': [106, 168, 79], 
    'T': [159, 197, 232], 
    'U': [0, 160, 160], 
    'V': [249, 203, 156], 
    'W': [182, 215, 168], 
    'X': [207, 226, 243],  
    'Y': [217, 217, 217], 
    'Z': [234, 209, 220]  
}

QUEEN_ICON = None

# Fungsi untuk mengubah matriks menjadi gambar
def matrixToImage(matrix, solution, save_path, color_map):
    global QUEEN_ICON
    n = len(matrix)
    cell_size = 100
    queen_size = int(1/2*cell_size)

    warna = np.zeros((n, n, 3), dtype=np.uint8)
    img = Image.new("RGB", (n*cell_size, n*cell_size), "white")
    draw = ImageDraw.Draw(img)

    if QUEEN_ICON is None:
        if os.path.exists("src/assets/queen_icon.png"):
            raw_img = Image.open("src/assets/queen_icon.png").convert("RGBA")
            QUEEN_ICON = raw_img.resize((queen_size, queen_size), Image.LANCZOS)
        else:
            print("File queen_icon.png not found!")

    for row in range(n):
        for col in range(n):
            x, y = col * cell_size, row * cell_size

            huruf = matrix[row][col]
            warna = tuple(color_map.get(huruf, [255, 255, 255]))
            draw.rectangle([x, y, x + cell_size, y + cell_size], fill=warna, outline="black", width=2)

            if solution and len(solution) > col and solution[col] == row:
                if QUEEN_ICON:
                    offset = (cell_size - queen_size) // 2
                    img.paste(QUEEN_ICON, (x + offset, y + offset), QUEEN_ICON)
                else:
                    draw.ellipse([x+20, y+20, x+80, y+80], fill="black")
    
    if save_path:
        if not save_path.lower().endswith(".png"):
            save_path += ".png"
        img.save(save_path)
    
    return img