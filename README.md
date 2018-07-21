# pilateration
The goal of this project is to evaluate the practicality of using RSSI to calculate the location of a transmitter within a polygon where the verticies are passive WiFi monitors.

## Step 1 - walk around & collect RSSI
I have 4 sensors, all Raspberry Pis with this identical WiFi adapter. I specifically chose this adapter because of the low cost, monitor mode capability, and single antenna so I won't get any directional gain like I may in dual-antenna setups.

## Step 2 - Compare RSSI to distance
Since all 4 of the adapters are identical, hopefully the RSSI will correspond to a relative distance from the receiver. Then to work out the math and plot (ideally in real-time) the transmitter location within the receiver area.

# Hardware
I'll try to keep this current, in case you want to create an identical setup on which to run this software.

## Raspberry Pi(s)
I have several of these, ranging from the original [Model B](https://www.adafruit.com/product/998) up to the [Model 3 B+](https://www.adafruit.com/product/3775). Passive data collection is very low CPU usage, so anything will work as a sensor, so long as the USB adapters are identical, otherwise RSSI measurements won't be very helpful.

## WiFi USB adapters with monitor mode
[Wifi With Antenna For Raspberry Pi](https://www.amazon.com/gp/product/B00H95C0A2/)

![alt text](https://camo.githubusercontent.com/602dac8e9fd58802145e8d2a0e7991383c9dfe08/68747470733a2f2f696d616765732d6e612e73736c2d696d616765732d616d617a6f6e2e636f6d2f696d616765732f492f35315a7a634e5334524f4c2e6a7067 "WIFI USB adapter image")
