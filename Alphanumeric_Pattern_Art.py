# Problem Statement:-->

'''Write python code which takes an alphanumeric string as an argument and prints it as an art which is a combination of ‘#’'''

# Solution code-->

import os
import sys

def PatternArt(string):
    '''
    PatternArt() takes Alphanumeric string([A-z][0-9]) as agrument and returns
    corresponding alphanumeric character in Artistic form.
    '''
    # Appending all pattern Alphabets and digits in empty list named `Alphanumeric_strings`
    Alphanumeric_Strings = [] 

    for i in range(len(string)):
        '''creating '#' pattern for every single Alphabets and Digits'''
        
        # For A:
        if string[i]=='A':
            print_A = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (((col == 0 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 5))):
                        print_A[row][col] = "#"
            Alphanumeric_Strings.append(print_A)

        # for B:
        elif string[i]=='B':
            print_B = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==5 and row!=0 and row!=3 and row!=6) or (row==0 or row==3 or row==6) and (col>0 and col<5):
                        print_B[row][col] = "#"
            Alphanumeric_Strings.append(print_B)

        # for C:
        elif string[i]=='C':
            print_C = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and row!=0 and row!=6) or ((row==0 or row==6) and (col>0)):
                        print_C[row][col] = "#"
            Alphanumeric_Strings.append(print_C)

        # for D:
        elif string[i]=='D':
            print_D = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or (col==5 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<5)):
                        print_D[row][col] = "#"
            Alphanumeric_Strings.append(print_D)

        # for E:
        elif string[i]=='E':
            print_E = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or ((row==0 or row==6) and (col>0)) or (row==3 and col<4):
                        print_E[row][col] = "#"
            Alphanumeric_Strings.append(print_E)

        # for F:
        elif string[i]=='F':
            print_F = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0) or ((row==0 or row==3) and (col>0)):
                        print_F[row][col] = "#"
            Alphanumeric_Strings.append(print_F)

        # for G:
        elif string[i]=='G':
            print_G = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=0 and row!=6)) or (col==5 and (row!=0 and row!=2 and row!=6)) or((row==0 or row==6) and (col>0 and col<5)) or ((row==3 and col==3) or (row==3 and col==4)):
                        print_G[row][col] = "#"
            Alphanumeric_Strings.append(print_G)

        # for H:
        elif string[i]=='H':
            print_H = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 or col==5) or (row==3 and (col>0 and col<5)):
                        print_H[row][col] = "#"
            Alphanumeric_Strings.append(print_H)    
        
        # for I:
        elif string[i]=='I':
            print_I = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==2 or ((row==0 or row==6) and col!=2):
                        print_I[row][col] = "#"
            Alphanumeric_Strings.append(print_I)

        # for J:
        elif string[i]=='J':
            print_J = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==3 or (row==0 and col!=3) or (row==6 and col<3) or (row==5 and col==0):
                        print_J[row][col] = "#"
            Alphanumeric_Strings.append(print_J)

        # for K:
        elif string[i]=='K':
            print_K = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or row + col==3 or row-col==3:
                        print_K[row][col] = "#"
            Alphanumeric_Strings.append(print_K)

        # for L:
        elif string[i]=='L':
            print_L = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or (row==6 and col>0):
                        print_L[row][col] = "#"
            Alphanumeric_Strings.append(print_L)

        # for M:
        elif string[i]=='M':
            print_M = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                   if (col==1 or col==5 or (row==2 and (col==2 or col==4)) or (row==3 and col==3)):
                        print_M[row][col] = "#"
            Alphanumeric_Strings.append(print_M)

        # for N:
        elif string[i]=='N':
            print_N = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                   if col==0 or col==5 or (row==col and (col>0 and col<5)):
                        print_N[row][col] = "#"
            Alphanumeric_Strings.append(print_N)
        
        # for O:
        elif string[i]=='O':
            print_O = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                   if (col==0 and (row!=0 and row!=6)) or (col==5 and (row!=0 and row!=6)) or  ((row==0 or row==6) and (col>0 and col<5)):
                       print_O[row][col] = "#"
            Alphanumeric_Strings.append(print_O)

        # for P:
        elif string[i]=='P':
            print_P = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                   if col==0 or col==5 and (row==1 or row==2) or ((row==0 or row==3) and (col>0 and col<5)):
                       print_P[row][col] = "#"
            Alphanumeric_Strings.append(print_P)

        # for Q:
        elif string[i]=='Q':
            print_Q = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=0 and row!=5 and row!=6)) or (col==5 and (row!=0 and row!=5)) or  ((row==0 or row==5) and (col>0 and col<5)) or (col==3 and row==4):
                       print_Q[row][col] = "#"
            Alphanumeric_Strings.append(print_Q)

        # for R:
        elif string[i]=='R':
            print_R = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or col==5 and (row==1 or row==2) or ((row==0 or row==3) and (col>0 and col<5)) or (col==5 and row>3):
                       print_R[row][col] = "#"
            Alphanumeric_Strings.append(print_R)

        # for S:
        elif string[i]=='S':
            print_S = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row==0 or row==3 or row==6) and (col>0 and col<5)) or (col==0 and (row>0 and row<3)) or (col==5 and (row>3 and row<6)) or ((row==1 and col==5) or (row==5 and col==0)):
                       print_S[row][col] = "#"
            Alphanumeric_Strings.append(print_S)

        # for T:
        elif string[i]=='T':
            print_T = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==2 or row==0:
                       print_T[row][col] = "#"
            Alphanumeric_Strings.append(print_T)

        # for U:
        elif string[i]=='U':
            print_U = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and row<6) or (row==6 and (col>0 and col<5)):
                       print_U[row][col] = "#"
            Alphanumeric_Strings.append(print_U)

        # for V:
        elif string[i]=='V':
            print_V = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (((col==1 or col==5) and row<5) or (row==6 and col==3) or (row==5 and (col==2 or col==4))):
                       print_V[row][col] = "#"
            Alphanumeric_Strings.append(print_V)

        # for W:
        elif string[i]=='W':
            print_W = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==1 or col==5 or (row==5 and (col==2 or col==4)) or (row==4 and col==3)):
                       print_W[row][col] = "#"
            Alphanumeric_Strings.append(print_W)

        # for X:
        elif string[i]=='X':
            print_X = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (((col==1 or col==5) and (row>4 or row<2)) or row==col and col>0 and col<6 or (col==2 and row==4) or (col==4 and row==2)):
                       print_X[row][col] = "#"
            Alphanumeric_Strings.append(print_X)

        # for Y:
        elif string[i]=='Y':
            print_Y = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (((col==1 or col==5) and row<2) or row==col and col>0 and col<4 or (col==4 and row==2) or ((col==3) and row>3)):
                       print_Y[row][col] = "#"
            Alphanumeric_Strings.append(print_Y)

        # for Z:
        elif string[i]=='Z':
            print_Z = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row==0 or row==6) and (col>=0 and col<=5) or row+col==5):
                       print_Z[row][col] = "#"
            Alphanumeric_Strings.append(print_Z)

        # for digit 0:
        elif string[i]=='0':
            print_0 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=0 and row!=6)) or (col==5 and (row!=0 and row!=6)) or  ((row==0 or row==6) and (col>0 and col<5)) or (row==col and col>0 and col<6):
                       print_0[row][col] = "#"
            Alphanumeric_Strings.append(print_0)

        # for digit 1:
        elif string[i]=='1':
            print_1 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==2 or row==6 or (col==1 and row==1):
                       print_1[row][col] = "#"
            Alphanumeric_Strings.append(print_1)

        # for 2:
        elif string[i]=='2':
            print_2 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row==0 or row==3) and (col>0 and col<5)) or (col==5 and (row>0 and row<3)) or (col==0 and (row>3 and row<6)) or (row==6 and col>0) or (row==1 and col==0):
                       print_2[row][col] = "#"
            Alphanumeric_Strings.append(print_2)

        # for 3:
        elif string[i]=='3':
            print_3 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row==0 or row==3 or row==6) and (col>0 and col<5)) or (col==5 and (row>0 and row<3)) or (col==5 and (row>3 and row<6)):
                       print_3[row][col] = "#"
            Alphanumeric_Strings.append(print_3)

        # for 4:
        elif string[i]=='4':
            print_4 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==3 or row==4) or ((row==1 and col==2)  or (row==2 and col==1) or (col==0 and row==3)):
                       print_4[row][col] = "#"
            Alphanumeric_Strings.append(print_4)

        # for 5:
        elif string[i]=='5':
            print_5 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if row==0 or (col==0 and (row<3)) or  (row==2 and col!=5) or (col==5 and (row>2 and row<6)) or (row==6 and col!=5):
                       print_5[row][col] = "#"
            Alphanumeric_Strings.append(print_5)

        # for 6:
        elif string[i]=='6':
            print_6 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 and (row>0 and row<6)) or (row==0 and (col>0 and col<4)) or (row==3 and (col>0 and col<4)) or (row==6 and (col>0 and col<4)) or (col==4 and (row>3 and row<6)) or (row==1 and col==4):
                       print_6[row][col] = "#"
            Alphanumeric_Strings.append(print_6)

        # for 7:
        elif string[i]=='7':
            print_7 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row==0) or (row==1 and col==5) or (row==2 and col==4) or (row==3 and col==3) or (row==4 and col==2) or (row==5 and col==1) or (row==6 and col==0):
                       print_7[row][col] = "#"
            Alphanumeric_Strings.append(print_7)

        # for 8:
        elif string[i]=='8':
            print_8 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row>0 and row<3)) or (col==0 and (row>3 and row<6)) or (col==5 and row!=0 and row!=3 and row!=6) or ((row==0 or row==3 or row==6) and (col>0 and col<5)):
                       print_8[row][col] = "#"
            Alphanumeric_Strings.append(print_8)

        # for 9:
        elif string[i]=='9':
            print_9 = [[' ' for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row==6 and (col>0 and col<5)) or (row==5 and col==0) or (row==3 and col>0) or (row==0 and (col>0 and col<5)) or ((col==0 or col==5) and (row>0 and row<3)) or (col==5 and (row>3 and row<6)):
                       print_9[row][col] = "#"
            Alphanumeric_Strings.append(print_9)

        else:
            print("invalid_input")

    return Alphanumeric_Strings


if __name__ == "__main__":

    number_of_arguments = len(sys.argv)

    if (number_of_arguments < 2):
        print("please enter alphanumric string as command line argument !!")
        sys.exit()

    user_input = sys.argv[1]
    user_input = user_input.upper()
    
    # Call our art function
    result = PatternArt(user_input)
    
    # Loop to print characters
    for i in range(7):
        for j in range(len(result)):
            for k in range(6):
                print(result[j][i][k], end=" ")
            print(end=" ")
        print()