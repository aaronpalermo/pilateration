#!/usr/bin/python3

import pyshark
import hashlib
import time
import requests

capture = pyshark.LiveCapture(interface='wlan1mon', bpf_filter='wlan src a8:96:75:c3:58:0d')
status = '.'
print("Sending packets to web server")

for packet in capture.sniff_continuously():
  try:
    pkt_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(packet.frame_info.time_epoch))) + str(packet.frame_info.time_epoch)[10:]
  except:
    pkt_time = "no time in pkt"

  try:
    pkt_ta = packet.wlan.ta_resolved
  except:
    pkt_ta = "no mac in pkt"

  try:
    pkt_rssi = packet.radiotap.dbm_antsignal
  except:
    pkt_rssi = "no dbm in pkt"

  try:
    pkt_data_md5 = hashlib.md5(str(packet.data.data).encode('utf-8')).hexdigest()
  except:
    pkt_data_md5 = "no data in pkt"

  #print('{0},{1},{2},{3}'.format(pkt_time, pkt_ta, pkt_rssi, pkt_data_md5))
  payload = '{0},{1},{2},{3}'.format(pkt_time, pkt_ta, pkt_rssi, pkt_data_md5)
  #print(payload)
  print(status, end='\r')
  if len(status) < 80:
    status = status + '.'
  else:
    print("                                                                                     ", end='\r')
    status = '.'

  try:
    r = requests.put("http://172.24.1.1:8000", data=payload)
  except:
    print("Error contacting web server")
