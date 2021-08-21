import pygame

class Tile:
	TILE_SIZE = 100
	DEFAULT_COLOR = (255, 255, 255)

	'''
	This class is responsible for the display of a generic game tile
	'''
	def __init__(self, 
		position, display, 
		tile_size=None, color=None):
		'''
		initializes a tile 
		with a default color placed at position
		'''	
		# calling the value.setter becuase need to set the tile color
		self._display = display
		self._x, self._y = position
		self._color = __class__.DEFAULT_COLOR if color is None else color
		self._tile_size = __class__.TILE_SIZE if tile_size is None else tile_size

		self.rasterize()

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, new_color):
		self._color = new_color
		self.rasterize()

	def rasterize(self):
		# self._display is a pygame screen
		# will use self._x and self._y as the position
		pygame.draw.rect(self._display, self._color, 
			(self._x, self._y, self._tile_size, self._tile_size))

		pygame.display.update()

	
