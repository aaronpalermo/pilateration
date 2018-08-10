import pyshark
import hashlib
import time
capture = pyshark.LiveCapture(interface='wlan0mon', display_filter='wlan.ta_resolved contains "c3:58"')

for packet in capture.sniff_continuously():
  #pretty_print('Just arrived:', packet)
  #packet.pretty_print()
  try:
    pkt_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(packet.frame_info.time_epoch))) + str(packet.frame_info.time_epoch)[10:]
  except:
    pkt_time = "no data in pkt"
  
  try:
    pkt_ta = packet.wlan.ta_resolved
  except:
    pkt_ta = "no data in pkt"
    
  try: 
    pkt_rssi = packet.radiotap.dbm_antsignal
  except:
    pkt_rssi = "no data in pkt"
    
  try:
    pkt_data_md5 = hashlib.md5(str(packet.data.data).encode('utf-8')).hexdigest()
  except:
    pkt_data_md5 = "no data in pkt"
    
  print('{0},{1},{2},{3}'.format(pkt_time, pkt_ta, pkt_rssi, pkt_data_md5))
