#!/usr/bin/env python 
import socket
import re
import argparse

parser = argparse.ArgumentParser(description='Script for setting Heos volume.')
parser.add_argument('-i','--ip',help='Heos IP address', required=True)
parser.add_argument('-p','--pid',help='Heos PID ID', required=True)
parser.add_argument('-v','--volume', help='Input volume',required=True)
args = parser.parse_args()

volume=args.volume
pid=args.pid
TCP_IP=args.ip
TCP_PORT = 1255
BUFFER_SIZE = 1024
MESSAGE = "heos://player/set_volume?pid=" +pid + "&level=" + volume
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
