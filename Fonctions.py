import chess
import math

'''
D'abord, on crée une fonction pieceValue() pour donner des valeurs aux pièces car on en a besoin pour définir la fonction evaluation()
'''
def pieceValue(piece):
  if piece == None:
    return 0
  #pour une utilisation plus facile, on donne des valeurs négatives aux pions noirs(représentés par des minuscules) et positives aux pions blancs
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
La fonction evaluation() sert à donner une note au plateau, càd définir l'équipe qui a l'avantage, elle nous sera utile pour définir les méthodes minmax() et alphabeta()
méthode utilisée : 10*valeur de la pièce+nombre de déplacements possibles de la pièce(https://www.youtube.com/watch?v=gXywCc_KIMM)
'''
def evaluation(board):
  blackScore = 0  
  whiteScore = 0
  
  #on parcourt tout le plateau(il y a 64 cases et la première case est d'indice 0)
  for i in range(0,64):
    moves=0
    #pour chaque case, on détermine le nb de coups légaux possibles
    for move in board.legal_moves:
        moves+=1
    
    #pour éviter d'avoir une erreur "< ou > est un opérateur non supporté entre NoneType et int", on rajoute la condition "pieceValue(str(board.piece_at(i)))!=None"
    if pieceValue(str(board.piece_at(i)))!=None and pieceValue(str(board.piece_at(i)))<0:
      blackScore += 10*pieceValue(str(board.piece_at(i)))-moves
    if pieceValue(str(board.piece_at(i)))!=None and pieceValue(str(board.piece_at(i)))>0:
      whiteScore += 10*pieceValue(str(board.piece_at(i)))+moves
     
  return blackScore+whiteScore
#si le résultat obtenu est >0 alors les blancs ont l'avantage, si =0 personne n'a l'avantage, si <0 alors les noirs ont l'avantage

'''
La fonction minimaxi() va tester toutes les possibilités d'une profondeur donnée, cette méthode va nous aider à définir le meilleur coup possible.
En effet, elle renvoie un tuple composé de l'évaluation du plateau et du meilleur coup à jouer.
méthode utilisée : https://fr.wikipedia.org/wiki/Algorithme_minimax#Pseudocode
'''
def minimaxi(board, depth, maximizingPlayer):
    possibleMoves = board.legal_moves
    bestMove = None
    
    if depth == 0 :
        return evaluation(board), bestMove
    
    if maximizingPlayer:
        v = -math.inf
        for move in possibleMoves:
            
            deplacement = chess.Move.from_uci(str(move))
            
            #fait le déplacement et met à jour l'échiquier
            board.push(deplacement)
            v2, current_move = minimaxi(board, depth-1, False)
            #annule le dernier déplacement
            board.pop()
            
            if(v2 > v or not bestMove):
                v = v2
                bestMove = move
                
    else:
        v = math.inf
        for move in possibleMoves:
            
            deplacement = chess.Move.from_uci(str(move))
            
            #fait le déplacement et met à jour l'échiquier
            board.push(deplacement)
            v2,current_move = minimaxi(board, depth-1, True)
            #annule le dernier déplacement
            board.pop()
            
            if(v2 < v or not bestMove):
                v = v2
                bestMove = move
                
    return v, bestMove

'''
La fonction alphaBeta() est une sorte d'amélioration de la fonction minimaxi() car elle passe par moins de "branches" que minimaxi().
méthode utilisée : https://fr.wikipedia.org/wiki/%C3%89lagage_alpha-b%C3%AAta#Pseudocode
'''
def alphaBeta(board, depth, alpha, beta):
    possibleMoves = board.legal_moves
    bestMove = None

    if depth == 0:
        return evaluation(board),bestMove

    if (not board.turn):
        v = 0
        for move in possibleMoves:
            deplacement = chess.Move.from_uci(str(move))
            
            #fait le déplacement et met à jour l'échiquier
            board.push(deplacement)
            v2, current_move = alphaBeta(board, depth-1, alpha, beta)
            #annule le dernier déplacement
            board.pop()

            if(v2 < v or not bestMove):
                v = v2
                bestMove = move

            if(v <= beta):
                return beta, bestMove

            if(v < alpha):
                alpha = v

        return alpha, bestMove
        
    else:
        v = 0
        for move in possibleMoves:
            deplacement = chess.Move.from_uci(str(move))
            
            #fait le déplacement et met à jour l'échiquier
            board.push(deplacement)
            v2,current_move = alphaBeta(board, depth-1, alpha, beta)
            #annule le dernier déplacement
            board.pop()

            if(v2 < v or not bestMove):
                v = v2
                bestMove = move

            if(v >= alpha):
                return alpha, bestMove

            if(v > beta):
                beta = v
            
        return beta, bestMove
