
# 🧵 Stitcher de Imagens com OpenCV

**Autores:**  
Bruna dos Santos Freitas  
Carlos Baroni Piolla  
Guilherme Silveira Cavinato  
Thiago Cardoso Hanna

---

Este script Python realiza a **costura de imagens panorâmicas** utilizando a função `cv2.Stitcher_create()` da biblioteca **OpenCV**, que internamente aplica algoritmos como **SIFT (Scale-Invariant Feature Transform)** para detecção e correspondência de pontos-chave entre as imagens.

Ele foi desenvolvido como parte do processo de geração de imagens 360° para o ambiente do **berçário** no tour virtual do projeto de TCC do **Cantinho da Meimei**.

---

## 📌 Funcionalidade Principal

🔧 O script tem como objetivo unir automaticamente diversas imagens sobrepostas de um mesmo ambiente, gerando uma única imagem panorâmica contínua.  

✅ Além da costura, o script:
- **Reduz a resolução** das imagens para agilizar o processo;
- **Ignora arquivos inválidos** ou não suportados;
- **Recorta bordas pretas** superiores e inferiores;
- **Salva a imagem final** em alta resolução no caminho especificado.

---

## ⚙️ Tecnologias e Algoritmos

- **OpenCV**: biblioteca principal para processamento de imagem.
- **SIFT** (via `cv2.Stitcher_create()`): detecta características robustas e invariante à escala para realizar o alinhamento entre as imagens.
- **Imutils**: facilita operações como redimensionamento e ajustes de imagem.

> ⚠️ A função `cv2.Stitcher_create()` utiliza o algoritmo **SIFT**, que oferece ótima performance para montagem de panoramas e é robusto a variações de iluminação e perspectiva.

---

## 🗂️ Estrutura e Parâmetros

### Diretórios e Arquivos:
- `./pics/Bercario/`: pasta onde estão as imagens a serem costuradas
- `./bercario.jpeg`: saída final da imagem panorâmica

### Parâmetros customizáveis:
- `MAX_WIDTH = 1200`: largura máxima para redimensionar imagens antes da costura
- `BLACK_COLOR = 25`: limiar para remoção de bordas pretas
- `R_WIDTH = 8400`: largura máxima da imagem costurada antes do recorte

---

## 🚀 Como Executar

1. Coloque as imagens na pasta `./pics/`
2. Execute o script com Python:

```bash
python Costura_Imagens_SIFT_TCC_Meimei.py
```

3. A imagem panorâmica final será salva como `bercario.jpeg` na raiz do projeto.

---

## 🧪 Requisitos

- Python 3.x
- OpenCV (`opencv-python`)
- Imutils (`imutils`)
- Numpy

Instale com:
```bash
pip install opencv-python imutils numpy
```

---

## 📷 Observações

- As imagens devem ter **sobreposição suficiente** para que o algoritmo de correspondência funcione corretamente.
- O recorte inferior/superior ajuda a remover bordas escuras que geralmente aparecem após a projeção panorâmica.
- O script pode ser adaptado para outros ambientes do tour alterando o caminho da pasta e do arquivo de saída.
