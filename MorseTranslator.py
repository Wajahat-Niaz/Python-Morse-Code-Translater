#Morse Translator
from time import sleep

#all the prints used in the program
ERROR = 'Error Unrecognized Morse Character: {}'
WELCOME = 'Welcome To Morse Code Translator\n\nWhat Would You Like To Do?\n'
START = '[1]Translate To Morse\n[2]Translate From Morse\n\nSelection: '
SELECTION_WRONG = '\nPlease Select 1 or 2\n'
TO_MORSE = 'To Morse Selected\n'
FROM_MORSE = 'From Morse Selected\n'
ENTER_TEXT = 'Enter Text To Translate: '
ENTER_MORSE = 'Enter Morse Code To Translate: '
AFTER_TRANSLATION = ''

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '＄': '...-..-', '@': '.--.-.', '\n': '.-.-', '\n\n': '.-.-.', ' ':'  ', '':''
}

#used to make the text appear in a typing like effect
def write_text(speed, text):
	for i in text:
		sleep(60/speed)
		print(i, end='', flush=True)
	print('\n')

#translate to morse code
def to_morse(eng):
	morse = ''
	for i in eng:
		morse += morse_dict.get(i.capitalize(),'X')+(' ' if i != ' ' else '')
	return '\nTranslated: '+morse

#the method to get english text from the morse code dictionary
def get_eng(morse):
	try:
		return list(morse_dict.keys())[list(morse_dict.values()).index(morse)]
	except ValueError:
		print(ERROR.format(morse))
		return ''

#translate back from morse code
def from_morse(morse):
	eng = ''
	morse_word = ''
	for i in morse+' ':
		if i != ' ':
			morse_word += i
		else:
			eng += get_eng(morse_word)
			morse_word = ''
	return '\nTranslated: '+eng

def start_app():
	print(WELCOME)
	while True:
		selection = input(START)
		if  selection == '1':
			print(TO_MORSE)
			text = input(ENTER_TEXT)
			#make the text appear faster as it gets longer
			write_text(50*(len(text))+(1000/len(text)),to_morse(text))
		elif selection == '2':
			print(FROM_MORSE)
			morse_code = input(ENTER_MORSE)
			write_text(50*(len(morse_code))+(1000/len(text)),from_morse(morse_code))
		else:
			print(SELECTION_WRONG)
	
start_app()