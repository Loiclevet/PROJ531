import chess
import math
import chess.polyglot
import chess.pgn as pgn
import Fonctions as fct
import Ouvertures as o

board = chess.Board()
print('---BIENVENUE DANS LE MEILLEUR POLYCHESS---\n')
print(board, '\n')
#variable permettant de déterminer à qui le tour
tour = 0

#on fixe la profondeur à 3 pour que l'éxecution de la fonction alphaBeta ne soit pas trop longue
profondeur = 3

#donner un nom pour la sauvegarde
nom_sauv = str(input('Comment voulez-vous nommer cette magnifique partie ? '))

#pseudo des 2 joueurs
player_1 = str(input('Entrez votre pseudo Joueur 1 : '))
player_2 = str(input('Entrez votre pseudo Joueur 2 : '))

print('\n')
print("--------START--------\n")
game = pgn.Game()

while not(board.is_game_over()):
    cap = True
    if tour % 2 == 0:
        moves = board.legal_moves
        for move in moves :
            for deplacement in o.polyOuverture(board):
                if move == deplacement[0]:
                    cap = False
                    print(f"coup conseillé: {deplacement[0]}, poids: {deplacement[1]}")
        if cap:
            fct.alphaBeta(board, profondeur, -math.inf, math.inf)
        
        position_initiale = input(f"Quelle pièce voulez-vous déplacer {player_1} ? ")
        position_finale = input("Jusqu'à où BG1 ? ")
        while chess.Move.from_uci(position_initiale + position_finale) not in board.legal_moves:
          print("MOUVEMENT IMPOSSIBLE!")
          position_initiale = input(f"Quelle pièce voulez-vous déplacer {player_1} ? ")
          position_finale = input("Jusqu'à où BG1 ? ")
        bouger = position_initiale+position_finale
        board.push_uci(bouger)
        print(board, '\n')
        
    else:
        moves = board.legal_moves
        for move in moves :
            for deplacement in o.polyOuverture(board):
                if move == deplacement[0]:
                    cap = False
                    print(f"coup conseillé: {deplacement[0]}, poids: {deplacement[1]}")
        if cap:
            fct.alphaBeta(board, profondeur, -math.inf, math.inf)
        
        position_initiale = input(f"Quelle pièce voulez-vous déplacer {player_2} ? ")
        position_finale = input("Jusqu'à où BG2 ? ")
        while chess.Move.from_uci(position_initiale+position_finale) not in board.legal_moves:
          print("MOUVEMENT IMPOSSIBLE!")
          position_initiale = input(f"Quelle pièce voulez-vous déplacer {player_2} ? ")
          position_finale = input("Jusqu'à où BG2 ? ")
        bouger = position_initiale+position_finale
        board.push_uci(bouger)
        print(board, '\n')
        
    tour += 1
      
    # condition partie terminée
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
        
    # sauvegarde au format pgn
    new_pgn = open(nom_sauv,'w')
    export = pgn.FileExporter(new_pgn)
    game.accept(export)
        
        
