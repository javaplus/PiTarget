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

last_read = 0       # this keeps track of the last potentiometer value
tolerance = 7400     # to keep from being jittery we'll only change
		# volume when the pot has moved a significant amount
		# on a 16-bit ADC


while True:
	# we'll assume that the pot didn't move
	vibration_value_changed = False

	# read the analog pin
	vibration_value = chan0.value

	# voltage = chan0.voltage

#	print('ADC Voltage: ' + str(chan0.voltage) + 'V')
	print('Channel VALUE=' + str(vibration_value)) 
	# how much has it changed since the last read?
	# pot_adjust = abs(vibration_value - last_read)

	if vibration_value > tolerance:
	    vibration_value_changed = True

	if vibration_value_changed:

	    #for x in range(1000): 
            # print('Changed value = {change}%' .format(change = pot_adjust))
            print('Big Hit value!!!!!!!!!!!!!!!! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ' + str(vibration_value))
	    # save the potentiometer reading for the next loop
            # last_read = vibration_value

	    # hang out and do nothing for a half second if hit
            time.sleep(0.5)
