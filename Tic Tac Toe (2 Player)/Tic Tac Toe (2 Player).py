import tkinter as tk
from tkinter import messagebox, simpledialog

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Tic Tac Toe - 2 Player")
        self.root.configure(bg="#eaf6f6")
        self.root.resizable(False, False)

        self.player1 = ""
        self.player2 = ""
        self.score = { "X": 0, "O": 0 }

        self.current_player = "X"
        self.game_over = False

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.get_player_names()
        self.create_widgets()

    def get_player_names(self):
        self.player1 = simpledialog.askstring("Player X", "Enter name for Player X:")
        self.player2 = simpledialog.askstring("Player O", "Enter name for Player O:")
        if not self.player1:
            self.player1 = "Player X"
        if not self.player2:
            self.player2 = "Player O"

    def create_widgets(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Comic Sans MS", 24, "bold"), bg="#eaf6f6", fg="#2f3542")
        title.pack(pady=10)

        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 14), bg="#eaf6f6", fg="#2f3542")
        self.score_label.pack()

        self.status_label = tk.Label(self.root, text=f"{self.player1}'s (X) turn", font=("Arial", 14), bg="#eaf6f6", fg="#2f3542")
        self.status_label.pack(pady=5)

        frame = tk.Frame(self.root, bg="#eaf6f6")
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=("Arial", 28), width=5, height=2,
                                bg="white", fg="#2f3542", 
                                command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

        controls = tk.Frame(self.root, bg="#eaf6f6")
        controls.pack(pady=10)

        tk.Button(controls, text="🔁 Restart", font=("Arial", 12), bg="#00b894", fg="white", command=self.reset_game).grid(row=0, column=0, padx=5)
        tk.Button(controls, text="🧹 Clear Score", font=("Arial", 12), bg="#d63031", fg="white", command=self.clear_scores).grid(row=0, column=1, padx=5)

    def get_score_text(self):
        return f"{self.player1} (X): {self.score['X']}   |   {self.player2} (O): {self.score['O']}"

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg="#e17055" if self.current_player == "X" else "#0984e3")

            if self.check_winner():
                winner_name = self.player1 if self.current_player == "X" else self.player2
                self.status_label.config(text=f"🎉 {winner_name} wins!")
                self.highlight_winner()
                messagebox.showinfo("Game Over", f"🎉 {winner_name} wins!")
                self.score[self.current_player] += 1
                self.score_label.config(text=self.get_score_text())
                self.game_over = True
            elif self.is_draw():
                self.status_label.config(text="😐 It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                next_player_name = self.player1 if self.current_player == "X" else self.player2
                self.status_label.config(text=f"{next_player_name}'s ({self.current_player}) turn")

    def check_winner(self):
        b = self.board
        self.winning_cells = []

        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                self.winning_cells = [(i, 0), (i, 1), (i, 2)]
                return True
            if b[0][i] == b[1][i] == b[2][i] != "":
                self.winning_cells = [(0, i), (1, i), (2, i)]
                return True

        if b[0][0] == b[1][1] == b[2][2] != "":
            self.winning_cells = [(0, 0), (1, 1), (2, 2)]
            return True
        if b[0][2] == b[1][1] == b[2][0] != "":
            self.winning_cells = [(0, 2), (1, 1), (2, 0)]
            return True

        return False

    def highlight_winner(self):
        for row, col in self.winning_cells:
            self.buttons[row][col].config(bg="#55efc4")

    def is_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.current_player = "X"
        self.status_label.config(text=f"{self.player1}'s (X) turn")

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg="white", fg="#2f3542")

    def clear_scores(self):
        self.score = {"X": 0, "O": 0}
        self.score_label.config(text=self.get_score_text())
        self.reset_game()


# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
