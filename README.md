# Temperature and Humidity Monitoring System

The Temperature and Humidity Monitoring System is a Python program that reads data from a DHT22 sensor (temperature and humidity sensor) and sends this data to the ThingSpeak cloud platform for visualization. This system is designed as an example of an IoT (Internet of Things) application.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Reads temperature and humidity data from a DHT22 sensor.
- Sends data to the ThingSpeak cloud platform for visualization.
- Provides error handling for sensor data retrieval and data sending.

## Requirements

- Raspberry Pi or similar hardware with GPIO pins.
- DHT22 temperature and humidity sensor.
- Python 3.x installed on the Raspberry Pi.
- `Adafruit_DHT` library for DHT22 sensor communication.
- `requests` library for sending data to ThingSpeak.

## Installation

1. Clone or download this repository to your Raspberry Pi.

```bash
git clone https://github.com/yourusername/temperature-humidity-monitoring.git```

1. Install the required Python libraries using pip.
```bash
pip install Adafruit_DHT requests```

1. Connect the DHT22 sensor to the appropriate GPIO pin on your Raspberry Pi.

2. Obtain a ThingSpeak account and API key.

3. Configure the program by editing the config.py file (see Configuration).

## Usage

1. Navigate to the program directory.
```bash
cd temperature-humidity-monitoring

2. Run the program.
```bash
python T_H_Monitori.py

3. The program will continuously read data from the DHT22 sensor and send it to ThingSpeak for visualization.

## Configuration
Edit the config.py file to set your configuration options:

DHT_SENSOR_TYPE: Set to Adafruit_DHT.DHT11 or Adafruit_DHT.DHT22 based on your sensor type.
DHT_PIN: The GPIO pin connected to the DHT22 sensor.
THINGSPEAK_API_KEY: Your ThingSpeak API key.

```bash
DHT_SENSOR_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 4
THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_API_KEY"

# Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to create an issue or a pull request in this repository.

# License
This project is licensed under the MIT License.
