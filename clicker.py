import keyboard
import pyautogui
def pressed():
    while True:
        if keyboard.is_pressed('l'): #enter you button1
            while True:
                pyautogui.click()
                if keyboard.is_pressed('o'): #enter you button2
                    break






if __name__ == "__main__":
    pressed()
