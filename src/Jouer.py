
class Partie:
  
  def __init__(self, board):
    self.board=board
   
  def get_move(self, legal_moves):
    
        position_initiale = input("Quelle pièce voulez-vous déplacer? ")
        position_finale = input("Jusqu'à où BG? ")
        while chess.Move.from_uci(pos_init + pos_fin) not in legal_moves:
            print("Non pas comme ça BG")
            position_initiale = input("Quelle pièce voulez-vous déplacer? ")
            position_finale = input("usqu'à où BG? ")

        return position_initiale + position_finale
    
  def start(self):

        while not self.board.is_checkmate():
          print(self.board)
          move = self.get_move(self.get_legal_move(self.color), self.board)
          self.move_piece(move)
          
