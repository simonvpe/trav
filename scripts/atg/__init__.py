#!/usr/bin/env python3

import json, urllib.request
from datetime import datetime

def get_obj(url):
  request = urllib.request.Request(url, None, {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5'
  })
  text = urllib.request.urlopen(request).read()
  return json.loads(text)

def cache_get_obj(url, filename):
  try:
    return open(filename, 'r').read()
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

