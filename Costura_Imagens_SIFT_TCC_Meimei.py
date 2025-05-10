import os
import time
import cv2
import imutils
from datetime import datetime
import numpy as np

DIR = './pics/Bercario'
R_WIDTH = 8400
WIDTH = 8002
HEIGHT = 4001
BLACK_COLOR = 25
RESULT = './bercario.jpeg'
MAX_WIDTH = 1200  # Reduz a largura das imagens ao importar

def stitch(files):
    # Reduz resolução ao carregar imagens
    imgs = []
    for file in files:
        img_path = os.path.join(DIR, file)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Erro ao carregar imagem: {file}")
            continue  # Ignora arquivos inválidos
        
        print(f"Imagem carregada com sucesso: {file}")
        
        # Redimensiona se a imagem for maior que MAX_WIDTH
        if img.shape[1] > MAX_WIDTH:
            img = imutils.resize(img, width=MAX_WIDTH)
        
        imgs.append(img)
    
    if len(imgs) < 2:
        print("Erro: Não há imagens suficientes para costurar.")
        return None

    stitcher = cv2.Stitcher_create()
    status, pano = stitcher.stitch(imgs)

    if status == 0:
        return pano
    else:
        print(f"Erro ao costurar imagens. Código de status: {status}")
        return None

def crop(img):
    # Remoção de bordas pretas (igual ao código original)
    width, height = img.shape[1], img.shape[0]

    if width > R_WIDTH:
        img = imutils.resize(img, width=R_WIDTH)

    top, bottom = 0, height
    limit = int(height/8)

    # Remover borda superior
    for c in range(width):
        for r in range(limit):
            if sum(img[r, c]) >= BLACK_COLOR:
                top = max(top, r)
                break
    top += 1

    # Remover borda inferior
    for c in range(width):
        for r in range(height - 1, height - limit, -1):
            if sum(img[r, c]) >= BLACK_COLOR:
                bottom = min(bottom, r)
                break
    bottom -= 1

    img = img[top:bottom, :]

    return img

if __name__ == '__main__':
    start = time.time()
    files = os.listdir(DIR)
    files = [f for f in os.listdir(DIR) if f.lower().endswith(('.jpeg','.jpg','.png'))]
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('\n')
    if not files:
        print("Erro: Nenhuma imagem encontrada no diretório.")
    else:
        pano = stitch(files)
        if pano is not None:
            pano = crop(pano)
            cv2.imwrite(RESULT, pano)
            print("Imagem panorâmica salva com sucesso!")
        else:
            print("Erro ao gerar a imagem panorâmica.")

    end = time.time()
    print('Tempo total:', round(end - start, 2), "segundos")