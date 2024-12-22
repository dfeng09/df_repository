import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # 生成随机目标数字
        self.target = random.randint(1, 100)
        self.attempts = 0

        # 主界面布局
        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.info_label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)
        self.reset_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target:
                self.result_label.config(text="The number is higher.", fg="blue")
            elif guess > self.target:
                self.result_label.config(text="The number is lower.", fg="blue")
            else:
                self.result_label.config(
                    text=f"Congratulations! You got it in {self.attempts} attempts!", fg="green"
                )
                self.submit_button.config(state=tk.DISABLED)
                self.reset_button.config(state=tk.NORMAL)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter an integer.", fg="red")

    def reset_game(self):
        # 重置游戏状态
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="", fg="blue")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

# 主程序入口
if __name__ == '__main__':
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # 生成随机目标数字
        self.target = random.randint(1, 100)
        self.attempts = 0

        # 主界面布局
        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.info_label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)
        self.reset_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target:
                self.result_label.config(text="The number is higher.", fg="blue")
            elif guess > self.target:
                self.result_label.config(text="The number is lower.", fg="blue")
            else:
                self.result_label.config(
                    text=f"Congratulations! You got it in {self.attempts} attempts!", fg="green"
                )
                self.submit_button.config(state=tk.DISABLED)
                self.reset_button.config(state=tk.NORMAL)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter an integer.", fg="red")

    def reset_game(self):
        # 重置游戏状态
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="", fg="blue")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

# 主程序入口
if __name__ == '__main__':
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
