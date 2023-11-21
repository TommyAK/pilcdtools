# Raspberry Pi LCD Tools

## About

## Hardware

__Raspberry Pi 3__

I used the Raspberry Pi to run the software in Python and its 40 Pin GPIO header for the connectivity of the LCD screen. 

__Logic Level Converter__

Since the LCD screen is 5V and the Raspberry Pi's GPIO pins are not tolerant to such voltage, I needed a way to safely connect the LCD without potentially harming the board. The logic level converter is used to convert a 5V output to 3.3V, which enables me to connect the LCD screen without any risk of damage.

__HD44780 16x2 LCD Screen (with I2C Backpack)__

The LCD screen uses a parallel interface and mine already came with the I2C backpack installed; however you may need to purchase this if yours does not have one.


## Circuit Diagram
![pigpio_lcdscreen_coloured drawio](https://github.com/TommyAK/pilcdtools/assets/35144580/a3492e49-721e-4ece-bb16-35d9b4ad655b)

## Software
**PyCharm Professional**

I used PyCharm Professional as it a very sophistcated IDE and has the ability to connect remotely via SSH or SFTP. This was used to work and test my code on the Raspberry Pi remotely.

**Python3**

The programming language used for the project, it has excellent collection of libraries suited towards communicating with the I2C backpack and for programming the LCD display.

**Pip**

Package manager for library to install and manage the libraries and modules required.

Python Modules:

- [RPLCD](https://rplcd.readthedocs.io/en/stable/)
- [smbus2](https://smbus2.readthedocs.io/en/latest/index.html)
- [tabulate](https://pypi.org/project/tabulate/)
- [art](https://pypi.org/project/art/)

## Configuration





