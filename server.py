#!/usr/bin/env python
# Modified from source found here: https://gist.github.com/mildred/67d22d7289ae8f16cae7

# Expected client usage:
# curl -X PUT -d "2019-02-10 18:27:44.660371,a7:c6:f5:a3:54:rd,-83,no data in pkt" http://10.10.0.2:8000

import http.server
import os

logfile = {}


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_PUT(self):
    path = self.translate_path(self.path)
    length = int(self.headers['Content-Length'])
    
    sensor_ip = str(self.client_address[0])
    input_data = str(self.rfile.read(length)).split(',')
    timestamp, mac, dbm, data_md5 = input_data
    print(mac)
    
    if not sensor_ip in logfile:
      logfile[sensor_ip] = {}
      #logfile[sensor_ip][mac] = [timestamp, dbm, data_md5]
    if not input_data[1] in logfile[sensor_ip]:
      logfile[sensor_ip][mac] = []

    logfile[sensor_ip][mac].append([timestamp, dbm, data_md5])

    print(logfile)

    self.send_response(201, "Created")
    self.end_headers()

if __name__ == '__main__':
  http.server.test(HandlerClass=HTTPRequestHandler, port=8000, bind='')
  
