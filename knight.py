#The Knight's tour
#Getting from a1 to h8
#Only touching ever square once
#Stephen Duncanson

# 8
# 7 
# 6 
# 5 
# 4 
# 3 
# 2 
# 1
# 0 1 2 3 4 5 6 7 8
# a b c d e f g h 

#move counter, for the while loop
#there are 64 squares on a chess board, so while moves is >= 64
#not every square has been visited
counter = 0

#Set the restraints on moves
board_range = range(9)

#possible moves
possible_moves = []

#Setting the original position at (0,0)
X_POS = 0
Y_POS = 0


#Move list - there are 8 moves a knight can make.
move1 = [X_POS + 1,Y_POS + 2]
move2 = [X_POS + 2,Y_POS + 1]
move3 = [X_POS + 2,Y_POS - 1]
move4 = [X_POS + 1,Y_POS - 2]
move5 = [X_POS - 1,Y_POS - 2]
move6 = [X_POS - 2,Y_POS - 1]
move7 = [X_POS - 2,Y_POS + 1]
move8 = [X_POS - 1,Y_POS + 2]

#moves += 1
#print(X_POS,Y_POS)


while counter < 10:
    if move1[0] in board_range and move1[1] in board_range:
        X_POS += move1[0]
        Y_POS += move1[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move2[0] in board_range and move2[1] in board_range:
        X_POS += move2[0]
        Y_POS += move2[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move3[0] in board_range and move3[1] in board_range:
        X_POS += move3[0]
        Y_POS += move3[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move4[0] in board_range and move4[1] in board_range:
        X_POS += move4[0]
        Y_POS += move4[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move5[0] in board_range and move5[1] in board_range:
        X_POS += move5[0]
        Y_POS += move5[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move6[0] in board_range and move6[1] in board_range:
        X_POS += move6[0]
        Y_POS += move6[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move7[0] in board_range and move7[1] in board_range:
        X_POS += move7[0]
        Y_POS += move7[1]
        counter += 1
        print(X_POS,Y_POS)
    elif move8[0] in board_range and move8[1] in board_range:
        X_POS += move8[0]
        Y_POS += move8[1]
        counter += 1
        print(X_POS,Y_POS)
    else:
        print("ERROR")

#while moves <= 64:
#    if Y_POS <= 4:
#        if X_POS > 1:
#            X_POS += move8[0]
#            Y_POS += move8[1]
#            moves + 1
#            print(X_POS,Y_POS)
#        elif X_POS < 1:
#            X_POS += move1[0]
#            Y_POS += move1[1]
#            moves + 1
#            print(X_POS,Y_POS)
#    elif Y_POS > 4:
#        if x > 1:
#            X_POS += move5[0]
#            Y_POS += move5[1]
#            moves + 1
#            print(X_POS,Y_POS)
#        elif x < 1:
#            X_POS += move4[0]
#            Y_POS += move4[1]
#            moves + 1
#            print(X_POS,Y_POS)
#    elif X_POS >= 4:
#        if Y_POS <= 4:
#            X_POS += move2[0]
#            Y_POS += move2[1]
#            moves + 1
#            print(X_POS,Y_POS)
#        elif Y_POS > 4:
#            X_POS += move3[0]
#            Y_POS += move3[1]
#            moves + 1
#            print(X_POS,Y_POS)
#    elif X_POS < 4:
#        if Y_POS >= 4:
#            X_POS += move6[0]
#            Y_POS += move6[1]
#            moves + 1
#            print(X_POS,Y_POS)
#        elif Y_POS < 4:
#            X_POS += move7[0]
#            Y_POS += move7[1]
#            moves + 1
#            print(X_POS,Y_POS)

