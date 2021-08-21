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


	def rotate_left(self):
		# rotates the block by 90 degrees left
		# and calls rasterize to display on the canvas
		pass

	def rotate_right(self):
		# rotates the block by 90 degrees right
		# and calls rasterize to display on the canvas
		pass

	def move_block_down(self):
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
	block = TetrisBlock((100, 0), disp, 0)

	block.rasterize()

	loop_delay = 0.05
	count = 0

	t1 = TetrisTile((10, 10), disp, (255,0,0))

	time.sleep(5)
	pygame.quit()
	quit()

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
		
