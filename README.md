#P1 Computação Gráfica - 8B Noturno#
#RA 742759#
#Gustavo Senna Duarte Oliveira#


#Filtro mediano para imagens PGM

Descrição do Projeto
Este projeto implementa um filtro medial para imagens PGM (Portable GrayMap). Um filtro mediano é usado para reduzir o ruído em uma imagem enquanto preserva as bordas. Este código é escrito em Python e permite carregar imagens no formato PGM, aplicar filtros e salvar as imagens geradas em uma pasta do seu projeto.

Como funciona o filtro de mediana
O filtro de mediana substitui o valor de cada pixel pelo valor médio do seu entorno, em uma janela de tamanho fixo (ex. 3x3). Isso ajuda a distinguir alto contraste (ruído), preservando informações importantes, como bordas.

Método de filtro:
Para cada pixel da imagem:
Definimos uma janela ao redor do ponto central (geralmente 3x3).
Coletamos valores de pixel nesta janela.
Pegamos os valores e encontramos a mediana.
Substitua o valor do pixel central pela mediana calculada.
Em pixels próximos à borda da imagem, o filtro ajusta a janela para que não ultrapasse a borda da imagem.

#Estrutura de código

1. def aplicar_filtro_mediana(imagem, tamanho_janela)
Esta função aplica um filtro mediano à imagem completa.

Introdução: 

Figura: Matriz representando a imagem PGM completa.
window_size: O tamanho da janela a ser usada (normalmente 3x3).

Como funciona: Converte uma imagem em uma matriz NumPy.

Para cada pixel, desenhe uma janela ao redor do pixel central, ajustando a borda da janela para que não ultrapasse a borda da imagem.

Ajusta a mediana dos valores da janela e a substitui pelo pixel central.
Retorna uma nova matriz de imagens filtradas.

2. def carregar_imagem_pgm(caminho)
A função é responsável por carregar a imagem PGM do caminho determinado.

caminho: O caminho para o arquivo PGM.

3. def salvar_imagem_pgm(caminho, imagem)
A função salva a imagem filtrada no formato PGM.

Entrada:

caminho: os filtros de imagem serão armazenados. 
Figura: Imagem de representação do array NumPy.

Como funciona:
Salve a matriz como um arquivo PGM, incluindo cabeçalhos e imagens de pixel apropriadas.

4. def processar_varias_imagens()
A função principal permite o processamento de múltiplas imagens.

Ação:

Execute um script Python em um terminal ou ambiente de desenvolvimento.

Quando solicitado, insira o caminho da imagem PGM que deseja editar. A imagem filtrada será salva automaticamente na pasta Filtradas com o nome _filtrada.pgm.

OBS: O caminho deve ser digitado no formato padrão, exemplo: C:\projetos\pgm_filter\nome_do_arquivo.pgm

Para finalizar o processamento, digite exit.

Problema
Manipulação de bordas: foi necessário modificar o código para evitar que a janela central se estendesse além das bordas da imagem, o que poderia causar “estouro de valores”. O problema foi resolvido alterando o centro da janela de função para um pixel mais próximo da borda.

Conclusão
Este projeto oferece uma boa solução para colocar filtros entre imagens PGM. É adaptável a diferentes tamanhos de janela e pode ser facilmente ajustado para suportar outros formatos de imagem, se necessário. A filtragem mediana é uma ferramenta poderosa de processamento de imagem para suavizar e remover ruído.