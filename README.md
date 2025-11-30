# verificacao_de_identidade

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
Os dados usados pelo sistema, são gerados por ele mesmo, quando solicitado a ele pressionando 
a tecla R, ele apenas extrai os embeddings para verificar se realmente tem uma pessoa ali, 
depois ele salva o frame da webcam em um formato JPEG na pasta faces (exemplo: faces/face_0.jpeg),
apos isso ele segue normalmente com a verificação de faces. depois de cada verificação feita,
ele salva na memoria quanto tempo ele levou para fazer a verificação e a similaridade de cada
rosto, para gravar essa informação, basta precionar a tecla g para ele gravar as metricas
da sessão atual.

## Como reproduzir
```bash
python -m venv .venv
# ativar ambiente...
pip install -r requirements.txt
python src/main.py --seed 42

## Resultados do Projeto

(Principais métricas + 2–3 gráficos com 1–2 linhas de interpretação)

Estrutura

(src/, data/, models/, reports/, notebooks/)
