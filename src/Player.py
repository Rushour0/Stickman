import pygame
from paths import *
from player_status_codes import *
from bitarray import bitarray

class Stickman_player:

	# Player attributes

	_facing = "R" # Direction in which the character faces
	_stop = 0 # Boolean for stopping action
	_movement_status = bitarray('00000000')|STANDING

	# Animation and other attributes

	_animate_frame = 0 # Keeps count of the animation frames
	_frames = 5 # Number of times a frame is to be shown in a loop
	_player_horizontal_speed = 2 # Horizontal speed of the character


	""" INITIALIZATION OF THE CHARACTER """

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


	""" PRIVATE METHODS FOR FRAME MANAGEMENT AND CHARACTER MOVEMENT """

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


	""" STATUS MODIFICATION OPERATIONS """

	# Remove any status from the _movement_status
	def _removeStatus(self,status):
		self._movement_status &= ~status

	# Add any status from the _movement_status
	def _addStatus(self,status):
		self._movement_status |= status


	""" STATUS CHECKING """

	# Private method returns whether the character is moving or not
	def _is_moving(self):
		return (self._movement_status & MOVING) == MOVING

	# Private method returns whether the character is walking or not
	def _is_walking(self):
		return (self._movement_status & WALKING) == WALKING

	# Private method returns whether the character is jumping or not
	def _is_jumping(self):
		return (self._movement_status & JUMPING) == JUMPING

	# Private method returns whether the character is standing or not
	def _is_standing(self):
		return (self._movement_status & STANDING) == STANDING

	# Private method returns whether the character is crouching or not
	def _is_crouching(self):
		return (self._movement_status & CROUCHING) == CROUCHING


	""" STATUS SETTING """

	# Private method adds moving to status
	def _make_moving(self):
		self._addStatus(MOVING)

	# Private method adds walking to status
	def _make_walking(self):
		self._addStatus(WALKING)

	# Private method adds jumping to status
	def _make_jumping(self):
		self._addStatus(JUMPING)

	# Private method sets status to standing
	def _make_standing(self):
		self._addStatus(STANDING)
		self._removeStatus(CROUCHING)

	# Private method sets status to crouching
	def _make_crouching(self):
		self._addStatus(CROUCHING)
		self._removeStatus(STANDING)


	""" STATUS REMOVAL """

	# Private method removes moving status
	def _remove_moving(self):
		self._removeStatus(MOVING)

	# Private method adds to status to walking
	def _remove_walking(self):
		self._removeStatus(WALKING)

	# Private method adds to status to standing
	def _remove_jumping(self):
		self._removeStatus(JUMPING)


	""" FRAME MANAGEMENT """

	# Return the default frame for the character
	def _default_frame(self):
		# Check for stop moving condiiton
		if self._stop:
			self._animate_frame = 0 # Set animation frames back to zero
			self._stop = 0	# Since stopping action will be complete, _stop is made false again

		# Player is standing
		if self._facing == "R":
			return self.standing_imgR + [self._get_pos()]
		return self.standing_imgL + [self._get_pos()]

	# Frame movement of the character
	def frame_movement(self):
		# Checking if the character is moving
		if self._is_moving():
			# Checking for movement status type
			if self._is_walking():
				if self._facing == "R":
					return self._to_right() + [self._get_pos()]
				return self._to_left() + [self._get_pos()]

		# If the character isn't moving
		return self._default_frame()

	
	""" CHARACTER MOVEMENT """

	# Set the _stop to 1 in order to stop the frame changing of the character
	def stop_moving(self):
		self._stop = 1
		self._remove_moving()

	# Set direction as right
	def move_right(self):
		self._facing = "R"
		self._make_moving()
		self._make_walking()

	# Set direction as left
	def move_left(self):
		self._facing = "L"
		self._make_moving()
		self._make_walking()
	
	# Jump up
	def jump_up(self):
		self._make_moving()
		self._make_jumping()

	# Crouch down
	def crouch_down(self):
		self._make_moving()
		self._make_crouching()
