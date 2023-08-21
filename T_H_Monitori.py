import Adafruit_DHT
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
THINGSPEAK_API_KEY = "YOUR_API_KEY"

def send_to_thingspeak(temp, humidity):
    url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={temp:.2f}&field2={humidity:.2f}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print("Error sending data")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temperature={temperature:.2f}°C  Humidity={humidity:.2f}%")
        send_to_thingspeak(temperature, humidity)
    else:
        print("Failed to retrieve data from sensor")
