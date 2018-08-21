#!/usr/bin/env python
import subprocess
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep, gmtime, strftime, localtime
WORKDIR = "/home/pi/weather_station/"
command1 = '/home/pi/weather_station/te923tool-0.6.1/te923con'
p = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
##print "Command output : ", output
##print "Command exit status/return code : ", p_status 


def string_check(parameter,typ,multiplier=1):
    try:
        if complex(parameter): # for int, long, float and complex
            if typ == "f":
                return float(parameter) * multiplier
            elif typ == "i":
                return int(parameter) * multiplier
            else:
                return "" 
    except ValueError:
        return ""

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

f = "f" #FLOAT
i = "i" #INTEGER

#1534271542:26.05:56:21.00:77:i:i:i:i:i:i:i:i:1006.6:i:5:0:11:1.7:1.4:19.2:76
DT,TIN,HIN,TOUT,HOUT,T2,H2,T3,H3,T4,H4,T5,H5,PRESS,UV,FC,STORM,WD,WS,WG,WC,RC = output.split(":")

TIN = string_check(TIN,f)
HIN = string_check(HIN,f)
TOUT = string_check(TOUT,f)
HOUT = string_check(HOUT,f)
PRESS = string_check(PRESS,f)
FC = string_check(FC,i)
print STORM

if FC == 0:
	FC_STR = "Heavy Snow"
elif FC == 1:
	FC_STR = "Little Snow"
elif FC == 2:
	FC_STR = "Heavy Rain"
elif FC == 3:
	FC_STR = "Little Rain"
elif FC == 4:
	FC_STR = "Cloudy"
elif FC == 5:
	FC_STR = "Some Clouds"
elif FC == 6:
	FC_STR = "Sunny"
else:
    FC_STR = ""

WD = string_check(WD,f,22.5)
WS = string_check(WS,f,3.6)
WG = string_check(WG,f,3.6)
WC = string_check(WC,f)
RC = string_check(RC,f)


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/weather_station/weather_sheet.json', scope) # rpi_$
client = gspread.authorize(creds)
sheet = client.open('Remote Monitoring')  # Google Spreadsheet name 'Remote Monitoring'
worksheet = sheet.worksheet("Weather") # Worksheet name 'Weather'
now = strftime("%d %b %Y %H:%M:%S", localtime()) # get current timestamp

data_set = [now, TIN, HIN, TOUT, HOUT, PRESS, FC_STR, WD, WS, WG, WC, RC]      # data package to be sent to Google sheet
worksheet.append_row(data_set)  # append the targetted google sheet with the above data set

