import chess
import chess.polyglot

'''
Cette fonction est utile pour la génération de toutes les ouvertures possibles
'''

def polyOuverture(board):
  ouverture=[]
  #trouve toutes les ouvertures possibles pour la position de départ
  with chess.polyglot.open_reader("bookOuvertures.bin") as reader:
    for entry in reader.find_all(board):
      ouverture.append((entry.move, entry.weight, entry.learn))
  return ouverture
