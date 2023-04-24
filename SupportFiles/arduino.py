import serial

from time import sleep
from pyfirmata import Arduino,SERVO,util

def connectArd():
    port = 'COM4'
    pin = 9
    board = Arduino(port)
    board.digital[pin].mode = SERVO
    return board

def rot(board,pin,angle):
    board.digital[pin].write(angle)