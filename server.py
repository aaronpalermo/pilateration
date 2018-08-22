#!/usr/bin/env python
# HTTP server code from: https://gist.github.com/mildred/67d22d7289ae8f16cae7
# Threading code from: http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/

# Expected client usage:
# curl -X PUT -d "2019-02-10 18:27:44.660371,a7:c6:f5:a3:54:rd,-83,no data in pkt" http://10.10.0.2:8000

import threading
import time
import http.server
import os
from collections import deque

logfile = {}
print("LEFT        BACK-LEFT      BACK-RIGHT        RIGHT")
left_dbm = ''
back_left_dbm = ''
back_right_dbm = '' 
right_dbm = ''

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_PUT(self):
    path = self.translate_path(self.path)
    length = int(self.headers['Content-Length'])
    
    sensor_ip = str(self.client_address[0])
    input_data = str(self.rfile.read(length)).split(',')
    
    timestamp = 0
    try:
      timestamp, mac, dbm, data_md5 = input_data
    except:
      #got some garbage in, so throwing away that line
      pass
        
    if (timestamp != 0):    
      #print(mac)

      if not sensor_ip in logfile:
        logfile[sensor_ip] = {}
        #logfile[sensor_ip][mac] = [timestamp, dbm, data_md5]
      if not input_data[1] in logfile[sensor_ip]:
        #logfile[sensor_ip][mac] = []
        logfile[sensor_ip][mac] = deque([],10)

      logfile[sensor_ip][mac].append([timestamp, dbm, data_md5])

      self.send_response(201, "Created")
      self.end_headers()
  def log_message(self, format, *args):
    return

class ThreadingExample(object):
  """ Threading example class
  The run() method will be started and it will run in the background
  until the application exits.
  """

  def __init__(self, interval=1):
    """ Constructor
    :type interval: int
    :param interval: Check interval, in seconds
    """
    self.interval = interval

    thread = threading.Thread(target=self.run, args=())
    thread.daemon = True                            # Daemonize thread
    thread.start()                                  # Start the execution

  def run(self):
    """ Method that runs forever """
    http.server.test(HandlerClass=HTTPRequestHandler, port=8000, bind='')

example = ThreadingExample()

print()
