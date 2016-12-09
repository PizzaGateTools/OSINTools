import screenshot
from termcolor import colored, cprint
print colored('   |  |    _ \ _)                ___|       |        ', 'red')
print colored('_  |_ |_| |   | |_  /_  /  _` | |      _` | __|  _ \ ', 'white')
print colored('_  |_ |_| ___/  |  /   /  (   | |   | (   | |    __/ ', 'white')
print colored('  _| _|  _|    _|___|___|\__,_|\____|\__,_|\__|\___| ', 'blue')
print colored('---------------------------------------------------- ', 'white')
print colored(' Usage: python pgate_screenshot.py or 	            ', 'red')
print colored(' proxychains python pgate_screenshot.py              ', 'red')
print colored('---------------------------------------------------- ', 'red')
print ('')


form = 'http://'
s = screenshot.Screenshot()
image = s.get_image(form+raw_input("Enter the url you would like to capture(ex.:google.com, facebook.com):: "))
image.save(raw_input("Filename to save the image under: "))s
