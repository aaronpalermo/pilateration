# pilateration
The goal of this project is to evaluate the practicality of using RSSI to calculate the location of a transmitter within a polygon where the verticies are passive WiFi monitors.

## Step 1 [DONE] - collect RSSI for known distances
For a given set of distances and orientations, collect RSSI data.  Distances range from 1ft to 16ft at 1ft increments.  Orientations are all vertical, and consist of different parts of the TX (mobile phone) facing the vertically oriented antenna.  Orientations denote the part of the phone facing the antenna and include: screen, back, left side, and right side.

## Step 2 [DONE] - walk around & collect RSSI
I have 4 sensors, all Raspberry Pis with this identical WiFi adapter. I specifically chose this adapter because of the low cost, monitor mode capability, and single antenna so I won't get any directional gain like I may in dual-antenna setups.

## Step 3 [DONE] - Compare RSSI to distance
Since all 4 of the adapters are identical, hopefully (failed) the RSSI will correspond to a relative distance from the receiver. Then to work out the math and plot (ideally in real-time) the transmitter location within the receiver area.  Antenna and phone orientation make a huge difference here, as much as 10dBm, so accurate distance is tough, but movement and motion tracking is still very viable.

# Hardware
I'll try to keep this current, in case you want to create an identical setup on which to run this software.

## Raspberry Pi(s)
I have several of these, ranging from the original [Model B](https://www.adafruit.com/product/998) up to the [Model 3 B+](https://www.adafruit.com/product/3775). Passive data collection is very low CPU usage, so anything will work as a sensor, so long as the USB adapters are identical, otherwise RSSI measurements won't be very helpful.

## WiFi USB adapters with monitor mode
[Wifi With Antenna For Raspberry Pi](https://www.amazon.com/gp/product/B00H95C0A2/)

![alt text](https://camo.githubusercontent.com/602dac8e9fd58802145e8d2a0e7991383c9dfe08/68747470733a2f2f696d616765732d6e612e73736c2d696d616765732d616d617a6f6e2e636f6d2f696d616765732f492f35315a7a634e5334524f4c2e6a7067 "WIFI USB adapter image")


## Actual Jupyter/Matplotlib output
It's almost a best case scenario, but here is what the matplotlib output should look like, showing the approximate location of a transmitter where the circles almost overlap.
![alt text](https://raw.githubusercontent.com/aaronpalermo/pilateration/master/sample_output.png "Sample output")

# Interesting stuff for later
## Wireshark view filters
Devices looking for APs: wlan.tag && wlan.fc.subtype == 0x4
SSID of AP the deivce with the above filter is looking for: packet.wlan.tag
