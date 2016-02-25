
import scrollphat, time, pygame 		# importing libraries to use
	
pygame.init()					# Initialising pygame library 			
pygame.joystick.init()				# Initilaising the joystick module from pygame 


joycount = pygame.joystick.get_count()		# Returns the number of joysticks available
print('Available Joysticks: {}'.format(joycount)) # prints no joysticks available 

joystick = pygame.joystick.Joystick(0)		# Create a joystick instance
joystick.init()					# Initialise joystick

print joystick.get_init()			# Check if joystick is initialised
print joystick.get_id()				# get the ID of the joystick
print joystick.get_name()			# Get the system name of the joystick
print joystick.get_numaxes()			# Get the number of axis on the joystick
print joystick.get_numballs()			# Get the number of trackballs on the joystick	
print joystick.get_numbuttons()			# Get the number of buttons on the joystick
print joystick.get_numhats()			# Get the number of hat controls on the joystick
print joystick.get_axis(0)			# Get the current number of axis

brightness = 20					# Setting brightness on scroll phat

w, h = (11, 5)					# Setting width and height
x, y = (0, 0)					# Setting x and y 

grav = 0.5					# Setting Gravity
jump_vel = 0					# Setting jump velocity
jump_decay = 0.8				# Setting jump decay

move_speed = 1					# Setting movement speed

while True:					# Loop forever

    scrollphat.clear()				# Clearing the display
    scrollphat.set_brightness(brightness)	# Getting the brightness for LEDS
    scrollphat.set_pixel(int(x), int(y), 1)	# Setting pixel to show in bottom left corner
    scrollphat.update()				# Updating scroll phat	
    time.sleep(0.03)				# Set scroll phat to sleep for .3 seconds

    pygame.event.pump()				# Processes pygame event handlers internally

    axis_value = joystick.get_axis(0)		# Setting axis value for x

    if axis_value > 0.8:			# If axis value is greater than 0.8 
        x += move_speed				# increase move speed of x
    elif axis_value < -0.8:			# If axis value is less than 0.8
        x -= move_speed				# Decrease move speed

    if x >= w:					# if x is greater than width
        x = w - 1				# x = width - 1
    elif x < 0:					# If x is less than 0
        x = 0					# x is equal to 0

    axis_value = joystick.get_axis(1)		# Setting axis value for y

    if axis_value > 0.8:			# if y is greter than 0.8
        y += move_speed				# increase move speed of y
    elif axis_value < -0.8:			# if y is less than 0.8
        y -= move_speed				# decrese move speed of y

    y += grav					# y = y+grav 
    y -= jump_v

    jump_vel *= jump_decay

    if joystick.get_button(0):
        print('JUMPING!!!!')
        jump_vel = 1

    if y >= h:
        y = h - 1
    elif y < 0:
        y = 0



