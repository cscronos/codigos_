import keyboard

while True:
    if keyboard.read_key() == "a":
        print('a')
    if keyboard.read_key() == "s":
        print('s')

# while True:
#     if is_pressed("q"):
#         print("You pressed q")
#         break
        
# keyboard.on_press_key("r", lambda _:print("You pressed r"))