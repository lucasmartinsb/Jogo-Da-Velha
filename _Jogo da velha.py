quadro = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
valido = True
jogo_continua = True
Velha = ('velha')

def mostrar_quadro () :
    print ('\n')
    print (quadro[0] + '|' + quadro[1] + '|' + quadro[2] + '     1 | 2 | 3')
    print (quadro[3] + '|' + quadro[4] + '|' + quadro[5] + '     4 | 5 | 6')
    print (quadro[6] + '|' + quadro[7] + '|' + quadro[8] + '     7 | 8 | 9')
    print ('\n')


def jogador_x () :
    global valido
    print ('Vez de X')
    posicao = input('Escolha uma posicao de 1-9: ')
    while posicao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print ('Entrada não válida')
        posicao = input('Escolha uma posicao de 1-9:')
    posicao.isnumeric()
    while posicao.isnumeric() == False:
        posicao = input('Escolha uma posicao de 1-9:')
    posicao = int(posicao) - 1
    quadro[posicao].isupper
    while quadro[posicao].isupper() == True:
        print ('Posição não válida')
        posicao = input('Escolha uma posição de 1-9:')
        posicao = int(posicao) - 1
    quadro[posicao] = 'X'
    mostrar_quadro ()
    check_vencedor ()
    if jogo_continua == False:
        jogar_novamente()
    if jogo_continua == True:
            jogador_o ()

def jogador_o () :
    global valido
    print ('Vez de O')
    posicao = input('Escolha uma posicao de 1-9: ')
    while posicao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        posicao = input('Escolha uma posicao de 1-9:')
    while posicao.isnumeric() == False:
        posicao = input('Escolha uma posicao de 1-9:')
    posicao = int(posicao) - 1
    quadro[posicao].isupper
    if quadro[posicao].isupper() == True:
        print ('Posição nao válida')
        posicao = input('Escolha uma posição de 1-9:')
        posicao = int(posicao) - 1
    quadro[posicao] = 'O'
    mostrar_quadro ()
    check_vencedor ()
    if jogo_continua == False:
        jogar_novamente()
    if jogo_continua == True:
        jogador_x ()

def check_vencedor () :
    vencedor_linha = linha()
    vencedor_vertical = vertical ()
    vencedor_diagonais = diagonais ()
    velha = deu_velha ()
    if vencedor_linha:
        print ('O vencedor é: {}'.format(vencedor_linha))
    elif vencedor_vertical:
        print ('O vencedor é: {}'.format (vencedor_vertical))
    elif vencedor_diagonais:
        print ('O vencedor é: {}'.format (vencedor_diagonais))
    elif velha:
        print ('O jogo deu velha')

def linha () :
    global jogo_continua
    linha_1 = quadro[0] == quadro[1] == quadro[2] != '-'
    linha_2 = quadro[3] == quadro[4] == quadro[5] != '-'
    linha_3 = quadro[6] == quadro[7] == quadro[8] != '-'
    if linha_1 or linha_2 or linha_3: 
        jogo_continua = False
    if linha_1:
        return quadro[0] 
    elif linha_2:
        return quadro[3] 
    elif linha_3:
        return quadro[6] 
    else:
        return None

def vertical () :
    global jogo_continua
    vertical_1 = quadro[0] == quadro[3] == quadro[6] != '-'
    vertical_2 = quadro[1] == quadro[4] == quadro[7] != '-'
    vertical_3 = quadro[2] == quadro[5] == quadro[8] != '-'
    if vertical_1 or vertical_2 or vertical_3:
        jogo_continua = False
    if vertical_1:
        return quadro[0]
    elif vertical_2:
        return quadro[1]
    elif vertical_3:
        return quadro[2]
    else:
        return None

def diagonais () :
    global jogo_continua
    diagonal_1 = quadro[0] == quadro[4] == quadro[8] != '-'
    diagonal_2 = quadro[2] == quadro[4] == quadro[6] != '-'
    if diagonal_1 or diagonal_2:
        jogo_continua = False
    if diagonal_1:
        return quadro[0]
    elif diagonal_2:
        return quadro[2]
    else:
        return None

def deu_velha () :
    global jogo_continua
    if '-' not in quadro:
        jogo_continua = False
        return Velha
    else:
        return None
def jogar_novamente() :
    global quadro
    global jogo_continua
    dnv = str(input('Deseja jogar novamente? [S] [N]'))
    if dnv == 's' or dnv == 'S' or dnv == 'n' or dnv == 'N':
        dnv = str(dnv)
    else:
        print ('Entrada não válida')
        dnv = str(input('Deseja jogar novamente? [S] [N]'))
    while dnv not in['s','S','n','N']:
        print ('Entrada não válida')
        dnv = str(input('Deseja jogar novamente? [S] [N]'))
    if dnv=='s' or dnv=='S' :
        quadro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        jogo_continua = True
        jogar()
    if dnv=='n' or dnv=='N':
        input('Pressione enter para sair')

def jogar () :
    mostrar_quadro()
    jogador_x ()

jogar ()