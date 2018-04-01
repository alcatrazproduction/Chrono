/*
 * Cano Decoder simulator, this will simulate track with rider. 
 */

#include <MsTimer2.h>
#include <string.h>


#define  sline(a) Serial.print( a )
#define  turn (1000*30)
unsigned char digits[]                = "0123456789ABCDEF";
volatile unsigned char message[256]; 
volatile  bool             ack        = true;
volatile  int              lasttp     = 0;
volatile  bool             started    = true;

int                        theYear    = 2018;
int                        theMounth  = 4;
int                        theDay     = 1;

int                        theHours   = 17;
int                        theMinutes = 00;
int                        theSeconds = 00;

int                        staLevel   = 30;
int                        boxLevel   = 30;

unsigned long  transponderList[][3] =
{
    {351957, 0, 0},
    {688158, 0, 0},
    { 73479, 0, 0},
    {572215, 0, 0},
    {748687, 0, 0},
    {961721, 0, 0},
    {564690, 0, 0},
    {   513, 0, 0},
    { 91953, 0, 0},
    { 99608, 0, 0},
    {531106, 0, 0},
    {110101, 0, 0},
    {220202, 0, 0},
    {330303, 0, 0},
    {440404, 0, 0},
    {550505, 0, 0},
    {660606, 0, 0},
    {770707, 0, 0},
    {880808, 0, 0},
    {990909, 0, 0},
};
char  test_passing[]  = "<STA 006141 00:02'57\"541 38 07 0 1569>";
typedef unsigned char ubyte;

class passing
{
  public:
          ubyte     startflag,
                    loop_id[3],
                    space1,
                    transponder[6],
                    space2,
                    hours[2],
                    sep1,
                    minutes[2],
                    sep2,
                    secondes[2],
                    sep3,
                    milli[3],
                    space3,
                    power[2],
                    space4,
                    loop_cnt[2],
                    space5,
                    btpower,
                    space6,
                    checksum[4],
                    endflag,
                    zero,
                    pad[20];
            
  passing( void )
  {
    memset( &startflag,' ',&zero-&startflag );     //  set all to space
    startflag =    '<';
    sep1 =         ':';
    sep2 =         '\'';
    sep3 =         '"';
    endflag =      '>';
    zero =         0;
  };

  passing( char *lid, int tp, int bpwd, int pwd )
  {
  unsigned long _milli;
  unsigned int  hrs,mins,secs;
  
    memset( &startflag,0,&zero-&startflag );     //  set all to space

    _milli  = transponderList[tp][1];
    hrs     = (_milli / ( 1000 * 60 * 60 ) );
    mins    = (_milli / ( 1000 * 60 ) ) % 60;
    secs    = (_milli / ( 1000  ) ) % 60;
    _milli  = _milli % 1000;
    sprintf( (char * )&startflag,
      "<%c%c%c %6.6ld %2.2d:%2.2d'%2.2d\"%3.3d %2.2d %2.2ld %1.1d xxxx>",
      lid[0],lid[1],lid[2],transponderList[tp][0], hrs, mins,
      secs, (int)_milli, pwd%100, transponderList[tp][2]%100,bpwd%10);

    doCheckSum();
  }

  void doCheckSum(void)
  {
  unsigned int   compute = 0;
  
        for(int i = 1; i< 33; i++ )
          compute   += (&startflag)[i];
        sprintf((char *) &checksum,"%4.4d>",0x0000FFFF&compute);
  };

};

void  createMsg( int tp, unsigned long time )
{
 int i;

   if( ack )
   {
      ack                           =  false;
      lasttp                        =  tp;
      transponderList[tp][1]        =  time;
      transponderList[tp][2]        += 1;
      passing  *p = new passing("STA", lasttp, 3,80);
      snprintf( &message[0],sizeof( message ),"%s\r\n",p);
      delete( p );
   }
   else
   {
      passing  *p = new passing("STA", lasttp, 3,80);
      snprintf( &message[0],sizeof( message ),"%s\r\n",p);
      delete( p );    
   }
}

/*
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// (c) Yves Huguenin, yves.huguenin@free.fr, mars 2018              //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Decoder interface class to be dinamicaly loaded               //
// main entry point is member function createThread( self, storage, pref,name )    //
// Input:                                //
// storage:    Dictionary with all the needed infos            //
//       multi_ip    multicast ip                //
//       port      the assigned port             //
// pref:   The preferences Dict ( all the settings )         //
// name:   the class name                      //
//                                 //
// Return the task pointer                       //
// the class must be decoder, and not the filename !             //
//                                 //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Chronelec Protime Elite Decoder /  Chronelec - V3 Protocol        //
// on the preference must provide:                   //
//   device  = serial device name ( Unix = /dev/tty....; Win = COMx )    //
//   baud    = baud rate ( default: 115200 )             //
//                                 //
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// On transponder read, cell or manual trigger, decoder sends PASSING
// message.  Host must reply with ACK to get next passing. If no
// acknowledge sent, passing is repeated periodically.
//
// Commands
// --------
//
// Get Status:
//   Request running time, noise and level status from decoder
//   command:  ESC + 0x05
//   response: [STATUS]
// Start:
//   Start decoder
//   command:  ESC + 0x07
//   response: [DEPART] or none if decoder already started
//
// Set Config:
//   Update decoder configuration
//   command:  ESC + 0x08 + 0x08 + [CONFIG] + [CRC] + '>'
//   response: none
//
// Set IP Config:
//   Update decoder IP configuration. Note: Decoder must be stopped
//   before issuing this command (why?)
//   command:  ESC + 0x09 + 0x09 + [IPCONFIG] + [CRC] + '>'
//   response: XPORT specific (TBC)
//
// Get Config:
//   Fetch current decoder configuration & identification
//   command:  ESC + 0x10
//   response: [DECODERCONF]
//
// Acknowledge:
//   Acknowledge last passing sent by decoder/flag ready for next passing
//   command:  ESC + 0x11
//   response: none or [PASSING]
//
// Repeat:
//   Repeat first unacknowledged passing, else last acknowledged passing
//   command:  ESC + 0x12
//   response: [PASSING]
//
// Stop:
//   Stop decoder
//   command:  ESC + 0x13 + '\'
//   response: [STOP] (even if already stopped)
//
// Set Time:
//   Update decoder time of day - also sets running time if decoder
//   started and config option "Running time to time of decoder" set
//   command:  ESC + 0x48 + [SETTIME] + 't'
//   response: none
//
// Set Date:
//   Update decoder date
//   command:  ESC + 0x0a + 0x0a + [SETDATE] + [CRC] + '>'
//   response: none
//
// Set STA Level:
//   Set detection level on STA channel
//   command:  ESC + 0x1e + [SETLEVEL]
//   response: none
//
// Set BOX Level:
//   Set Detection level on BOX channel
//   command:  ESC + 0x1f + [SETLEVEL]
//   response: none
//
// Stat BXX:
//   Request status on remote decoder with id specified in B
//   command:  ESC + 0x49 + [B]
//   response: (TBC)
//
// BXX Level:
//   Increment all detection levels by 0x10 (Note 2)
//   command:  ESC + 0x4e + 0x2b
//   response: none
//
//
// Messages
// --------
//
// PASSING:  '<' + ' ' + CHAN + ' ' + REFID + ' ' + PASSTIME + ' '
//             + POWER + ' ' + PASSCOUNT + ' '
//             + BATTERY + ' ' + CHARSUM + '>' + [NEWLINE]
//
// CHAN:   'MAN'|'BOX'|'STA'...
// REFID:    '000000'->'999999'  six digits, left zero pad
// PASSTIME: 'hh:mm'ss"dcm'  left zero pad
// POWER:    '00'->'99'  passing power
// PASSCOUNT:  '00'->'01'  count of times in loop (question?)
// BATTERY:  '0'|'1'|'2'|'3' 0/high -> 3/low
// CHARSUM:  '0000'->'8192'  sum of bytes from offset 1-32
//
// STATUS:   '[' + 'hh:mm'ss"' + ' ' + 'NS' + ' ' + 'NB'
//                 + ' ' + 'LS' + ' ' + 'LB' + ']' + [NEWLINE]
//             hh: hour eg 03
//             mm: minute eg 59
//             ss: second eg 31
//       Noise: NS (STA) and NB (BOX) '00' -> '99'
//       Levels: LS (STA) and LB (BOX) '00' -> '99'
//       Note: time reported is running time, and will
//       be 00:00'00" when decoder is stopped.
//
// DEPART:   'DEPART_' + [DATESTR] + '__' + [TODSTR] + [NEWLINE]
//
// STOP:   'STOP_' + [DATESTR] + '__' + [TODSTR] + [NEWLINE]
//
// DATESTR:  'YYYY-MM-DD'
//       YYYY: year eg 2012
//       MM: month eg 02
//       DD: day of month eg 12
//
// TODSTR:   'hh:mm:ss'
//       hh: hour eg 03
//       mm: minute eg 59
//       ss: second eg 31
//
// ESC:    0x1b
// NACK:   0x07
// CRC:    CRC-16/MCRF4XX on bytes following ESC (Note 1)
// B:    '1'|'2'|'3'...'7'  (0x30 + id)
// SETLEVEL: level as two ascii chars eg: 45 => '4' + '5' or 0x34 + 0x35
// SETTIME:  h + m + s
//       eg: 21h03:45  =>  0x15 0x03 0x2d
// SETDATE:  D + M + Y (Y == year - 2000)
//       eg: 23/05/12  =>  0x17 0x05 0x0c
// DECODERCONF:  '+' + '+' + '+' + [CONFIG] + [LEVELS] + [IPCONFIG]
//         + [IDENT] + [VERSION] + '>' + [NEWLINE]
//
// NEWLINE:  CR + LF
// CR:   0x0d
// LF:   0x0a
//
// LEVELS (2 bytes):
// 0 STA level 30 => 0x30
// 1 BOX level "
//
// IDENT (4 bytes):
// 0-3 '0129' => 0x00 + 0x01 + 0x02 + 0x09
//
// VERSION (4 bytes): (TBC)
// 0 0x13  ?
// 1-3 '201' version string?
//
// CONFIG (27 bytes):
// offset  option      values
// 0 Time of day       0x00=>runtime, 0x01=>timeofday
// 1 GPS Sync        0x00=>off, 0x01=>on
// 2 Time Zone Hour      0x10=>10h, 0x09=>9h
// 3 Time Zone Min     0x00=>:00, 0x30=>:30
// 4 Distant 232/485 select  0x00=>232, 0x01=>485  (check)
// 5 Distant Fibre Optic   0x00=>no, 0x01=>yes
// 6 Print pass on serial  0x00=>no, 0x01=>yes
// 7 Detect maximum      0x00=>no, 0x01=>yes
// 8 Protocol        0x00=>Cv3,0x01=>AMB,0x02=>Cv2
// 9 Generate sync     0x00=>no, 0x01=>yes
// 10  Sync interval min   0x01=>1min, ... , 0x99=>99min
// 11  Sync ToD on CELL    0x00=>off, 0x01=>on
// 12  Sync Time hours   0x00=>0h, ... , 0x23=>23h (Question Function?)
// 13  Sync Time min     0x00=>:00, ... , 0x59=>:59
// 14      Active Loop           0x00=>passive, 0x01=>powered (active)
// 15,16 STA Tone      0x12,0x34=>1234Hz 0x00,0x00=>no tone
// 17,18 BOX Tone    "
// 19,20 MAN Tone    "
// 21,22 CEL Tone    "
// 23,24 BXX Tone    "
// 25,26 STA+BOX Levels    eg 0x45,0x92 => 45,92 (note 2)
//
// IPCONFIG (16 bytes):
//
// 0-3   IP Address,     net order eg: 192.168.95.252 => 0xc0 + 0xa8 + 0x5f + 0xfc
// 4-7   Netmask,      "
// 8-11    Gateway,      "
// 12-15 Remote host,    "
//
// NOTES:
//
//   1.  CRC is computed with the following parameters:
//     model:    crc-16
//     poly:   0x1021
//     init:   0xffff
//     reflect-in: yes
//     reflect-out:  yes
//     xor-out:  0x0000
//
//   2.  Detection level appears to be stored or manipulated
//     as byte, but displayed as decimal equivalent of hex string.
//     When incrementing with command BXX Level, STA is wrapped to
//     zero when STA level is > 0x99. BOX level will increment
//     > 0x90 all the way to 0xff as long as STA is < 0xa0.
//     Side effects of this have not been tested.
//
*/
char  ESC       = 27;                 // escape character




/*
// Command Definition
//  Status
//  response: [STATUS]
//  Start'
//  response: [DEPART] or none if decoder already started
//   Update decoder configuration
//   command:  ESC + 0x08 + 0x08 + [CONFIG] + [CRC] + '>'
//   response: none
//   Update decoder IP configuration. Note: Decoder must be stopped
//   before issuing this command (why?)
//   command:  ESC + 0x09 + 0x09 + [IPCONFIG] + [CRC] + '>'
//   response: XPORT specific (TBC)
//   Fetch current decoder configuration & identification
//   command:  ESC + 0x10
//   response: [DECODERCONF]
//
//   Acknowledge last passing sent by decoder/flag ready for next passing
//   command:  ESC + 0x11
//   response: none or [PASSING]
//
//   Repeat first unacknowledged passing, else last acknowledged passing
//   command:  ESC + 0x12
//   response: [PASSING]
//
//   Stop decoder
//   command:  ESC + 0x13 + '\'
//   response: [STOP] (even if already stopped)
//
//   Update decoder time of day - also sets running time if decoder
//   started and config option "Running time to time of decoder" set
//   command:  ESC + 0x48 + [SETTIME] + 't'
//   response: none
//
//   Update decoder date
//   command:  ESC + 0x0a + 0x0a + [SETDATE] + [CRC] + '>'
//   response: none
//
//   Set detection level on STA channel
//   command:  ESC + 0x1e + [SETLEVEL]
//   response: none
//
//   Set Detection level on BOX channel
//   command:  ESC + 0x1f + [SETLEVEL]
//   response: none
//
//   Request status on remote decoder with id specified in B
//   command:  ESC + 0x49 + [B]
//   response: (TBC)
//
//   Increment all detection levels by 0x10 (Note 2)
//   command:  ESC + 0x4e + 0x2b
//   response: none
*/
unsigned long   oldMillis = 0;

void  sendLine()
{
  MsTimer2::stop();
  
  if( (millis() - oldMillis) > 1000 )
  {
    int s =  ( millis() - oldMillis )/1000;

    oldMillis = millis();

    theSeconds += s;
    if( theSeconds > 59 )
    {
      theMinutes += theSeconds / 60;
      theSeconds = theSeconds % 60;
      if( theMinutes > 59 )
      {
        theHours += theSeconds / 60;
        theMinutes = theMinutes % 60;
      }
    }
  }
  
  MsTimer2::set(turn+millis()&0x00000ff0, sendLine);
  if( ack )
  {
  unsigned long     m     = millis();
  unsigned int      tp    = m % (sizeof(transponderList)/ sizeof(unsigned long[3]) );
    createMsg(  tp , m ); 
    sline( (char *) &message[0] );
  }

  MsTimer2::start();
}

void parseTheCmd( char *cmd )
{
  if( cmd[0] != ESC )           // Check if it is realy a command
    return;
  switch( cmd[1] )
  {
    case 0x07:                  // Start decoder
      if( !started )
      {
        started = true;
         {          
          snprintf( (char * )&message[0], sizeof( message ),
            "DEPART_%4.4d-%2.2d-%2.2d__%2.2d:%2.2d:%2.2d\n",
            theYear,theMounth,theDay,theHours,theMinutes,theSeconds);
          sline( (char *) &message[0] );
         }
      }
      ack = true;
      break;
    case 0x13:                  // Stop decoder
      if( cmd[2] != 0x5C )
        return;
      started = false;
         {          
          snprintf( (char * )&message[0], sizeof( message ),
            "STOP_%4.4d-%2.2d-%2.2d__%2.2d:%2.2d:%2.2d\n",
            theYear,theMounth,theDay,theHours,theMinutes,theSeconds);
          sline( (char *) &message[0] );
         }
      break;
      
    case 0x12:                  // Repeat last passing
      ack = false;
      createMsg(  0 , 0 ); 
      sline( (char *) &message[0] );
      break;
      
    case 0x11:                  // Ack
      ack = true;
      break;
      
    case 0x05:                  // Status
      {
         if( started )
         {          
          snprintf( (char * )&message[0], sizeof( message ),
            "[%2.2d:%2.2d'%2.2d\" %2.2d %2.2d %2.2d %2.2d]\r\n",
            theHours,theMinutes,theSeconds,0,50,staLevel,boxLevel);
         }
         else
         {          
          snprintf( (char * )&message[0], sizeof( message ),
            "[%2.2d:%2.2d'%2.2d\" %2.2d %2.2d %2.2d %2.2d]\r\n",
            0,0,0,0,50,staLevel,boxLevel);
         }
         sline( (char *) &message[0] );
          
      }
      break;
      
    case 0x48:                  // SetTime
      if( cmd[5] != 't' )
        return;
      theHours    = cmd[2];
      theMinutes  = cmd[3];
      theSeconds  = cmd[4];
      break;
    
    case 0x0A:                  // SetDate
      if( cmd[2] != 0x0A )
        return;
      theDay     = cmd[3];
      theMounth   = cmd[4];
      theYear     = cmd[5] + 2000;
      break;
      
    case 0x1E:                  // SetStaLevel
      staLevel    = 0;
      staLevel    = ((cmd[2]-'0')%10)*10 + ((cmd[3]-'0')%10);
      break;
      
    case 0x1F:                  // SetBoxLevel
      boxLevel    = 0;
      boxLevel    = ((cmd[2]-'0')%10)*10 + ((cmd[3]-'0')%10);
      break;
  }
}

void setup()
{
  Serial.begin( 19200 );
  MsTimer2::set(1000, sendLine);
  oldMillis = millis();
  MsTimer2::start();
}

void loop()
{
char    Buffer[256];

  if( Serial.available() )
  {
  int   i = Serial.readBytesUntil('\r',&Buffer[0],sizeof(Buffer) );

    for(int j=0;j<i;j++)
    {
      if( Buffer[j] == ESC )
        parseTheCmd(&Buffer[j]);
    }
  }
}


