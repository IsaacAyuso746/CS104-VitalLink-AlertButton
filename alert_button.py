from dotenv import load_dotenv
import os
import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
print("Alert button monitoring system is now active. Press Ctrl+C to stop.")
message = {
    "chat_id": "8538794016",
    "text": "Someone pressed the button!!"
}

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            requests.post("https://api.telegram.org/bot8935248314:AAE-GTBA2PkfN4EqR-K3yTC49C7Z3xdd0Zc/sendMessage", json= message)
            print("Someone pressed the alert button!")
            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()

