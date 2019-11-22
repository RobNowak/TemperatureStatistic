"""
A python script to measure the temperature and write it to prometheus
"""

import time
from decimal import Decimal
from prometheus_client import start_http_server, Gauge

# Create a metric to track time spent and requests made.
TEMPERATURE = Gauge('temperature_in_degrees', 'Temperature measured with sensor')

def measure():
    """Measures the temperature and write it to a prometheus gauge"""
    sensor_data = open('/sys/bus/w1/devices/28-03199779b9e5/w1_slave')
    data_lines = sensor_data.readlines()
    temperature = Decimal(data_lines[1].split('=')[1].strip())/1000
    TEMPERATURE.set(temperature)
    sensor_data.close()
    time.sleep(60)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        measure()
