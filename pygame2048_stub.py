import pygame

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
	def __init__(self, value):
		'''
		initializes a tile based on its value
		automatically figures out font size and color
		'''	
		# calling the value.setter becuase need to set the tile color
		self.value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		self._value = new_value
		self._update_tile_color()
		self._update_text_font()
	
	@property
	def color(self):
		return self._color

	def _update_tile_color(self):
		# this method will change self._tile_color depending on the value
		pass

	def _update_text_font(self):
		# needed to support different font size depending on 
		# value 
		# this method will change self._text_font
		pass

	def rasterize(self, display, position):
		# screen is pygame display (screen)
		# position is a tuple of (x, y) cartesian position within
		# the screen
		# will use self.value, self._tile_color, self._text_font to display the tile on the screen (is passed in as a pygame display) at position
		pass

class Board2048:
	'''
	This class manages the entire 4x4 2048 board.  It maintains the values in the
	board as well as the display of the board
	'''
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
	import time
	display = pygame.display.set_mode((500, 300))
	for value in [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
		tile1 = Tile2048(value)
		tile1.rasterize(display, (100, 50))
		tile2 = Tile2048(value * 2)
		tile2.rasterize(display, (220, 50))

		tile3 = Tile2048(value * 2)
		tile4 = Tile2048(value)
		tile3.rasterize(display, (100, 150 + 20))
		tile4.rasterize(display, (220, 150 + 20))
		pygame.display.update()
		time.sleep(1.5)

if __name__ == "__main__":
	main()


