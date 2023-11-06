import tkinter as tk
import random

class MineSweeper:

	def __init__(self, master):
		self.master = master
		master.title('Campo Minato')
		master.resizable(False, False)

		self.score = 0
		self.create_top_frame()
		self.create_game_frame()
		self.create_bottom_frame()

		self.place_mines()

	def create_top_frame(self):
		self.top_frame = tk.Frame(self.master, bg='light blue')
		self.top_frame.pack(fill='x')

		self.score_label = tk.Label(self.top_frame, text='Punti:', bg='light blue')
		self.score_label.pack(side='left')

		self.score_value = tk.Label(self.top_frame, text=self.score, bg='light blue')
		self.score_value.pack(side='left')

	def create_game_frame(self):
		self.game_frame = tk.Frame(self.master)
		self.game_frame.pack()

		self.tiles = []
		for row in range(10):
			tile_row = []
			for col in range(10):
				tile = tk.Button(self.game_frame, width=2, bg='grey', relief='raised',
								 command=lambda r=row, c=col: self.click_tile(r, c))
				tile.grid(row=row, column=col)
				tile_row.append(tile)
			self.tiles.append(tile_row)

	def create_bottom_frame(self):
		self.bottom_frame = tk.Frame(self.master, bg='light blue')
		self.bottom_frame.pack(fill='x')

		self.exit_button = tk.Button(self.bottom_frame, text='ESCI', width=10, command=self.master.destroy)
		self.exit_button.pack(pady=10)

	def place_mines(self):
		self.mines = set()
		while len(self.mines) < 10:
			row = random.randint(0, 9)
			col = random.randint(0, 9)
			self.mines.add((row, col))

	def click_tile(self, row, col):
		tile = self.tiles[row][col]

		if (row, col) in self.mines:
			tile.config(bg='red', text='X', state='disabled')
			self.end_game()
		elif tile['bg'] == 'white':
			tile.config(bg='blue', text='O')
			self.score -= 1
			self.score_value.config(text=self.score)
		else:
			self.reveal_tile(row, col)
			self.score += 1
			self.score_value.config(text=self.score)
			self.check_win()

	def reveal_tile(self, row, col):
		if row < 0 or row > 9 or col < 0 or col > 9:
			return
		tile = self.tiles[row][col]
		if tile['state'] != 'normal':
			return
		mine_count = 0
		for r in range(row-1, row+2):
			for c in range(col-1, col+2):
				if r == row and c == col:
					continue
				if (r, c) in self.mines:
					mine_count += 1
		if mine_count == 0:
			tile.config(bg='white', state='disabled')
			for r in range(row-1, row+2):
				for c in range(col-1, col+2):
					if r == row and c == col:
						continue
					self.reveal_tile(r, c)
		else:
			tile.config(bg='white', text=mine_count, state='disabled')

	def end_game(self):
		for row in self.tiles:
			for tile in row:
				if (row, col) in self.mines:
					tile.config(bg='grey', text='*', state='disabled')
				else:
					tile.config(state='disabled')
		self.score_value.config(bg='green')

		self.rigioca_frame = tk.Frame(self.master, bg='white', width=200, height=100)
		self.rigioca_frame.place(x=250, y=250)

		self.rigioca_button = tk.Button(self.rigioca_frame, text='RIGIOCA', bg='purple', fg='white', width=10,
										command=self.restart_game)
		self.rigioca_button.pack(pady=20)

	def check_win(self):
		revealed_count = 0
		for row in self.tiles:
			for tile in row:
				if tile['bg'] == 'white':
					revealed_count += 1
		if revealed_count == 90:
			self.score_value.config(bg='green')
			self.rigioca_frame = tk.Frame(self.master, bg='white', width=200, height=100)
			self.rigioca_frame.place(x=250, y=250)

			self.rigioca_button = tk.Button(self.rigioca_frame, text='RIGIOCA', bg='purple', fg='white', width=10,
											command=self.restart_game)
			self.rigioca_button.pack(pady=20)

	def restart_game(self):
		self.master.destroy()
		root = tk.Tk()
		MineSweeper(root)
		root.mainloop()


root = tk.Tk()
MineSweeper(root)
root.mainloop()