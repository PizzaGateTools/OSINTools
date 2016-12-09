import screenshot
form = 'http://'
s = screenshot.Screenshot()
image = s.get_image(form+raw_input("Enter the url you would like to capture: "))
image.save(raw_input("Filename to save the image under: "))

