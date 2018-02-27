//websocket gateway on 8070
var port_serveur = 8070, port_udp_live = 41181, port_udp_feedback = 11579;
//var compression = require('compression');
var express = require('express');
var http = require('http');
var url = require('url');
var path = require('path');
var fs = require('fs');
var app = express();
//app.use(compression());
var server = http.createServer(app);
var io = require('socket.io').listen(server);

//obsolete: io.set('transports', ['xhr-polling', 'websocket', 'flashsocket', 'htmlfile', 'jsonp-polling']); // enable all transports (optional if you want flashsocket)

server.listen(port_serveur);

//-------------------------------------------------------------------------------------------------
// intitulé du processus pour identification précise - ne pas modifier !
process.title = 'G-Live on ' + port_serveur;

// inclusion fichier settings du g-live
var vm = require('vm');
var includeInThisContext = function(path) {
		var code = fs.readFileSync(path);
		vm.runInThisContext(code, path);
}.bind(this);
includeInThisContext(__dirname+"/public/g-live.settings.js");

var pagedefaut = function(req,res,next){
/*
console.log('req.url='+req.url);
	if(req.url.length>2 && req.url.substr(0,2)=="//") {
console.log('req.url='+req.url);
	req.url = '/g-live.html?cfg='+req.url.substr(2,req.url.length-2);
	req.path = '/';
console.log('req.url='+req.url);
	}
*/
	if(req.path=='/') { // appel racine -> équivalent page index par défaut
	req.url = '/g-live.html';
	}
	next();
}

var routeclax = function(req,res,next){
	// service fichiers depuis le dossier de l'épreuve, selon leur emplacement sur le disque - renseigné dans settings.js
	if (liveLocal) {
		var extension = path.extname(req.path).toLowerCase();
		if (extension == '.clax' || extension == '.mdp' || extension == '.gpx' || req.path=='/result-plugins.js') {
			if (claxfolder!=undefined && claxfolder!='') {
				// fichier clax local, hors du domaine direct de l'application
				var f = path.join(claxfolder,decodeURI(req.path));
				if (extension == '.clax') 
					console.log('full url clax='+f);
				else if (f.endsWith('\\Live\\'+decodeURIComponent(path.basename(req.path))))
					// le fichier clax peut être servi depuis le sous-dossier /Live (clone du fichier originel), mais pas les autres
					f = f.replace('\\Live\\'+decodeURIComponent(path.basename(req.path)),'\\'+decodeURIComponent(path.basename(req.path)));
				res.download(f);
				return(0);
			}
		}
	}
	next(); // Passing the request to the next handler in the stack.
}

var routeUrlKiosque = function(req,res,next){ //url-rewriting pour accès en /kiosk au mode kiosque
	if(/^\/kiosk/.test(req.path)){
		req.url = '/g-live.html?kiosk=1';
	}
	next();
}
	
var screenconfigs = function(req,res,next){ //url-rewriting pour accès en /Screen ou /screen à une config d'écran (routage vers page screen.html)
	if(/^\/Screen\/*/.test(req.path)  ||  /^\/screen\/*/.test(req.path)) {
		req.url = '/screen.html';
	}
	next();
}
var routeFichierScreenConfig = function(req,res,next){
	// service fichiers screenconfig.json depuis dossier AppData/Wiclax
	if (liveLocal && req.path.toLowerCase().endsWith('.screenconfig.json')) {
	var dossierAppData = path.join(process.env.APPDATA,'Wiclax');
	var f = path.join(dossierAppData,decodeURIComponent(req.path));
	res.download(f);
	return(0);
	}
	next(); // Passing the request to the next handler in the stack.
}

//-------------------------------------------------------------------------------------------------

app.use(pagedefaut);
app.use(routeclax);
app.use(routeFichierScreenConfig);
app.use(screenconfigs);
app.use(routeUrlKiosque); // après screenconfig
app.use(express.static(__dirname + '/public'));


var mysocket = 0;

io.sockets.on('connection', function (socket) {
	var nb=io.engine.clientsCount;
	console.log(nb + ' ' + (nb==1?'client connecte':'clients connectes'));
	console.log('dir: '+__dirname);
	mysocket = socket;
	mysocket.on('screenconfig', function(config){ 
		console.log('screenconfig='+config);
		try {
		var message = new Buffer('screenconfig '+config);
		server.send(message,0,message.length,port_udp_feedback,serverInfo.address);
		} catch(e){console.log('46:'+e.message)}
	});
});

//udp server pour le live
var dgram = require("dgram");
var server = dgram.createSocket("udp4");
var serverInfo;
server.on("message", function (msg, rinfo) {
	console.log("msg: " + msg);
	//console.log("rinfo.port=" + rinfo.port + " rinfo.address=" + rinfo.address);
	serverInfo=rinfo;
	if (msg.length>0 && msg[0]=='76'){ //76 pour 'L'
		try {
		var message = new Buffer('echo ' + port_udp_live);
		server.send(message,0,message.length,port_udp_feedback,rinfo.address);
		} catch(e){}
	}
	if (""+msg=="nbc?"){
		var message = new Buffer('nbc=' + io.engine.clientsCount);
		server.send(message,0,message.length,port_udp_feedback,rinfo.address);
	}
	if (mysocket != 0){
		mysocket.emit('field', "" + msg);
		mysocket.broadcast.emit('field', "" + msg);
	}
});
server.on("listening", function () {
	var address = server.address();
	console.log("udp server listening " + address.address + ":" + address.port);
});
server.bind(port_udp_live);