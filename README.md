# Verificação de Identidade por Reconhecimento Facial Identificação

## Equipe
- Nome Ygor samuel nanes de oliveira — RA: 2225201035
Turma: 41 | Curso: Ciencia da computação| Período: Noturno | Ano: 2025

## Problema
imagine a seguinte situação, você precisa entrar em algum local restrito ou então
confirmar sua identidade ou presença, porém seu crachá está danificado ou foi perdido, ou
até mesmo ele ainda não está pronto, e você precisa fazer essa confirmação; é aqui aonde o 
projeto entra em ação, ultilizando apenas do seu rosto, em poucos segudos sua identidade é
confirmada.

## Abordagem de IA
Neste projeto, foi ultilizado reconhecimento facil baseado em aprendizado de máquina, atravês
da biblioteca face_recognition, onde a mesma trabalha com um modelo de deep learning baseado
em resnet_based para a deteccção e codigicação facial. o projeto funciona em duas fases, a
primeira parte faz a extração dos embeddings faciais pela webcam a cada tempo,por meio 
da biblioteca OpenCv; depois ele faz uma comparação por distancia euclidiana com o banco de 
faciais que ele tem, dependendo da distancia, ele retorna se é mesma pessoa ou não e retorna 
a conversão da distancia em probabilidade para o usuario. esse conjuto todo é excelente para 
o caso proposto, já que opera de modo offline e não precisa de muito tempo para fazer a 
verificação.

## Dados
Os dados usados pelo sistema, são gerados por ele mesmo, para fins de gerar metricas,
foram usados rosto não são reais, foram obtidos atravês do site https://this-person-does-not-exist.com/en.
quando solicitado a ele pressionando a tecla R, ele apenas extrai os embeddings para verificar 
se realmente tem uma pessoa ali,depois ele salva o frame da webcam em um formato JPEG na pasta faces 
(exemplo: faces/face_0.jpeg),apos isso ele segue normalmente com a verificação de faces. 
depois de cada verificação feita,ele salva na memoria quanto tempo ele levou para fazer a verificação 
e a similaridade de cada rosto, para gravar essa informação, basta precionar a tecla g para ele 
gravar as metricas da sessão atual.

## Como reproduzir
```bash
python -m venv .venv

## ativar ambiente...

python src/main.py

## Dependências do face_recognition (importante!!)

O pacote `face_recognition` utiliza a biblioteca `dlib`, que requer CMake
para funcionar corretamente., em alguns sistemas também pode ser necessário
instalar o CMake manualmente:

Download oficial: https://cmake.org/download/

pip install -r requirements.txt

## Resultados do Projeto

resultados

Foi criado um gráfico exbiindo o tempo que cada reconhecimento levou, onde boa parte das execuções
teve uma latência baixa com algumas variações por conta do hardware. Além do grafico de similaridade 
que mostra de formaamigavel o percentual da verificação entre as variações dos rostos, quedas no
grafico, muitas vezes é por causa de 3 fatores: Movimento, Iluminação do local ou então algum 
objeto no rosto(Oculos,bone, mascara por exemplo.)

Estrutura:

src/
 ├─ main.py            # Executa o sistema de reconhecimento facial
 ├─ recontoshi.py      # Funções de reconhecimento, salvamento e cálculo
 ├─ grafic_matplot.py  # Gera gráficos de latência e similaridade
 ├─ vars.py            # Armazena métricas da sessão
faces/
 └─ face_0.jpeg        # Banco de rostos cadastrados
reports/
 └─ algumnome_mt_loko                # Gráficos gerados

 ## Requisitos mínimos
- Python 3.10 ou superior
- Webcam integrada ou USB
- Windows 10/11
- CMake instalado no sistema (Windows MSI recomendado)