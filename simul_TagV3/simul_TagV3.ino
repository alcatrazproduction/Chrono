/*
 * Cano Decoder simulator, this will simulate track with rider. 
 */

#include <MsTimer2.h>
#include <string.h>


#define  sline(a) Serial.println( a)
#define  turn (1000*30)
unsigned char digits[]                = "0123456789ABCDEF";
volatile unsigned char message[]      = "CDFD4C0000F1D5\0\0ERROR"; // CDFD4C 0000F1D5
unsigned long  transponder[] =
{
    2351957,
    2688158,
    3073479,
    4572215,
    4748687,
    4961721,
    5564690,
    6000513,
    6091953,
    6099608,
    7531106,
    1010101,
    2020202,
    3030303,
    4040404,
    5050505,
    6060606,
    7070707,
    8080808,
    9090909,
};

void  createMsg( unsigned long tp, unsigned long time )
{
 int i;
 
   for( i = 0 ; i<6 ; i++ )
   {
   int  d;
     
     d= digits[(((0x00f00000)&tp)>>20) & 0x0f];
     message[i]= d;
     tp = tp << 4;
   }
   time = time*4;
   for( i = 0; i<8 ; i++ )
   {
    int d;
    
     d= digits[(((0xf0000000)&time)>>28 ) & 0x0f];
     message[i+6]= d;
     time = time << 4;
   }
}

void  sendLine()
{

  MsTimer2::stop();
  MsTimer2::set(turn+millis()&0x00000ff0, sendLine);
  createMsg( transponder[ millis()%((sizeof(transponder)/sizeof(unsigned long))) ], millis() ); 
  sline( (char *) &message[0] );
  MsTimer2::start();
}

void setup()
{
  Serial.begin( 115200 );
  Serial.println( "Cano Simulator (c) Yves Huguenin $VER: 0.1 ");
  MsTimer2::set(turn, sendLine);
  MsTimer2::start();
}

void loop()
{
char    Buffer[256];

  if( Serial.available() )
  {
  int   i = Serial.readBytesUntil('\r',&Buffer[0],sizeof(Buffer) );

    if( !strcasecmp("version",&Buffer[0] ) )
    {
      Serial.println( "Cano Simulator (c) Yves Huguenin $VER: 0.1 ");
    }
    else
    if( !strcasecmp("cano mode",&Buffer[0] ) )
    {
      Serial.println( "CANO MODE");
    }
  }
}


