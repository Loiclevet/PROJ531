import chess

#---> D'abord, on crée une fonction qui nous renvoie la valeur d'une pièce pour pouvoir réutiliser cette fonction dans l'évaluation du score
def get_pieceValue(piece):
  if piece == None:
    return 0
  elif piece == 'p' or piece == 'P':
    return 1
  elif piece == 'n' or piece == 'N':
    return 3
  elif piece == 'b' or piece == 'B':
    return 3
  elif piece == 'r' or piece == 'R':
    return 5
  elif piece == 'q' or piece == 'Q':
    return 9
  elif piece == 'k' or piece == 'K':
    return 'Illimité'
 
