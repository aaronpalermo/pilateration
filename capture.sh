mkdir -p /opt/wifi
chmod 777 /opt/wifi/

# I lock collection to channel 11 since we have known 
# transmitters and we want to reduce collection initially 
# until we know if RSSI is actually going to tell us 
# anthing about relative distance between transmitter and receiver
# airmon-ng starts wlan1 in monitor mode on channel 11
airmon-ng start wlan1 11

# set the timestamp variable so I write to a new file
# every time the script is run
TIMESTAMP=$(date +%Y.%m.%d-%H.%M.%S)

# run tcpdump with some args
# -tttt = verbose date/time stamp in human readable format
# -i wlan1mon = interface is wlan1mon
# -e = print the link-level header of each packet - so we can collect RSSI & MAC
#      even if we don't know (or care to know) the WPA keys
# -s 256 = we only want the first 256 bytes of the packet, not the whole thing
# not subtype beacon = don't look at router beacons.  These are horribly noisy.
#tcpdump -tttt -i wlan1mon -e -s 256 not subtype beacon > /opt/wifi/$TIMESTAMP.txt &

#run tcpdump to capture from a MAC address where 0xc8 is the 8th byte
#tcpdump -tttt -i wlan1mon -e -s 256 'ether[8]=0x58' > /opt/wifi/$TIMESTAMP.txt &

# Moving this to tshark becuase it has awesome filtering and display capabilities
# -s 256 = only look at the first 256 bytes of each packet
# -Y = use a display filter as a capture filter.  AWESOME!
# wlan.ta_resolved contains "c3:58" = only capture packets where the last 3 bytes of the MAC contain "c3:58"
# wlan.bssid != wlan.ta = ensures we don't capture any traffic from routers or access points
# -T fields = specify which fields to output
# -E header=y -E separator=, -E quote=d  = ouptut in a nice CSV format
# -e frame.time_epoch = show frame time (according to recevier)
# -e wlan.ta_resolved = show mac address with first 3 bytes shown as vendor
# -e wlan_radio.signal_dbm = output signal strength
# - e wlan.fcs = frame check sequence (crc32) value to help determine uniqueness of a frame

tshark -s 256 -i wlan1mon -Y 'wlan.ta_resolved contains "c3:58" && wlan.bssid != wlan.ta' -T fields -e frame.time_epoch -e wlan.fcs -e wlan.ta_resolved -e wlan_radio.signal_dbm -E header=y -E separator=, -E quote=d > /opt/wifi/$TIMESTAMP.txt &




