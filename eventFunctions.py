import os 
import sys
import cv2
import numpy as np
import datetime
import pyautogui as pg
from typing import Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#function for openCV to take screenshot
def takeScreenshot() -> np.ndarray:
    # Take a screenshot
    screenshot = cv2.cvtColor(
            np.array(pg.screenshot(
                    region=(0, 0, 2560, 1440))), 
            cv2.COLOR_BGR2GRAY)
    # screenshotAsPic = np.array(pg.screenshot(region=(0, 0, 2560, 1440))) used for debugging
    return screenshot#,screenshotAsPic used for debugging

def isImageOnScreen(templateName: str, screenshot: Optional[np.ndarray] = None) -> bool:
    # if screenshot is None, take a new screenshot
    if screenshot is None:
        print("Taking screenshot")
        screenshot = takeScreenshot()   
    
    templatePath = os.path.join('template/', f"{templateName}.png")
    template = cv2.imread(templatePath, cv2.IMREAD_GRAYSCALE)
    
    #check if the template is on the screenshot
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.8)
    
        # Not sure why this works but okay
    for pt in zip(*loc[::-1]):
        return True

    return False
    

test = isImageOnScreen("countryselection")
print(test)
