# download 
# https://github.com/T-622/RPI-PICO-I2C-LCD/blob/main/pico_i2c_lcd.py
# download 
# https://github.com/dhylands/python_lcd/blob/master/lcd/lcd_api.py
import utime
import network       # For Wi-Fi connectivity
import urequests     # For making HTTP requests
import dht           # For interfacing with DHT sensors
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd


# Wi-Fi credentials

ssid = 'Wokwi-GUEST'     # SSID of the Wi-Fi network

password = ''            # Password (empty for open networks like Wokwi-GUEST)



# ThingSpeak API configuration

THINGSPEAK_API_KEY = 'NU4UEM0T3BJ0NTHF'  # Your ThingSpeak Write API Key

THINGSPEAK_URL = 'https://api.thingspeak.com/update'  # ThingSpeak endpoint



# Set up Wi-Fi in station mode

wlan = network.WLAN(network.STA_IF)  # Create a WLAN object in station mode, the device connects to a Wi-Fi network as a client. 

wlan.active(True)                    # Activate the Wi-Fi interface

wlan.connect(ssid, password)         # Connect to the specified Wi-Fi network



# Wait until connected

print("Connecting to Wi-Fi...", end="")

while not wlan.isconnected():

    print(".", end="")               # Print dots while waiting

    utime.sleep(0.5)                  # Wait half a second before retrying



# Once connected, print confirmation and IP address

print("\nConnected!")

print("IP address:", wlan.ifconfig()[0])  # Display the assigned IP address



# Initialize the DHT22 sensor on GPIO pin 15

sensor = dht.DHT22(Pin(15))

# Initialize LCD

i2c =I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

lcd = I2cLcd(i2c, 0x27, 4, 20)
lcd.clear()
lcd.putstr("IoT system ready")
utime.sleep(2)
lcd.clear()



# Function to send temperature data to ThingSpeak

def send_to_thingspeak(temp, humid):

    if temp is None or humid is None:

        print("No data to send.")

        return

    try:

        # Send HTTP POST request to ThingSpeak with temperature data

        response = urequests.post(

            THINGSPEAK_URL,

            data='api_key={}&field1={}&field2={}'.format(THINGSPEAK_API_KEY, temp, humid),

            headers={'Content-Type': 'application/x-www-form-urlencoded'}

        )

        print("ThingSpeak response:", response.text)  # Print server response

        response.close()  # Close the connection

    except Exception as e:

        print("Failed to send data:", e)  # Handle any errors



# Main loop: read sensor and send data every 15 seconds

while True:

    try:

        sensor.measure()                      # Trigger sensor measurement

        temperature = sensor.temperature()    # Read temperature in Celsius
        humidity = sensor.humidity()          # Read humidity in percent

        lcd.clear()
        lcd.putstr("Temp: {:.1f} C\n".format(temperature))
        lcd.putstr("Humid: {:.1f} %\n".format(humidity))

        print("Temperature:", temperature, "°C")  # Display temperature
        print("Humid:", humidity, "%")            # Display humidity

        send_to_thingspeak(temperature, humidity)       # Send data to ThingSpeak

    except Exception as e:

        print("Error reading sensor or sending data:", e)  # Handle errors

    

    utime.sleep(15)  # Wait 15 seconds before next reading
utime.sleep(1)


