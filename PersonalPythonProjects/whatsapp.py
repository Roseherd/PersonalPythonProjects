import pywhatkit as kit
import pyautogui as pt
from PIL import Image

phone_number = "+233542161144"

message = "This is a Python message from Richard."

image = Image.open("C:\\Users\\Hp\\OneDrive\\Pictures\\Screenshots\\whatsapp_send_button.png.png")


try:
    kit.sendwhatmsg(phone_number, message, 22, 3)
    pt.click("image")

    print("Message Sent!")
except:
    print("Error in sending the message")
