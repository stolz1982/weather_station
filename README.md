# weather_station

sudo apt-get install python-pip libusb-dev gcc make vim git 

sudo pip install --upgrade google-auth-oauthlib

pip install gspread oauth2client (if you experience an error apply "export LC_ALL=C"



make all (read below the instructions in detail)


> 4. Weather Station (208,39€)
>
> apllication: http://te923.fukz.org/documentation.html
T0:H0:T1:H1:T2:H2:T3:H3:T4:H4:T5:H5:PRESS:UV:FC:STORM:WD:WS:WG:WC:RC

-  T0    - temperature from internal sensor in °C
-  H0    - humidity from internal sensor in % rel
-  T1..5 - temperature from external sensor 1..4 in °C
-  H1..5 - humidity from external sensor 1...4 in % rel
-  PRESS - air pressure in mBar
-  UV    - UV index from UV sensor
-  FC    - station forecast, see below for more details
-  STORM - stormwarning; 0 - no warning, 1 - fix your dog
-  WD    - wind direction in n x 22.5°; 0 -> north
-  WS    - wind speed in m/s
-  WG    - wind gust speed in m/s
-  WC    - windchill temperature in °C
-  RC    - rain counter (maybe since station starts measurement) as value


   weather forecast means (as precisely as possible)
     0 - heavy snow
     1 - little snow
     2 - heavy rain
     3 - little rain
     4 - cloudy
     5 - some clouds
     6 - sunny>
> Manual: http://www.linux-community.de/ausgaben/linuxuser/2013/06/mit-dem-raspberry-pi-eine-wetterstation-anzapfen/
>
> Alternate Manual: http://www.linux-community.de/ausgaben/linuxuser/2013/06/mit-dem-raspberry-pi-eine-wetterstation-anzapfen/3/#articleInfo
>
> Procurement: https://shop.jacob.de/produkte/tfa-nexus-35.1075-artnr-292610.html?gclid=Cj0KCQjwx43ZBRCeARIsANzpzb-V059Hsf52pOLq_G3-egxjIWfAUuWSohgOgatchh0Y8vgwkIj537AaAlkREALw_wcB

wget http://te923.fukz.org/downloads/te923tool-0.6.1.tgz

tar xvzf te923tool*
cd te923tool*

#in the make file the parameter -lusb needs to be shift to the end of the line
#administrator@KE0915:~/weather_station/te923tool-0.6.1$ cat Makefile 
#all: te923con 
#
#
#te923con: te923con.c te923con.h te923usb.c te923usb.h te923com.c te923com.h
#	gcc -Wall  -o te923con te923con.c te923usb.c te923com.c -lusb



