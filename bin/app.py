#!/bin/python2
# -*- coding: utf-8 -*-


import sys
sys.path.append('.') # '/var/www/'

import web
from gothonmap import map

urls = (
    '/', 'Index',
    '/f', 'Indexf',    
    '/game', 'GameEngine',
    '/jeu', 'JeuEngine'    
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, 
                                  initializer = {'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base = "layout_plus") # /templates/layout_plus.html

# ENGLISH
class Index(object):
	"""
	It opens the website (root page). It redirects to /game, the game page where the first room is loaded. 
	"""
	
	def GET(self): # this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")

# FRANCAIS
class Indexf(object):
	"""
	When French selected, it redirected to /jeu, the French game page where the first room is load in French.
	"""
	
	def GET(self): # this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/jeu")

# ENGLISH
class GameEngine(object):
	"""
	This is the core of the game engine (the loop). GET generates a room according to the game map and suggests inputs to the player for the next things to happen. POST sends these inputs to the game map and seeks new information in the map (variables) for the GET function. The loop continues. 
	"""

	def GET(self):
		if session.room:
			return render.show_room_plus(room = session.room) # /templates/show_room_plus.html

	def POST(self):
		form = web.input(action = None)
		if (session.room.name == "The Armory") and (session.room.paths.has_key(form.action) == False):
			form.action = '*'
		if session.room and form.action: # if all True, it executes the next line; otherwise, it jumps over it
			if session.room.paths.has_key(form.action): # if the entry is what is expected in the dictionary (it stops errors, mispellings, missing values), it executes the next line; otherwise, it jumps over it
				session.room = session.room.go(form.action)
		web.seeother("/game")

# FRANCAIS
class JeuEngine(object):
	"""
	This is the core of the game engine (the loop) as with class GameEngine, but with French variables in the map.
	"""

	def GET(self):
		if session.room:
			return render.show_room_plusf(room = session.room) # /templates/show_room_plusf.html

	def POST(self):
		form = web.input(action = None)
		if (session.room.namef == "L'Arsenal") and (session.room.paths.has_key(form.action) == False):
			form.action = '*'
		if session.room and form.action:
			if session.room.paths.has_key(form.action):
				session.room = session.room.go(form.action)
		web.seeother("/jeu")

if __name__ == "__main__":
    app.run()
