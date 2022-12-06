import pyautogui

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True


def start_browser(name_browser=''):
    pyautogui.press('win')
    pyautogui.write(name_browser)
    pyautogui.press('Enter')


def open_site(url1='',url2=''):
    pyautogui.write(url1)
    pyautogui.press('Enter')
    pyautogui.sleep(6)
    pyautogui.hotkey('ctrl','t')
    pyautogui.write(url2)
    pyautogui.press('Enter')


def main():
    start_browser(name_browser='your browser')
    open_site(url1='your url',url2='your url')


if __name__ == '__main__':
    main()
