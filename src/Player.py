import pygame
from paths import *

class Stickman_player:
	_animate_frame = 0
	_stop = 0
	_frames = 5 # Number of times a frame is to be shown in a loop
	_facing = "R" # Direction in which the character faces
	_player_horizontal_speed = 2
	def __init__(self,WINDOW_DIMENSIONS):
		
		# Position of the character
		self.x = WINDOW_DIMENSIONS[0]/2
		self.y = WINDOW_DIMENSIONS[1]*15/16

		# Standing image facing Left Direction
		self.standing_imgL = [pygame.image.load(standing_imgL)]
		self.standing_imgL+=[(self.standing_imgL[0].get_width(),self.standing_imgL[0].get_height())]
		
		# Standing image facing Right Direction
		self.standing_imgR = [pygame.image.load(standing_imgR)]
		self.standing_imgR+=[(self.standing_imgR[0].get_width(),self.standing_imgR[0].get_height())]

		# Walking images facing Left Direction
		self.walking_imgsL = [[pygame.image.load(walking_img)] for walking_img in walking_imgsL]

		# Walking images facing Left Direction
		self.walking_imgsR = [[pygame.image.load(walking_img)] for walking_img in walking_imgsR]
		
		# Adding other attributes to the images' list
		for img in self.walking_imgsR:
			img.append((img[0].get_width(),img[0].get_height()))

		for img in self.walking_imgsL:
			img.append((img[0].get_width(),img[0].get_height()))

		# Width and Height of all image frames
		self.width,self.height = self.standing_imgL[1][0],self.standing_imgL[1][1]

	# Get position of the character
	def _get_pos(self):
		return (self.x - self.width/2,self.y - self.height)

	# Private method left facing animation of the character
	def _to_left(self):

		val = self._animate_frame//self._frames
		if val == len(self.walking_imgsL):
			self._animate_frame = 0

		val = self._animate_frame//self._frames
		
		self._animate_frame+=1
		self.x -= self._player_horizontal_speed
		return self.walking_imgsL[val]

	# Private method right facing animation of the character
	def _to_right(self):
		val = self._animate_frame//self._frames
		if val == len(self.walking_imgsR):
			self._animate_frame = 0

		val = self._animate_frame//self._frames

		self._animate_frame+=1
		self.x += self._player_horizontal_speed
		return self.walking_imgsR[val]

	# Frame movement of the character
	def frame_movement(self):

		if self._facing == "R":
			return self._to_right() + [self._get_pos()]
		return self._to_left() + [self._get_pos()]

	# Set the _stop to 1 in order to stop the frame changing of the character
	def stop_animating(self):
		self._stop = 1

	# Return the default frame for the character
	def default_frame(self):
		if self._stop:
			self._animate_frame = 0
			self._stop = 0
		if self._facing == "R":
			return self.standing_imgR + [self._get_pos()]
		return self.standing_imgL + [self._get_pos()]


	# Set direction as right
	def make_right(self):
		self._facing = "R"

	# Set direction as leftt
	def make_left(self):
		self._facing = "L"

