#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

networkJson = urlfetch.fetch("https://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタトクカシーーになるように自分で直してください！
  patoka = request.args.get('a','')
  takushi = request.args.get('b','')
  patatoku = ''
  if len(patoka) == len(takushi):
    for i, pa in enumerate(patoka):
      patatoku += pa
      patatoku += takushi[i]

  elif len(patoka) > len(takushi):
    dif = len(patoka)-len(takushi)
    for i, ta in enumerate(takushi):
      patatoku += patoka[i]
      patatoku += ta
    for i in range(dif):
      i += len(takushi)
      patatoku += patoka[i]

  elif len(patoka) < len(takushi):
    dif = len(takushi) - len(patoka)
    for i ,pa in enumerate(patoka):
      patatoku += pa
      patatoku += takushi[i]
    for i in range(dif):
      i += len(patoka)
      patatoku += takushi[i]
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=patatoku)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def DFS(que,to_station):
  

def norikae():
  from_station = request.args.get('from')
  to_station = request.args.get('to')
  route = []  
  que = []
  for i in range(len(network)):
    if from_station in network[i]["Stations"]:
      route.append(from_station)
      lis = network[i]["Stations"]
      if to_station in lis:
        route.append(to_station)
        break
      else:
        que.append(lis)
        DFS(que,to_station)
  return render_template('norikae.html', network=route)

