import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ' + str(chan0.voltage) + 'V')

hit_tolerance = 7400     # amount of vibration to count as a hit.


while True:
	
	# read the analog pin
	vibration_value = chan0.value

	# voltage = chan0.voltage

#	print('ADC Voltage: ' + str(chan0.voltage) + 'V')
	print('Channel VALUE=' + str(vibration_value)) 

	if vibration_value > hit_tolerance:
	    
	    print('Big Hit value!!!!!!!!!!!!!!!! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ' + str(vibration_value))
        
		# Broadcast an event

	    # hang out and do nothing for a second if hit
        time.sleep(1)
