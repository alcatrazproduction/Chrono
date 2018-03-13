#!/usr/bin/python
######################################################################################
# (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018							#
######################################################################################

class Preferences:
	decoderList				= {}
# Flag		Infos
# 'active'	if decoder is active or not
# 'class'		Type of decoder ( name of the interface class )
# 'type'		The type of line, 0 = finish line, other are partial in sequence !

	decoderList['simulator_FL']	= {
								'active': 	True,
								'port': 		10000,
								'class': 		'simulator',
								'type':		0,
								'howmany':	45,
								'laptime':	30,
								'delay':		0,
								'auto_assign':	True
							}
	decoderList['simulator_LP1']	= {
								'active': 	True,
								'port': 		10001,
								'class': 		'simulator',
								'type':		1,
								'howmany':	45,
								'laptime':	30,
								'delay':		10
							}
	decoderList['simulator_LP2']	= {
								'active': 	True,
								'port': 		10002,
								'class': 		'simulator',
								'type':		2,
								'howmany':	45,
								'laptime':	30,
								'delay':		18
							}
	decoderList['finish']		= {
								'active': 	False,
								'port': 		10010,
								'class': 		'cano',
								'type':		0,
								'device': 	"/dev/ttyUSB0",
								'baud': 		115200
							}
	decoderList['mw4wd']		= {
								'active': 	False,
								'port': 		10010,
								'class': 		'cano',
								'type':		0,
								'device': 	"/dev/ttyACM0",
								'baud': 		115200
							}
	decoderList['partial']		= {
								'active': 	False,
								'port': 		10030,
								'class': 		'remote',
								'type':		1
							}
	defaultSerialDevice			= "/dev/ttyUSB0"
	dataBase					= {}
	dataBase['host'] 			= "localhost"
	dataBase['user']			= "Chrono"
	dataBase['pass']			= "Chrono"
	dataBase['db']				= "Chrono"
