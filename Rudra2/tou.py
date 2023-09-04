import webbrowser
import pyautogui                                            #pip install PyAutoGUI

def open_youtube():
    query = input(">> ")
    query = query.replace("search","").replace("youtube","").replace("on","").replace("play","").replace("play a","").replace("the","").replace("music","").replace("video","")
    webbrowser.open("https://www.youtube.com/")
    try:
        pyautogui.sleep(3)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.3)
        pyautogui.write(query)
        pyautogui.press('enter')
    except:
        pyautogui.sleep(5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.sleep(0.3)
        pyautogui.write(query)
        pyautogui.press('enter')

# Usage
open_youtube()
