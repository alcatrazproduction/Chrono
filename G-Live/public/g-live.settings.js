//.clax URL, if not provided as page argument (g-live.html, arg='f')
//for local live: urlclax is folder relative starting from claxfolder; both using slashes and not backslashes; both excl. special chars and respecting character casing
//e.g. claxfolder="C:/events" + urlclax="My race/My race.clax" => full clax path = "C:\events\My race\My race.clax"
var urlclax="Test X2 staffetta_replay.clax";
var claxfolder="D:/Epreuves/Live";
//live node server url
var liveNodeServer="http://192.168.1.101:8070";
var urlSocketIO="socket.io/socket.io.js";

var liveLocal=1; //local (1) or web (0)
var pgTitle="G-Live"; //page title to display
var favicon="img/fav.png"; //page icon(.png,relative path,optional)
var pgHeader="",pghHeight=60; //url and height for page header, optional
var deflang="4";
var RankOnRealTime=0; //ranking made on real times by default if available
