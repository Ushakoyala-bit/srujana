# Program to take a screenshot using pyscreenshot

import pyscreenshot
import datetime

# Capture the screen
try:
    image = pyscreenshot.grab()
    print("Screenshot captured successfully.")
except Exception as e:
    print(f"Error capturing screenshot: {e}")
    exit()

# Display the captured screenshot
try:
    image.show()
    print("Screenshot displayed successfully.")
except Exception as e:
    print(f"Error displaying screenshot: {e}")

# Save the screenshot with a timestamped filename
try:
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    image.save(filename)
    print(f"Screenshot saved as {filename}")
except Exception as e:
    print(f"Error saving screenshot: {e}")



    # Program to take screenshot 
  
import pyscreenshot 
  
# To capture the screen 
image = pyscreenshot.grab() 
  
# To display the captured screenshot 
image.show() 
  
# To save the screenshot 
image.save("GeeksforGeeks.png") 