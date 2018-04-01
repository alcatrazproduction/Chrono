#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018								 #
######################################################################################

import importlib
import Globals


class decoder_task():
	soc_ip		= "224.3.29.71"

	def __init__(self, decoder, name):
		print( decoder )
		try:
			d = Globals.decoder[ name ]
			return
		except:
			d						= dict()
			m						= importlib.import_module( "decoder." + decoder['class'] )
			d['class']				= m.decoder()
			d['multi_ip']			= self.soc_ip
			d['port']				= decoder['port']
			d['preferences']		= decoder

			p = d['class'].createThread( d,  decoder, name )
			d['pid']				= p
			Globals.decoder[name]	= d
			if p is not None:
				p.setDaemon( True )
				p.start()

