import chess
import chess.polyglot
import chess.pgn
import Fonctions.py as fct

board=chess.Board()

def bouger_piece():
  position_initiale = input("Quelle pièce voulez-vous déplacer? ")
  position_finale = input("Jusqu'à où BG? ")
  while chess.Move.from_uci(position_initiale + position_finale) not in board.legal_moves:
    print("Non pas comme ça BG")
    position_initiale = input("Quelle pièce voulez-vous déplacer? ")
    position_finale = input("Jusqu'à où BG? ")
  move=position_initiale+position_finale
  board.push_uci(move)

while not(board.is_game_over()):
  pass
