from pynput import keyboard

def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

def suelta(tecla):
	print('Se ha soltado la tecla ' + str(tecla))

with keyboard.Listener(pulsa, suelta) as escuchador:
	escuchador.join()