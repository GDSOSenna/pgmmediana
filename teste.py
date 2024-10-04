import os
from PIL import Image
import numpy as np

#Aplica filtro
def aplicar_filtro_mediana(imagem, tamanho_janela):
    matriz = np.array(imagem)
    matriz_filtrada = matriz.copy()
    offset = tamanho_janela // 2
    
    for i in range(offset, matriz.shape[0] - offset):
        for j in range(offset, matriz.shape[1] - offset):
            janela = matriz[i-offset:i+offset+1, j-offset:j+offset+1]
            matriz_filtrada[i, j] = np.median(janela)
    
    return matriz_filtrada

#puxa imagemm do diretório
def carregar_imagem_pgm(caminho):
    with open(caminho, 'r') as file:
        tipo_magico = file.readline().strip()
        largura, altura = map(int, file.readline().split())
        max_val = int(file.readline().strip())
        
        dados_imagem = []
        for linha in file:
            dados_imagem.extend(map(int, linha.split()))
        
        imagem = np.array(dados_imagem).reshape((altura, largura))
        return imagem

#salve a image, como pgm
def salvar_imagem_pgm(caminho, imagem):
    altura, largura = imagem.shape
    with open(caminho, 'w') as file:
        file.write("P2\n")
        file.write(f"{largura} {altura}\n")
        file.write("255\n")  # Valor máximo de cinza
        
        for linha in imagem:
            file.write(" ".join(map(str, linha)) + "\n")

#consegue processar diversas imagens através de inputs
def processar_varias_imagens():
    
    #nome da pasta onde será salvo as imagens filtradas
    pasta_saida = "Filtradas"

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    while True:
        caminho_imagem = input("Digite o caminho da imagem PGM ou 'sair' para terminar: ")
        
        if caminho_imagem.lower() == 'sair':
            print("Processamento encerrado.")
            break
        
        if not os.path.exists(caminho_imagem):
            print(f"Erro: O caminho '{caminho_imagem}' não existe. Tente novamente.")
            continue
        
        try:
            imagem = carregar_imagem_pgm(caminho_imagem)
            imagem_filtrada = aplicar_filtro_mediana(imagem, 3)
            
            nome_saida = os.path.join(pasta_saida, os.path.splitext(os.path.basename(caminho_imagem))[0] + '_filtrada.pgm')
            salvar_imagem_pgm(nome_saida, imagem_filtrada)
            print(f"Imagem filtrada salva como: {nome_saida}")
        
        except Exception as e:
            print(f"Ocorreu um erro ao processar a imagem: {e}")

processar_varias_imagens()
