import chess
import math
import chess.polyglot
import chess.pgn as pgn
import Fonctions as fct
import Ouvertures as o

board = chess.Board()
print('---BIENVENUE DANS POLYCHESS IA VS IA---\n')
print(board, '\n')
#variable permettant de déterminer à qui le tour
tour = 0

#on fixe la profondeur à 3 pour que l'éxecution de la fonction alphaBeta ne soit pas trop longue
profondeur = 3

#donner un nom pour la sauvegarde
nom_sauv = str(input('Comment voulez-vous nommer cette magnifique partie ? '))

print('\n')
print("--------START--------\n")
game = pgn.Game()

while not(board.is_game_over()):
    cap = True
    if tour % 2 == 0:
        moves = board.legal_moves
        maximum = 0
        for move in moves :
            for deplacement in o.polyOuverture(board): 
                if move == deplacement[0]:
                    if maximum < deplacement[1]:
                        maximum = deplacement[1]
                        mouvement = deplacement[0]
                    cap = False
        if cap:
            mouvement = fct.alphaBeta(board, profondeur, -math.inf, math.inf)[1]
            
        valide = False
        while not valide:
            
            try:
                board.push(chess.Move.from_uci(str(mouvement)))
                print(board, '\n')
                valide = True
                
            except (ValueError):
                print('try again')
            except (TypeError):
                print('try again')
        
    else:
        moves = board.legal_moves
        maximum = 0
        for move in moves :
            for deplacement in o.polyOuverture(board): 
                if move == deplacement[0]:
                    if maximum < deplacement[1]:
                        maximum = deplacement[1]
                        mouvement = deplacement[0]
                    cap = False
                    
        if cap:
            mouvement = fct.alphaBeta(board, profondeur, -math.inf, math.inf)[1]
            
        valide = False
        while not valide:
            
            try:
                board.push(chess.Move.from_uci(str(mouvement)))
                print(board, '\n')
                valide = True
                
            except (ValueError):
                print('try again')
            except (TypeError):
                print('try again')
                    
    tour += 1
      
    # condition partie terminée
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
        
    # sauvegarde au format pgn
    new_pgn = open(nom_sauv,'w')
    export = pgn.FileExporter(new_pgn)
    game.accept(export)
