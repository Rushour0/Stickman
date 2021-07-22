from globals import *
from pygame.locals import *

# PyGame initialized
pygame.init()

# Refresh Rate
clock = pygame.time.Clock()

# Font and size
font = pygame.font.Font(font_path, 32)

# For performance
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Set window name
pygame.display.set_caption("Stickman")

# Create screen
flags = DOUBLEBUF
screen = pygame.display.set_mode(WINDOW_DIMENSIONS, flags, 16)

# Background image
background = pygame.image.load(background_img)
print(background.get_width(),background.get_height())

# Player declaration
player = Stickman_player(WINDOW_DIMENSIONS)

def background_show():
	screen.blit(background,(0,0))

def player_show(values):
	player_img = values[0]
	width,height = values[1][0],values[1][1]
	x,y = values[2][0],values[2][1]
	screen.blit(player_img,(x-width/2,y-height))

# Player variables
player_img = player.frame_movement()

# Moving keys
keys = set([pygame.K_a,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_d])

# Jump keys
jumpKeys = set([pygame.K_SPACE,pygame.K_w,pygame.K_UP])

while 1:
	clock.tick(60)
	
	pressed = pygame.key.get_pressed()
	
	events = pygame.event.get()
	for event in events:

		# Click on cross button or alt+f4
		if event.type == pygame.QUIT:
			exit()

		# Key down check
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.move_left()

			if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				player.move_right()
			
			elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
				player.move_left()

			if not player.is_jumping() and event.key in jumpKeys:
				player.jump_up()


		# Key up check
		if event.type == pygame.KEYUP:
			if event.key in keys:
				player.stop_moving()
			if event.key == pygame.K_l:
				print(player.get_pos())

	# Get player image
	player_img = player.frame_movement()
	
	# Final display of all images
	screen.fill((0,0,0))
	background_show()

	player_show(player_img)

	pygame.display.update()


print("over")