
class Partie:
  
  def __init__(self, board):
    self.board=board
    
  def start(self):

        while not self.board.is_checkmate():
          print(self.board)
          move = self.get_move(self.get_legal_move(self.color), self.board)
          self.move_piece(move)
          
