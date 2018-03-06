class Preferences:
	decoderList				= {}
	decoderList['simulator']		= {	'active': 	True,
								'port': 		10000,
								'class': 		'simulator',
								'howmany':	20,
								'laptime':	30,
								'delay':		0
							}
	decoderList['finish']		= {	'active': 	True,
								'port': 		10001,
								'class': 		'cano',
								'device': 	"/dev/ttyUSB0",
								'baud': 		115200
							}
	decoderList['partial']		= {	'active': 	False,
								'port': 		10002,
								'class': 		'remote'
							}
	defaultSerialDevice			= "/dev/ttyUSB0"
	dataBase					= {}
	dataBase['host'] 			= "localhost"
	dataBase['user']			= "Chrono"
	dataBase['pass']			= "Chrono"
	dataBase['db']				= "Chrono"
