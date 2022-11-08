import pyautogui as spam;
import time;

def spammsg():
    limit  = input("Repeat :");
    msg = input("The Msg:");
    i = 0
    print("You have 20 seconds to go your messages and click!");
    time.sleep(20);
    while i < int(limit):
        spam.typewrite(msg);
        spam.press('Enter')
        i += 1


spammsg();