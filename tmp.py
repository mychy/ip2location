#!/usr/bin/python
#encoding: utf-8

import geoip2.database
import sys, os, re
import ip2location

reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == '__main__':
  ip = raw_input("Please input an ip address or file name:\n")
  if os.path.isfile(ip) is not True:
    result = ip2location.resolveIp2Geo(ip)
    print ip2location.dumpInfo(result)
  else:
    fin = open(ip, 'r')
    fout = open(ip+'.resolved', 'w')
    for line in fin:
      line = line.strip('\n')
      r = ip2location.resolveIp2Geo(line)
      fout.write(line + ' ' + ip2location.dumpInfo(r))
      continue
    fin.close()
    fout.close()
