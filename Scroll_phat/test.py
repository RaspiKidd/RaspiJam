import scrollphat, time, pygame

pygame.init()
pygame.joystick.init()


joycount = pygame.joystick.get_count()
print('Available Joysticks: {}'.format(joycount))

joystick = pygame.joystick.Joystick(0)
joystick.init()

print joystick.get_init()
print joystick.get_id()
print joystick.get_name()
print joystick.get_numaxes()
print joystick.get_numballs()
print joystick.get_numbuttons()
print joystick.get_numhats()
print joystick.get_axis(0)

brightness = 20

w, h = (11, 5)
x, y = (0, 0)

grav = 0.5
jump_vel = 0
jump_decay = 0.8

move_speed = 1

while True:

    scrollphat.clear()
    scrollphat.set_brightness(brightness)
    scrollphat.set_pixel(int(x), int(y), 1)
    scrollphat.update()
    time.sleep(0.03)

    pygame.event.pump()

    axis_value = joystick.get_axis(0)

    if axis_value > 0.8:
        x += move_speed
    elif axis_value < -0.8:
        x -= move_speed

    if x >= w:
        x = w - 1
    elif x < 0:
        x = 0

    axis_value = joystick.get_axis(1)

    if axis_value > 0.8:
        y += move_speed
    elif axis_value < -0.8:
        y -= move_speed

    y += grav
    y -= jump_vel

    jump_vel *= jump_decay

    if joystick.get_button(0):
        print('JUMPING!!!!')
        jump_vel = 1

    if y >= h:
        y = h - 1
    elif y < 0:
        y = 0



