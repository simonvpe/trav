#!/usr/bin/env python3

import json, pycurl
from datetime import datetime
from io import BytesIO

def get_obj(url):
  buffer = BytesIO()
  c = pycurl.Curl()
  c.setopt(c.URL, url)
  c.setopt(c.WRITEFUNCTION, buffer.write)
  c.setopt(c.USERAGENT, 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')
  c.setopt(c.HTTPHEADER, ('Accept:','application/json'))
  c.perform()
  c.close()
  return json.loads(buffer.getvalue())

def cache_get_obj(url, filename):
  try:
    return json.loads(open(filename, 'r').read())
  except:
    data = get_obj(url)
    open(filename, 'w').write(json.dumps(data))
    return data

def get_day(date):
  url = date.strftime("https://www.atg.se/services/racinginfo/v1/api/calendar/day/%Y-%m-%d")
  filename = date.strftime(".cache/days/%Y-%m-%d.json")
  return cache_get_obj(url, filename)

def get_game(game):
  url = "https://www.atg.se/services/racinginfo/v1/api/games/%s" % game
  filename = ".cache/games/%s" % game
  return cache_get_obj(url, filename)

def get_race(race):
  url = "https://www.atg.se/services/racinginfo/v1/api/races/%s" % race
  filename = ".cache/races/%s" % race
  return cache_get_obj(url, filename)

