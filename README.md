# Raspberry Pi LCD Tools

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/419ed7fc-8e89-4742-957a-6bf6b386bd46" width=40% height=40%>

## About
This project was done to experiment with the Raspberry Pi's GPIO board. I had used single-board computers for a variety of other projects but none which utilised the GPIO. I wanted to control a LCD Screen as it seemed like an interesting opportunity to combine setting up hardware and also developing software. This repository will serve as a relatively brief log of what I did, and how to reproduce the experiments and results as everything I did will be explained. I will assume that someone willing to follow along has prior knowledge of Linux and using the terminal.

## Hardware

__Raspberry Pi 3__

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/eec2ac55-fb59-4535-90da-01110162f5a9" width=20% height=20%>

I used the Raspberry Pi to run the software in Python and its 40 Pin GPIO header for the connectivity of the LCD screen. 


__Logic Level Converter__

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/1f64be68-66ac-4fef-acc8-062cc9ea0261" width=30% height=30%>

Since the LCD screen is 5V and the Raspberry Pi's GPIO pins are not tolerant to such voltage, I needed a way to safely connect the LCD without potentially harming the board. The logic level converter is used to convert a 5V output to 3.3V, which enables me to connect the LCD screen without any risk of damage.

__HD44780 16x2 LCD Screen (with I2C Backpack)__

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/baf8ccf8-515b-40b9-92f6-42b2b350e7c6" width=30% height=30%>

The LCD screen uses a parallel interface and mine already came with the I2C backpack installed; however, you may need to purchase this if yours does not have one.


## Circuit Diagram
![pigpio_lcdscreen_coloured drawio](https://github.com/TommyAK/pilcdtools/assets/35144580/a3492e49-721e-4ece-bb16-35d9b4ad655b)

[Click here to open larger image](https://i.ibb.co/fvmPR42/pigpio-lcdscreen-coloured-drawio.png)

## Software
**PyCharm Professional**

I used PyCharm Professional as it a very sophisticated IDE and can connect remotely via SSH or SFTP. This was used to work and test my code on the Raspberry Pi remotely.

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

**Raspberry Pi OS**

The first thing to do after installing Raspberry Pi OS is to enable the I2C interface.

This can be done by opening a terminal and typing `sudo raspi-config`.

From here, simply navigate to *3 Interface Options* and then *P5 I2C*. It will you ask if you would like ARM I2C interface to be enabled and you can select *Yes*

It is worth noting that SSH can also be enabled from this menu. SSH is required for remote development.


**Python**

Python and its package manager pip can be installed with `sudo apt-install python3` and `sudo apt install pip`.

Pip libraries can be installed by typing `sudo pip install <package name>`.



**Running The Code**

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/3fe4061c-7e6c-4805-aee2-aa3c928c8d62" width=80% height=80%>

The code can be cloned from this repository or downloaded and extracted.

After executing the `.py` file on the Raspberry Pi, you will be greeted with a menu that will provide you with different display options. Selecting one will output information on the LCD screen.

**Example output on LCD:**

<img src="https://github.com/TommyAK/pilcdtools/assets/35144580/3768e1e0-8d49-4f53-89e7-1fb420e394d3" width=90% height=90%>







