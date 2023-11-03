import keyboard
import time
import random
from key_check import key_check
from gspread import service_account_from_dict
from configparser import ConfigParser
import wmi
from camera_move import MouseMoveTo


def press_enter():
    while True:
        random_time = random.randint(1, 3)
        keyboard.press_and_release('enter')
        time.sleep(random_time)
        keyboard.press('w')
        time.sleep(random_time)
        keyboard.release('w')
        time.sleep(1)
        random_bool = random.choice([True, False])
        if random_bool:
            random_camera = random.randint(250, 550)
        else:
            random_camera = random.randint(-550, -250)

        for i in range(abs(random_camera)):
            if random_camera >= 0:
                MouseMoveTo(2, 0)
                time.sleep(0.001)
            else:
                MouseMoveTo(-2, 0)
                time.sleep(0.001)

        random_time_between_cycles = random.randint(30, 60)
        for i in range(random_time_between_cycles):
            time.sleep(1)
            if keyboard.is_pressed('ctrl+2'):
                print("script stopped")
                return

print("(RU) Anti-AFK Скрипт, создатель на Funpay: pnqua - https://funpay.com/users/1408209/")
print("(ENG) Anti-AFK Script made by Funpay: pnqua - https://funpay.com/users/1408209/")
key_check()
print(f'(RU) Нажмите ctrl+1, чтобы запустить скрипт. Зажмите ctrl+2 на секунду, чтобы остановить')
print(f'(ENG) Press ctrl+1 to start. Hold ctrl+2 for a sec to stop')
while True:
    time.sleep(0.02)
    
    if keyboard.is_pressed('ctrl+1'):
        print("script started")
        time.sleep(3)
        press_enter()











