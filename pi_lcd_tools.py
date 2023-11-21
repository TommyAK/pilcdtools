#!/usr/bin/env python

from RPLCD.i2c import CharLCD
from tabulate import tabulate
from art import tprint
import subprocess
import datetime
import time
import os

lcd = CharLCD('PCF8574', 0x27)

def menu():
    tprint("Pi      LCD     Tools")
    table = [['Display Time and Date', 'Display CPU Temp and Usage', 'Display Storage Usage',
              'Display Message', 'Display IP'], ['1', '2', '3', '4', '5']]
    print(tabulate(table, headers='firstrow', tablefmt='pretty'))
    while True:
        x = int(input(f"Enter choice (1-{len(table[1])}) : "))
        if x == 1:
            write_time()
        elif x == 2:
            write_pi_monitor()
        elif x == 3:
            write_root_storage()
        elif x == 4:
            write_message()
        elif x == 5:
            display_ip_addr()
        else:
            print("Invalid selection.")


def display_ip_addr():
    lcd.home()
    print("Displaying IP addresses...")
    private_ip = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
    private_ip = private_ip.stdout.strip()
    public_ip = subprocess.run(['curl', 'ipinfo.io/ip'], capture_output=True, text=True)
    public_ip = public_ip.stdout.strip()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(f"{private_ip}")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"{public_ip}")


def write_time():
    lcd.home()
    print("Displaying time...")
    while True:
        time_date = datetime.datetime.now()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(str(time_date.strftime('%H:%M:%S')))
        lcd.cursor_pos = (1, 0)
        lcd.write_string(str(time_date.strftime('%d-%m-%Y')))
        time.sleep(1)


def write_root_storage():
    lcd.home()
    print("Displaying storage...")
    while True:
        storage = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
        lines = storage.stdout.split('\n')
        if len(lines) > 1:
            columns = lines[1].split()
            total, used, free, percentage = columns[1], columns[2], columns[3], columns[4]
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f"Total: {total}")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Used: {used}")


def write_message():
    lcd.home()
    string = str(input("Input message to display: "))
    speed = float(input("Message display speed (0.1 - 1.0): "))
    print("Displaying message...")
    while True:
        padding = ' ' * 16
        text = padding + string + padding
        for i in range(len(text) - 16 + 1):
            message = text[i:i + 16]
            lcd.home()
            lcd.write_string(message)
            time.sleep(speed)


def write_pi_monitor():
    lcd.home()
    print("Displaying temp and memory usage...")
    while True:
        lcd.cursor_pos = (0, 0)
        if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
            with open('/sys/class/thermal/thermal_zone0/temp') as temp:
                temp = temp.readline().strip()
            if temp.isdigit():
                temp = "{:.2f}".format(float(temp) / 1000)
        lcd.write_string(f"CPU Temp: {temp}C")
        lcd.cursor_pos = (1, 0)
        total_mem = (subprocess.getoutput("free -h | awk 'FNR == 2 {print $2}'"))
        available_mem = (subprocess.getoutput("free -h | awk 'FNR == 2 {print $3}'"))
        lcd.write_string(f"RAM: {available_mem}/{total_mem}")
        time.sleep(5)
        lcd.clear()


menu()
