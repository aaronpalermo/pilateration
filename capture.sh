sudo mkdir -p /opt/wifi
sudo chmod 777 /opt/wifi/

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
tcpdump -tttt -i wlan1mon -e -s 256 not subtype beacon > /opt/wifi/$TIMESTAMP.txt &


