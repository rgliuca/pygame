import pygame
import time

pygame.init()

class Tile2048:
	COLORS = { 0: (205, 193, 180),
               2: (238, 228, 218),
               4: (237, 224, 200),
               8: (242, 177, 121),
               16: (245, 149, 99),
               32: (246, 124, 96),
               64: (246, 94, 59),
               128: (237, 207, 115),
               256: (237, 204, 98),
               512: (237, 200, 80),
               1024: (237, 197, 63),
               2048: (237, 194, 45) }
	
	TILE_SIZE = 100

	FONT = pygame.font.SysFont('Clear Sans', TILE_SIZE // 100 * 50)

	'''
	This class is responsible for the display
	'''
	def __init__(self, value, position, display):
		'''
		initializes a tile based on its value
		automatically figures out font size and color
		'''	
		# calling the value.setter becuase need to set the tile color
		self._display = display
		self._x = position[0]
		self._y = position[1]
		self.value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		self._value = new_value
		self._update_tile_color()
		self._update_text_size()
		self._rasterize()
	
	@property
	def color(self):
		return self._color

	def _update_tile_color(self):
		pass

	def _update_text_size(self):
		# needed to support different font size depending on 
		# value
		pass

	def rasterize(self):
		# screen is pygame display (screen)
		# position is a tuple of (x, y) cartesian position within
		# the screen
		pass

class Board2048:
	'''
	This class manages the entire 4x4 2048 board.  It maintains the values in the
	board as well as the display of the board
	'''
	BKGROUND_COLOR = (255, 255, 255) # set board boackground color to white
	TILE_OFFSET = Tile2048.TILE_SIZE // 10
	DISPLAY_OFFSET = 50
	NCOLS = 4
	NROWS = 4

	def __init__(self, 
		tile_size=Tile2048.TILE_SIZE, 
		tile_offset=TILE_OFFSET,
		display_offest=DISPLAY_OFFSET):
		# let's compute the board size using tile_size and tile_offset
		pass


	def reset(self):
		'''
		resets the game board: clears all cells and seed the first two random cells
		'''

	def _place_new_value(self):
		pass

	def _shift_cells(self, cell_list):
		# always shifts cell_list to the left (towards 0 index)
		# there are 4 elements, may have element with 0 value (
		# empty cells)  
		# 1. remove the 0 value cells (clear the spaces)
		# 2. shift cell_list to the left
		#       i. if len(cell_list)>1 then start with the 0 element and
		#           check if neighbors are the same and combine
		#       ii. move on to the next elements to check for neighbors
		#           to combine.  At most, there are only two combinations
		# 3. add in the correct number of 0 (empty spaces) to the right
		#   to make the final length = 4
		# returns True/False if cells shifted 
		orig_list = cell_list.copy()
		while 0 in cell_list:
			cell_list.remove(0)

		i = 0
		while i + 1 < len(cell_list):
			if cell_list[i] == cell_list[i + 1]:
				cell_list[i] *= 2
				cell_list.pop(i + 1)
			i += 1
				
		cell_list += [0] * (4 - len(cell_list))
		return not orig_list == cell_list

	def shift_up(self):
		pass

	def shift_down(self):
		pass

	def shift_left(self):
		pass

	def shift_right(self):
		pass

class Game2048:
	'''
	This class manages the playing of the game
	Creates 
		1. Board2048
		2. pygame initialization

	Exposes play() method which will return when the game ends

	Can restart() after play() returns

	'''

	pass

def main():
	display = pygame.display.set_mode((500, 300))
	for value in [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
		tile = Tile2048(value)
		tile.rasterize(display, (100, 100))
		pygame.display.update()
		time.sleep(0.8)
	pygame.quit()

if __name__ == "__main__":
	main()


