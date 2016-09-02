#!/usr/bin/env python
#
# GrovePi Library for using the Grove - RTC v1.1(http://wiki.seeedstudio.com/wiki/Grove_-_RTC)
#		
# This example returns time stored in the Real time clock(RTC)- DS1307
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import time
import datetime
import grove_i2c_rtc_ds1307

# Main Program

print ""
print "               RTC DS1307                    "
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
ds1307 = grove_i2c_rtc_ds1307.rtc()

# Writes the date and time of Raspberry Pi into DS 1307
ds1307.write_now()

## Another way to write the date and time to DS1307 -Uncomment the following 3 lines##

# Writes the date and time stored in the object "dt" into DS 1307
#dt = datetime.datetime.strptime("02/09/16 17:00", "%d/%m/%y %H:%M")
#ds1307.write_datetime(dt)

# Main Loop - sleeps 10 Seconds, then reads and prints values of all clocks

while True:
    # Prints the date and time of Raspberry Pi
	print ""
	print ""
	print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	# Prints the date and time of DS 1307
	print "DS1307=\t\t%s" % ds1307.read_datetime()
	# Waits for 10 seconds and then again reads and prints the time of both the clocks
	time.sleep(10.0)