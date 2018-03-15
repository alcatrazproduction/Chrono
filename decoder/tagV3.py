Tag Heuer Protime Elite Decoder / Tag Heuer by Chronelec - V3 Protocol
----------------------------------------------------------------------

On transponder read, cell or manual trigger, decoder sends PASSING
message.  Host must reply with ACK to get next passing. If no
acknowledge sent, passing is repeated periodically.

Commands
--------

Get Status:
	Request running time, noise and level status from decoder
	command:	ESC + 0x05
	response:	[STATUS]

Start:
	Start decoder
	command:	ESC + 0x07
	response:	[DEPART] or none if decoder already started

Set Config:
	Update decoder configuration
	command:	ESC + 0x08 + 0x08 + [CONFIG] + [CRC] + '>'
	response:	none

Set IP Config:
	Update decoder IP configuration. Note: Decoder must be stopped
	before issuing this command (why?)
	command:	ESC + 0x09 + 0x09 + [IPCONFIG] + [CRC] + '>'
	response:	XPORT specific (TBC)

Get Config:
	Fetch current decoder configuration & identification
	command:	ESC + 0x10
	response:	[DECODERCONF]

Acknowledge:
	Acknowledge last passing sent by decoder/flag ready for next passing
	command:	ESC + 0x11
	response:	none or [PASSING]

Repeat:
	Repeat first unacknowledged passing, else last acknowledged passing
	command:	ESC + 0x12
	response:	[PASSING]

Stop:
	Stop decoder
	command:	ESC + 0x13 + '\'
	response:	[STOP] (even if already stopped)

Set Time:
	Update decoder time of day - also sets running time if decoder
	started and config option "Running time to time of decoder" set
	command:	ESC + 0x48 + [SETTIME] + 't'
	response:	none

Set Date:
	Update decoder date
	command:	ESC + 0x0a + 0x0a + [SETDATE] + [CRC] + '>'
	response:	none

Set STA Level:
	Set detection level on STA channel
	command:	ESC + 0x1e + [SETLEVEL]
	response:	none

Set BOX Level:
	Set Detection level on BOX channel
	command:	ESC + 0x1f + [SETLEVEL]
	response:	none

Stat BXX:
	Request status on remote decoder with id specified in B
	command:	ESC + 0x49 + [B]
	response:	(TBC)

BXX Level:
	Increment all detection levels by 0x10 (Note 2)
	command:	ESC + 0x4e + 0x2b
	response:	none


Messages
--------

PASSING:	'<' + ' ' + CHAN + ' ' + REFID + ' ' + PASSTIME + ' '
                           + POWER + ' ' + PASSCOUNT + ' '
                           + BATTERY + ' ' + CHARSUM + '>' + [NEWLINE]

CHAN:		'MAN'|'BOX'|'STA'...
REFID:		'000000'->'999999'  six digits, left zero pad
PASSTIME:	'hh:mm'ss"dcm'	left zero pad
POWER:		'00'->'99'	passing power
PASSCOUNT:	'00'->'01'	count of times in loop (question?)
BATTERY:	'0'|'1'|'2'|'3'	0/high -> 3/low
CHARSUM:	'0000'->'8192'	sum of bytes from offset 1-32

STATUS:		'[' + 'hh:mm'ss"' + ' ' + 'NS' + ' ' + 'NB'
                                  + ' ' + 'LS' + ' ' + 'LB' + ']' + [NEWLINE]
                        hh: hour eg 03
                        mm: minute eg 59
                        ss: second eg 31
			Noise: NS (STA) and NB (BOX) '00' -> '99'
			Levels: LS (STA) and LB (BOX) '00' -> '99'
			Note: time reported is running time, and will
			be 00:00'00" when decoder is stopped.

DEPART:		'DEPART_' + [DATESTR] + '__' + [TODSTR] + [NEWLINE]

STOP:		'STOP_' + [DATESTR] + '__' + [TODSTR] + [NEWLINE]

DATESTR:	'YYYY-MM-DD'
			YYYY: year eg 2012
			MM: month eg 02
			DD: day of month eg 12

TODSTR:		'hh:mm:ss'
			hh: hour eg 03
			mm: minute eg 59
			ss: second eg 31

ESC:		0x1b
NACK:		0x07
CRC:		CRC-16/MCRF4XX on bytes following ESC (Note 1)
B:		'1'|'2'|'3'...'7'	 (0x30 + id)
SETLEVEL:	level as two ascii chars eg: 45 => '4' + '5' or 0x34 + 0x35
SETTIME:	h + m + s
			eg:	21h03:45	=>	0x15 0x03 0x2d
SETDATE:	D + M + Y	(Y == year - 2000)
			eg:	23/05/12	=>	0x17 0x05 0x0c
DECODERCONF:	'+' + '+' + '+' + [CONFIG] + [LEVELS] + [IPCONFIG]
				+ [IDENT] + [VERSION] + '>' + [NEWLINE]

NEWLINE:	CR + LF
CR:		0x0d
LF:		0x0a

LEVELS (2 bytes):
0	STA level 30 => 0x30
1	BOX level "

IDENT (4 bytes):
0-3	'0129' => 0x00 + 0x01 + 0x02 + 0x09

VERSION (4 bytes): (TBC)
0	0x13	?
1-3	'201'	version string?

CONFIG (27 bytes):
offset	option			values
0	Time of day 		0x00=>runtime, 0x01=>timeofday
1	GPS Sync		0x00=>off, 0x01=>on
2	Time Zone Hour		0x10=>10h, 0x09=>9h
3	Time Zone Min		0x00=>:00, 0x30=>:30
4	Distant 232/485 select	0x00=>232, 0x01=>485	(check)
5	Distant Fibre Optic	0x00=>no, 0x01=>yes
6	Print pass on serial	0x00=>no, 0x01=>yes
7	Detect maximum		0x00=>no, 0x01=>yes
8	Protocol		0x00=>Cv3,0x01=>AMB,0x02=>Cv2
9	Generate sync		0x00=>no, 0x01=>yes
10	Sync interval min	0x01=>1min, ... , 0x99=>99min
11	Sync ToD on CELL	0x00=>off, 0x01=>on
12	Sync Time hours		0x00=>0h, ... , 0x23=>23h (Question Function?)
13	Sync Time min		0x00=>:00, ... , 0x59=>:59
14      Active Loop             0x00=>passive, 0x01=>powered (active)
15,16	STA Tone		0x12,0x34=>1234Hz 0x00,0x00=>no tone
17,18	BOX Tone		"
19,20	MAN Tone		"
21,22	CEL Tone		"
23,24	BXX Tone		"
25,26	STA+BOX Levels		eg 0x45,0x92 => 45,92 (note 2)

IPCONFIG (16 bytes):

0-3	IP Address, net order eg: 192.168.95.252 => 0xc0 + 0xa8 + 0x5f + 0xfc
4-7	Netmask, "
8-11	Gateway, "
12-15	Remote host, "

NOTES:

	1.	CRC is computed with the following parameters:
		model:		crc-16
		poly:		0x1021
		init:		0xffff
		reflect-in:	yes
		reflect-out:	yes
		xor-out:	0x0000

	2.	Detection level appears to be stored or manipulated
		as byte, but displayed as decimal equivalent of hex string.
		When incrementing with command BXX Level, STA is wrapped to
		zero when STA level is > 0x99. BOX level will increment
		> 0x90 all the way to 0xff as long as STA is < 0xa0.
		Side effects of this have not been tested.
