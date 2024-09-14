from phue import Bridge


b = Bridge('Your IP')
b.connect()
b.get_api()

def on_off():
    print(b.get_light(1, 'on'))
    if not b.get_light(1, 'on'):
        b.set_light([1,4], 'on', True)
    else:
        b.set_light([1,4], 'on', False)
#while True:
#   user_input_lamp = int(input("Lampe eingeben 1,4: "))
#    user_input_cmd = input("Command eingeben (on): ")
#    user_input_ToF = (input("True or False t or f: "))

#   if user_input_ToF == "t":
#        user_input_ToF = True

#    else:
#        user_input_ToF = False
        
#    if user_input_lamp == 14:
#        user_input_lamp = [1,4]

    #user_input_color = int(input("von 0-65.000: "))
    #user_input_bri = int(input("von 0-255: "))

#    b.set_light(user_input_lamp, user_input_cmd, user_input_ToF)



    

#    command = {'transitiontime' : 50, 'on': True}
#    b.set_light([1,4], command)