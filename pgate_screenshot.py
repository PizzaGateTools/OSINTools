import screenshot
s = screenshot.Screenshot()
image = s.get_image(raw_input("Enter the url you would like to capture: "))
image.save(raw_input("Filename to save the image under: "))

