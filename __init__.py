#on importe le module chess pour avoir accès aux fonctionnalités d'un moteur de jeux d'échecs
import chess

#représentation de l'échiquier
board=chess.Board()
print(board)

#génération des coups légaux
def polyglot(board):
  #trouve toutes les entrées pour la position de départ
  with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:
    for entry in reader.find_all(board):
      print(entry.move, entry.weight, entry.learn)
