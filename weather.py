#!/usr/bin/env python
import subprocess
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

command1 = '/home/administrator/weather_station/te923tool-0.6.1/te923con'
p = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
##print "Command output : ", output
##print "Command exit status/return code : ", p_status 

##-  T0    - temperature from internal sensor in C
##-  H0    - humidity from internal sensor in rel
##-  T1..5 - temperature from external sensor 1..4 in C
##-  H1..5 - humidity from external sensor 1...4 in % rel
##-  PRESS - air pressure in mBar
##-  UV    - UV index from UV sensor
##-  FC    - station forecast, see below for more details
##-  STORM - stormwarning; 0 - no warning, 1 - fix your dog
##-  WD    - wind direction in n x 22.5; 0 -> north
##-  WS    - wind speed in m/s
##-  WG    - wind gust speed in m/s
##-  WC    - windchill temperature in C
##-  RC    - rain counter (maybe since station starts measurement) as value
##
##
##   weather forecast means (as precisely as possible)
##     0 - heavy snow
##     1 - little snow
##     2 - heavy rain
##     3 - little rain
##     4 - cloudy
##     5 - some clouds
##     6 - sunny

#1534271542:26.05:56:21.00:77:i:i:i:i:i:i:i:i:1006.6:i:5:0:11:1.7:1.4:19.2:76
DT,TIN,HIN,TOUT,HOUT,T2,H2,T3,H3,T4,H4,T5,H5,PRESS,UV,FC,STORM,WD,WS,WG,WC,RC = output.split(":")
print "TIN: ", TIN
print "HIN0: ", HIN
print "TOUT: ", TOUT
print "HOUT: ", HOUT
print "PRESS: ", PRESS
print "WIND DIRECTION: ", WD
print "WIND SPEED: ", WS
print "WIND GUST: ", WG
print "WIND CHILL: ", WC
print "RAIN COUNTER: ", RC

#needs to be tested
#pi = 3.1415926
#precision = 4
#print( "{:.{}f}".format( pi, precision ) )

#scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('rpi_googlesheet.json', scope) # rpi_$
#client = gspread.authorize(creds)
#sheet = client.open('Remote Monitoring')  # Google Spreadsheet name 'Remote Monitoring'
#worksheet = sheet.worksheet("Weather") # Worksheet name 'Weather'
