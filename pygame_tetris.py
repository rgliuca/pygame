from pygame_objects import *

class TetrisTile(Tile):
	TETRIS_TILE_SIZE = 50 

	def __init__(self, position, display, color):
		super().__init__(position, display)
		self._tile_size = __class__.TETRIS_TILE_SIZE
		self.color = color
		self.rasterize()

class TetrisBlock:
	'''
	This is going to be a 4x4 block
	consisting of 16 tiles
	'''

	BLOCKS = [
		# block 0
		(	
		[[0, 1, 0, 0],
		 [0, 1, 0, 0],
		 [0, 1, 0, 0], 
		 [0, 1, 0, 0]],
	 	(0, 0, 255))

		# block 1
		
	]

	def __init__(self, position, display):
		#self._block_id = ....
		# self._block_id should be a random value between 1 and 7
		# if block_id is 1, then the matrix should be

		# self._block should be a 4x4 matrix of 0s and 1s
		if self._block_id == 1:
			self._block = [[0, 1, 0, 0] for _ in range(4)]
		#elif....

	def rotate_left(self):
		pass

	def rotate_right(self):
		pass

	def move_block_down(self):
		pass


if __name__ == "__main__":
	disp = pygame.display.set_mode((400, 300), 0, 32)
	#tile = Tile((10, 10), disp)
	tile = TetrisTile((255, 0, 0), (10, 10), disp)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(pygame.mouse.get_pos())
		
		