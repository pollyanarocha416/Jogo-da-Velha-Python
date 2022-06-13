# dois jogadores
#nove casas 
#3 linhas e 3 colunas
X = "X"
O = "O"
VAZIO = " "
#tabuleiro = [0, 1, 2,
#             3, 4, 5,
#             6, 7, 8]
#tabuleiro = [X, O, X,
#             O, X, O,
#             O, VAZIO, X]

#tabuleiro = [VAZIO, VAZIO, VAZIO,
#             VAZIO, VAZIO, VAZIO,
#             VAZIO, VAZIO, VAZIO]

tabuleiro = [X, O, X,
             X, X, VAZIO,
             O, O, O]

#tabuleiro = [X, 0, X,
#             0, X, 0,
#             0, X, 0]


alinhamento = False
vencedor = VAZIO
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
        alinhamento = True
        vencedor = tabuleiro[i]
#if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
#    print("O jogo acabou.")
#if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
#    print("O jogo acabou.")
#if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
#    print("O jogo acabou.")

if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            alinhamento = True
            vencedor = tabuleiro[i]
#if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
#    print("O jogo acabou.")
#if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
#   print("O jogo acabou.")
#if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
#    print("O jogo acabou.")
if not alinhamento:
    for i in range(0, 3, 2):
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-1] != VAZIO:
           alinhamento = True
           vencedor = tabuleiro[i]
#if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
#    print("O jogo acabou.")
#if tabuleiro[6] == tabuleiro[4] == tabuleiro[2]:
#    print("O jogo acabou.")
if alinhamento:
   print("Vencedor:", vencedor)
else:
   if not VAZIO in tabuleiro:
      print("Jogou empatou: Deu velha!")
