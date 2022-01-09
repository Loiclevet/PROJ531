import chess

'''
D'abord, on crée une fonction pieceValue() car on en a besoin pour définir la fonction evaluation()
'''
def pieceValue(piece):
  if piece == None:
    return 0
  #pour une meilleure utilisation, on donne des valeurs négatives aux pions noirs(représentés par des minuscules) et positives aux pions blancs
  elif piece == 'P':
    return 1
  elif piece == 'N':
    return 2
  elif piece == 'B':
    return 3
  elif piece == 'R':
    return 5
  elif piece == 'Q':
    return 9
  elif piece == 'K':
    return 500
  elif piece == 'p':
    return -1
  elif piece == 'n':
    return -2
  elif piece == 'b':
    return -3
  elif piece == 'r':
    return -5
  elif piece == 'q':
    return -9
  elif piece == 'k':
    return -500

'''
La fonction evaluation() sert à donner une note au plateau, càd en déduire l'équipe qui a l'avantage, elle nous sera utile pour définir les méthodes minmax() et alphabeta()
méthode utilisée : 10*valeur de la pièce+nombre de déplacements possibles de la pièce(https://www.youtube.com/watch?v=gXywCc_KIMM)
'''
def evaluation(board):
  blackScore = 0  
  whiteScore = 0
  #on parcoure tout le plateau(il y a 64 cases et la première case est d'indice 0)
  for i in range(0,64):
    moves=0
    #pour chaque case, on définit le nb de coups légaux possibles
    for move in board.legal_moves:
        moves+=1
    #pour éviter d'avoir une erreur "< ou > est un opérateur non supporté entre NoneType et int", on rajoute la condition "pieceValue(str(board.piece_at(i)))!=None"
    if pieceValue(str(board.piece_at(i)))!=None and pieceValue(str(board.piece_at(i)))<0:
      blackScore += 10*pieceValue(str(board.piece_at(i)))-moves
    if pieceValue(str(board.piece_at(i)))!=None and pieceValue(str(board.piece_at(i)))>0:
      whiteScore += 10*pieceValue(str(board.piece_at(i)))+moves
  return blackScore+whiteScore
#si le résultat obtenu est>0 alors les blancs ont l'avantage et si il est<0 alors les noirs ont l'avantage

