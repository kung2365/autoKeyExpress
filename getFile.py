
# Program extracting first column 
import xlrd
import pyautogui 
import time
import sys
import os
from pynput.keyboard import Key, Listener
import time
import threading

# partNumber = ''
# partName = ''

stp = False
listen = False

def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    
    print(key)
    if key == Key.f2 or stp == True:
        # Stop listener
        print('pppppppppppppppppppppppppppppppppppppppppppppp')
        return False

def add(partNumber, partName):
    timeToWait = 0.1
    # clock for new
    pyautogui.click(23, 76)
    time.sleep(timeToWait)
    
    # click for insert part number
    pyautogui.click(250, 139)
    time.sleep(timeToWait)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')

    # key part number value
    pyautogui.write(str(partNumber), interval=0.01)
    time.sleep(timeToWait)

    

    #click for inser part name
    pyautogui.click(321, 166)
    time.sleep(timeToWait)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')

    # key part name
    pyautogui.write(str(partName), interval=0.01)
    time.sleep(timeToWait)

    #click for ok
    # pyautogui.click(989, 566)
    # time.sleep(timeToWait)

    #click for save
    pyautogui.click(212, 78)
    time.sleep(timeToWait)

    #click for ok
    # pyautogui.click(989, 566)
    # time.sleep(timeToWait)

    

    # esc to exit
    pyautogui.press('esc')
    time.sleep(timeToWait)
    pyautogui.press('esc')
    time.sleep(timeToWait)
    pyautogui.click(164, 84)
    time.sleep(timeToWait)
    pyautogui.click(164, 84)
    time.sleep(timeToWait*1.5)

def keyIn():
    with Listener(on_press=on_press) as listener:
            listener.join()
    print('kkkkkkkkkkkkkkkkkkkkkkk')
def auto(loc):
    #loc = (".\\doc\\doc1.xlsx") 
    try:
        wb = xlrd.open_workbook(loc)
    except:
        return 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0)

    stp = False
    listen = False

    threads = []
    t = threading.Thread(target=keyIn)
    threads.append(t)
    t.start()
    for i in range(sheet.nrows): 
        #print(sheet.cell_value(i+1, 1))
        partNumber = sheet.cell_value(i, 0)
        partName = sheet.cell_value(i, 1)
        if  'stop' in str(t.is_alive()):
            print('ttttttttttttttttt')
            break
        print(str(t.is_alive),'9999999999999')
        partNumber = str(partNumber).replace('-', '',2)
        if i > 0:
            add(partNumber, partName)
            print(partNumber)
    stp = True

        
    
    