import time
import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BOARD)

print("0")

GPIO.setup(37, GPIO.OUT)  # Purple
GPIO.setup(32, GPIO.OUT)  # White

# 34Ground

GPIO.setup(36, GPIO.OUT)  # Orange
GPIO.setup(38, GPIO.OUT)  # Gray

# BACK WHEELS
GPIO.setup(35, GPIO.OUT)  # Green
GPIO.setup(33, GPIO.OUT)  # Yellow

GPIO.setup(31, GPIO.OUT)  # Blue
GPIO.setup(29, GPIO.OUT)  # Orange

# front Wheel test

print("1")

GPIO.output(37, True)
time.sleep(3)
GPIO.output(37, False)

print("2")

GPIO.output(32, True)
time.sleep(3)
GPIO.output(32, False)

print("3")
GPIO.output(36, True)
time.sleep(3)
GPIO.output(36, False)

print("4")

GPIO.output(38, True)
time.sleep(3)
GPIO.output(38, False)

print("5")
GPIO.output(35, True)
time.sleep(3)
GPIO.output(35)


print("6")
GPIO.output(33, True)
time.sleep(3)
GPIO.output(33, False)

print("7")
GPIO.output(31, True)
time.sleep(3)
GPIO.output(31, False)

print("8")
GPIO.output(29, True)
time.sleep(3)
GPIO.output(29, False)


print("9")


exit()

print("6")
