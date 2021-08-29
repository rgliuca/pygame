from pygame_objects import *
import pygame
import copy
import time

class TetrisTile(Tile):
	TILE_SIZE = 50 

	def __init__(self, position, display, color):
		super().__init__(
			position, display, 
			__class__.TETRIS_TILE_SIZE, color)

class TetrisBlock:
	'''
	This is going to be a 4x4 block
	consisting of 16 tiles
	'''

	TILE_GAP = 5

	BLOCKS = [
        # block 0
        (
            [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]],
            (2, 117, 187)),

        # block 1
        (
            [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]],
            (53, 187, 238)),

        # block 2
        (
            [[1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],
            (3, 152, 137)),

        # block 3
        (
            [[0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],
            (240, 120, 52)),

        # block 4
        (
            [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
            (206, 50, 17)),

        # block 5
        (
            [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]],
            (239, 51, 120)),

        # block 6
        (
            [[1, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],
            (138, 32, 85))
	]

	def __init__(self, position, display, block_id=None):
		# if block_id is None, select a random block from
		# the list __class__.BLOCKS
		# otherwise, assign self._block_id = block id  
		# This is useful for debugging! 
		# self._block_id = block_id

		self._x, self._y = position
		self._display = display

		if block_id is None or \
			block_id < 0 or \
			block_id >= len(self.BLOCKS):
			raise ValueError

		self._block = copy.deepcopy(self.BLOCKS[block_id])
		self.rasterize()

	def rotate(self, surrounding_image):
		# rotates the block clockwise by 90 degrees 
		# and calls rasterize to display on the canvas
		pass

	def move_left(self, board):
		# moves the block to the left by one unit
		pass
	
	def move_right(self, board):
		# moves the block to the right by one unit
		pass

	def animate(self, board):
		# moves the block down by one unit in the y direction (animate)
		# and calls rasterize to display the block on the canvas
		pass

	def rasterize(self):
		# This method is going to take the display
		# and display this Tetris block at self._x, self._y

		# take self._block (the 2D list) and generate the TetrisBlock 
		# at self._x, self._y position

		# loop through self._block (image)
		pass

class TetrisBoard:
	HEIGHT = 20
	WIDHT = 10
	
	def __init__(self, position, display):
		# position is the canvas starting (x,y) to draw the board
		self._board = []  # a two dimensional matrix with WIDTH x HEIGHT, initialize every cell to 0
		self._display = display
		# drawo the Tetris Game Board based on the grid size WIDTH x HEIGHT and TILE_SIZE and TILE_GAP
		
		
	def spawn_new_block(self):
		# create a new block at the top of the screen and return the block variable
		# what position? (at the top of the screen!)
		# what id?  (select the id based on the random algorithm)
		new_block = TetrisBlock(position, display, id)
	
	
class TetrisGame:
	BKGROUND_COLOR = (255, 255, 255)

	def __init__(self, display):
		self._last_block_id = 0
		self._display = display
		self._dsplay.fill(TetrisGame.BKGROUND_COLOR)
		pygame.display.set_caption("TETRIS")

if __name__ == "__main__":
	canvas_height = 800
	canvas_width = 400
	disp = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)
	
	disp.fill(TetrisGame.BKGROUND_COLOR)

	t1 = TetrisTile((10, 10), disp, (255,0,0))

	time.sleep(5)
	pygame.quit()
	quit()
	
	loop_delay = 0.05
	count = 0
	block = TetrisBlock((100, 0), disp, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(pygame.mouse.get_pos())

			if event.type == pygame.K_LEFT:
				block.rotate_left()

		if count * loop_delay > 1:
			count = 0
			# clear the screen
			# call TetrisBlock's method to move the block down by one unit!

		count += 1
		time.sleep(loop_delay)
		
