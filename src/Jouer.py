
class Partie:
  
  def __init__(self, board, color):
    self.board=board
    self.color=color
    
  def bouger_piece(self, move):
        self.board.push_uci(move)
   
  def get_move(self, legal_moves):
    position_initiale = input("Quelle pièce voulez-vous déplacer? ")
    position_finale = input("Jusqu'à où BG? ")
    while chess.Move.from_uci(position_initiale + position_finale) not in legal_moves:
      print("Non pas comme ça BG")
      position_initiale = input("Quelle pièce voulez-vous déplacer? ")
      position_finale = input("usqu'à où BG? ")
      
    return position_initiale + position_finale
      
  def get_legal_move(self):
    moves=[]
    for move in self.board.legal_moves:
      moves.append(move)
    return moves
    
  def start(self):

        while not self.board.is_checkmate():
          print(self.board)
          move = self.get_move(self.get_legal_move())
          self.bouger_piece(move)
          
