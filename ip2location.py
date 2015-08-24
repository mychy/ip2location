#!/usr/bin/python
#encoding: utf-8

import geoip2.database
import sys, os, re

reload(sys)
sys.setdefaultencoding( "utf-8" )

reobj = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')

db_file = 'GeoLite2-City.mmdb'
reader = geoip2.database.Reader(db_file)

def dumpInfo(geoinfo):
  result = ''
  if geoinfo is False or geoinfo is None:
    return '\n'
  result += ' ' + geoinfo.country.names['zh-CN']
  try:
    if geoinfo.city.name is not None:
      result += ' ' + geoinfo.city.names['zh-CN']
  except Exception, e:
      result += ' ' + geoinfo.city.name
  result += '\n'
  return result

def resolveIp2Geo(ipAddr):
  result = None
  try:
    result = reader.city(ipAddr)
  except Exception, e:
    print str(e)
  return result

def searchIpAddr(string):
  return reobj.search(string)
  return ipAddrs

