

import tkinter as tk

from time import sleep
from random import randint

class Dialog:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        tk.Label(self.top, text = 'You want to Play 1 Player or 2 Players?').pack()
        self.ps1 = tk.Button(self.top, text='1 Player', command = self.players_1)
        self.ps2 = tk.Button(self.top, text='2 Players', command = self.players_2)
        self.ps1.pack()
        self.ps2.pack()

    def players_1(self):
        self.choice = False
        self.top.destroy()

    def players_2(self):
        self.choice = True
        self.top.destroy()

class Board:
    def __init__(self):
        self.fields = [[-1]*3 for _ in range(3)]

    def hasWon(self, value):
        print('player=', value, ' : ', self.fields)
        for i in range(3):
            flag = 0
            for j in range(3):
                if self.fields[i][j] == value:
                    flag += 1
            if flag == 3:
                return True
            flag = 0
            for j in range(3):
                if self.fields[j][i] == value:
                    flag += 1
            if flag == 3:
                return True
            
        flag = 0
        for j in range(3):
            if self.fields[j][j] == value:
                flag += 1
        if flag == 3:
            return True

        flag = 0
        for j in range(3):
            for i in range(3):
                if (i == 2 and j == 0) or (j == 1 and i == 1) or (j==2 and i == 0):
                    if self.fields[j][i] == value:
                        flag += 1

        if flag == 3:
            return True
        return False

    def findZ(x, y):
        z = 0
        for i in range(3):
            for j in range(3):
                if i == x and y == j:
                    return z
                z += 1
    

class Main_Window:
    def __init__(self):
        self.app = tk.Tk()
        self.app.wm_title('Tic-Tac-Toe')
        self.app.geometry('250x400')
        self.board = Board()
        self.spaces = []
        self.number_players = tk.StringVar()
        tk.Label(self.app, textvariable=self.number_players).pack()
        self.user = tk.StringVar()
        self.playerPlaying = tk.Label(self.app, textvariable=self.user)
        self.playerPlaying.place(x=50, y=50, width=100, height = 30)
        self.spaceFills = [self.spaceFill0, self.spaceFill1, self.spaceFill2, self.spaceFill3, self.spaceFill4, self.spaceFill5, self.spaceFill6, self.spaceFill7, self.spaceFill8]

        for i in range(9):
            self.spaces.append(tk.Button(self.app, text=' ', command=self.spaceFills[i]))

        y = 100
        k = 0
        for j in range(3):
            x = 40
            for i in range(3):
                self.spaces[k].place(x=x, y=y, width=50, height = 50)
                x += 60
                k += 1
            y+= 60

        self.disable_all()
        self.result = tk.StringVar()
        self.resultLabel = tk.Label(self.app, textvariable=self.result)
        self.resultLabel.place(x=50, y=300, width=100, height = 30)

        self.count = 0
        self.player = 1

        self.restart_btn = tk.Button(self.app, text='Start', command=self.restart)
        self.restart_btn.place(x=40, y = 350, width = 60, height=40)

        self.reset_btn = tk.Button(self.app, text='Reset', command=self.reset_all)
        
        
    def player_decide(self):
        self.dialog = Dialog(self.app)
        self.app.wait_window(self.dialog.top)
        self.flag_2_players = self.dialog.choice

    def restart(self):
        self.player_decide()
        self.restart_btn['text'] = 'Restart'
        self.reset_btn.place(x=140, y = 350, width=60, height = 40)
        if self.flag_2_players:
            self.number_players.set('2 players tic tac toe')
        else:
            self.number_players.set('1 player tic tac toe')

        self.reset_all()
            
                
    def spaceFill(self, x, y, z):
        self.spaces[z]["text"] = 'X' if self.player else 'O'
        self.board.fields[x][y] = self.player
        self.spaces[z].config(state='disabled')
        if self.board.hasWon(self.player):
            print('won by',self.player)
            self.win(self.player)
            return
        self.player ^= 1
        self.count += 1
        if (not self.flag_2_players) and (not self.player):
            self.bot()
        else:
            self.play()
        
    def spaceFill0(self):
        self.spaceFill(0, 0, 0)
        
    def spaceFill1(self):
        self.spaceFill(0, 1, 1)
        
    def spaceFill2(self):
        self.spaceFill(0, 2, 2)
        
    def spaceFill3(self):
        self.spaceFill(1, 0, 3)
        
    def spaceFill4(self):
        self.spaceFill(1, 1, 4)
        
    def spaceFill5(self):
        self.spaceFill(1, 2, 5)
        
    def spaceFill6(self):
        self.spaceFill(2, 0, 6)
        
    def spaceFill7(self):
        self.spaceFill(2, 1, 7)
        
    def spaceFill8(self):
        self.spaceFill(2, 2, 8)
        
    def playerPlayShow(self):
        if self.flag_2_players:        
            if self.player:
                self.user.set('Player 1\'s Turn')
            else:
                self.user.set('Player 2\'s Turn')

        else:
            if self.player:
                self.user.set('Player\'s Turn')
            else:
                self.user.set('CPU\'s Turn')
    
    def play(self):
        if self.count < 9:
            self.playerPlayShow()
        else:
            self.tie()

    def reset_all(self):
        for i in range(9):
            self.spaces[i].config(state = 'active')
            self.spaces[i]['text'] = ' '
            
        self.board.fields = [[-1]*3 for _ in range(3)]
        self.player = 1
        self.result.set(' ')
        self.count = 0
        self.play()
        if not self.flag_2_players:
            self.moves = []
        
    def disable_all(self):
        for x in range(9):
            self.spaces[x].config(state='disabled')

    def win(self, player_won):
        if self.flag_2_players:
            if player_won:
                ans = "Player 1 won"
            else:
                ans = "Player 2 won"
        else:
            if player_won:
                ans = "Player won"
            else:
                ans = "CPU won"
                
        self.result.set(ans)
        self.disable_all()

    def tie(self):
        self.result.set('Game Tie')


    def bot(self):
        
        matrix = self.board.fields
        player = 1
        cpu = 0
        def is_winning(value):            
            for i in range(3):
                flag = 0
                x = -1
                y = -1
                for j in range(3):
                    if matrix[i][j] == value:
                        flag += 1
                    else:
                        x = i
                        y = j
                if flag == 2 and matrix[x][y] == -1 and (x, y) not in self.moves:
                    self.moves.append((x, y))
                    return True, x, y
                
                flag = 0
                x = -1
                y = -1
                for j in range(3):
                    if matrix[j][i] == value:
                        flag += 1
                    else:
                        x = j
                        y = i
                if flag == 2 and matrix[x][y] == -1 and (x, y) not in self.moves:
                    self.moves.append((x, y))
                    return True, x, y
            
            flag = 0
            x = -1
            y = -1
            for j in range(3):
                if matrix[j][j] == value:
                    flag += 1
                else:
                    x = j
                    y = j
            if flag == 2 and matrix[x][y] == -1 and (x, y) not in self.moves:
                self.moves.append((x, y))
                return True, x, y

            flag = 0
            x = -1
            y = -1
            for j in range(3):
                for i in range(3):
                    if (i == 2 and j == 0) or (j == 1 and i == 1) or (j==2 and i == 0):
                        if matrix[j][i] == value:
                            flag += 1
                        else:
                            x = j
                            y = i

            if flag == 2 and matrix[x][y] == -1 and (x, y) not in self.moves:
                self.moves.append((x, y))
                return True, x, y

            return False, None, None


        isBotWin, x, y = is_winning(cpu)
        
        if not isBotWin:
            isPlayerWin, x, y = is_winning(player)
            if not isPlayerWin:
                def chance():
                    print('In chance')
                    for i in range(3):
                        for j in range(3):
                            if matrix[i][j] == cpu:
                                if j == 0:
                                    if matrix[i][j+1] == -1 and matrix[i][j+2] == -1:
                                        li = [j+1, j+2]
                                        return i, li[randint(0, 1)]
                                if j == 1:
                                    if matrix[i][j+1] == -1 and matrix[i][j-1] == -1:
                                        li = [j-1, j+1]
                                        return i, li[randint(0, 1)]
                                if j == 2:
                                    if matrix[i][j-2] == -1 and matrix[i][j-1] == -1:
                                        li = [j-2, j-1]
                                        return i, li[randint(0, 1)]
                        for j in range(3):
                            if matrix[j][i] == cpu:
                                if j == 0:
                                    if matrix[j+1][i] == -1 and matrix[j+2][i] == -1:
                                        li = [j+1, j+2]
                                        return li[randint(0, 1)], i
                                if j == 1:
                                    if matrix[j+1][i] == -1 and matrix[j-1][i] == -1:
                                        li = [j-1, j+1]
                                        return li[randint(0, 1)], i
                                if j == 2:
                                    if matrix[j-2][i] == -1 and matrix[j-1][i] == -1:
                                        li = [j-2, j-1]
                                        return li[randint(0, 1)], i

                    for j in range(3):
                        if matrix[j][j] == cpu:
                            if j == 0:
                                if matrix[j+1][j+1] == -1 and matrix[j+2][j+2] == -1:
                                    li = [j+1, j+2]
                                    a = li[randint(0, 1)]
                                    return a, a
                            if j == 1:
                                if matrix[j+1][j+1] == -1 and matrix[j-1][j-1] == -1:
                                    a = li[randint(0, 1)]
                                    return a, a
                            if j == 2:
                                if matrix[j-2][j-2] == -1 and matrix[j-1][j-1] == -1:
                                    a = li[randint(0, 1)]
                                    return a, a
                    
                    for j in range(3):
                        for i in range(3):
                            if (i == 2 and j == 0) or (j == 1 and i == 1) or (j==2 and i == 0):
                                if matrix[j][i] == cpu:
                                    if i == 2 and j == 0:
                                        l = [(1, 1), (2, 0)]
                                        for i in l:
                                            if matrix[i[0]][i[1]] == -1:
                                                return i
                                    if i == 1 and j == 1:
                                        l = [(0, 2), (2, 0)]
                                        for i in l:
                                            if matrix[i[0]][i[1]] == -1:
                                                return i

                                    if i == 0 and j == 2:
                                        l = [(0, 2), (1, 1)]
                                        for i in l:
                                            if matrix[i[0]][i[1]] == -1:
                                                return i
                    return None, None
                    
                def try1():
                    print('in Try1')
                    for i in range(3):
                        flag = 0
                        l = []
                        for j in range(3):
                            if matrix[i][j] == -1:
                                flag += 1
                                l.append((i, j))
                        if flag == 3:
                            return l[randint(0, 2)]
                        
                        flag = 0
                        l = []
                        for j in range(3):
                            if matrix[j][i] == -1:
                                flag += 1
                                l.append((j, i))
                        if flag == 3:
                            return l[randint(0, 2)]
                        
                    flag = 0
                    l = []
                    for j in range(3):
                        if matrix[j][j] == -1:
                            flag += 1
                            l.append((j, j))
                    if flag == 3:
                        return l[randint(0, 2)]

                    flag = 0
                    l = []
                    for j in range(3):
                        for i in range(3):
                            if (i == 2 and j == 0) or (j == 1 and i == 1) or (j==2 and i == 0):
                                if matrix[j][i] == -1:
                                    flag += 1
                                    l.append((i, j))
                    if flag == 3:
                        return l[randint(0, 2)]

                    return None, None;

                def try2():
                    y1, y2 = chance()
                    if not y1:
                        y1, y2 = try1()
                        if not y1:
                            movesLeft = []
                            for i in range(3):
                                for j in range(3):
                                    if matrix[i][j] == -1:
                                        movesLeft.append((i, j))

                            return movesLeft[randint(0, len(movesLeft)-1)]
                        
                        return y1, y2

                    return y1, y2

                x, y = try2()

                
            if (x, y) not in self.moves:
                self.moves.append((x, y))

        z = Board.findZ(x, y)

        self.play()
        sleep(0.5)
        print('x=%d, y=%d, z=%d'%(x, y, z))
        print('self.moves: ', self.moves)
        self.spaceFill(x, y, z)

        
    
def main():
    Main_Window().app.mainloop()
    

if __name__ == '__main__':
    main()
