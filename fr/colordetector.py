import pyautogui
import pygetwindow as gw
import time

def detect_cyan_color(image):
    cyan_color = (0, 255, 255) 
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel_color = image.getpixel((x, y))
            if pixel_color == cyan_color:
                return x, y
    return None, None


screen_width, screen_height = pyautogui.size()


cyan_x = None
cyan_y = None


scan_interval = 0  

try:
    while True:
        
        screenshot = pyautogui.screenshot()

        
        new_cyan_x, new_cyan_y = detect_cyan_color(screenshot)
        if new_cyan_x is not None and new_cyan_y is not None:
            cyan_x = new_cyan_x
            cyan_y = new_cyan_y

       
        if cyan_x is not None and cyan_y is not None:
            
            pyautogui.moveTo(cyan_x, cyan_y)

        
        time.sleep(scan_interval)

except KeyboardInterrupt:
    print("Program finished.")

