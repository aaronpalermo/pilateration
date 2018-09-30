## Now running on the ESP8266 (NodeMCU)
This is the simplest method I could find to collect Probe Requests on the ESP8266.  Full credit to Angel SB Martin, who I pulled nearly all of this code from.  My only changes were adding a struct for PROBE_REQ, some formatting changes, and frequency hopping.

The original code base that I borrowed heavily from is here:<BR>
https://github.com/n0w/esp8266-simple-sniffer

## Instructions:
Use the Arduino IDE, open main.ino and upload to your device.  If it doesn't work, use the power of the Internet to find out why.

## More hardware
The exact device I'm using is about half the price on what I spent on USB adapters previously.  You can find the NodeMCU ESP-12E on amazon here: <BR>
https://www.amazon.com/gp/product/B010N1SPRK

![](https://images-na.ssl-images-amazon.com/images/I/71ioYKGjw0L._SL1010_.jpg)