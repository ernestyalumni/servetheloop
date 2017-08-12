// @file :: traverse_podCommands.js
// @author :: Ernest Yeung, rLoop
// @example :: To use this, do this in the command prompt: node traverse_podCommands.js  
// Note that you HAVE TO run this in the directory containing podCommands.js and binary.js because podCommands.js 
// refers relative to itself to binary.js (in its file directory tree)

//const podCmds_obj = require('./server/udp/podCommands.js'); // doesn't work because we need ./binary which is referenced from the original podCommands.js
var podCmds = require('./podCommands.js')

// podCommands.js require './binary' so make sure to include that 
const binary  = require('./binary.js') 

// convert all the podCommands to an array
const podCmds_lst = podCmds()

//
// File I/O with json of the list of RETURNED pod commands
//

// @ref https://stackoverflow.com/questions/34156282/how-do-i-save-json-to-local-text-file
// Convert it from an object to string with stringify
var json_out = JSON.stringify( Object.getOwnPropertyNames(podCmds_lst) );

// use fs to write file to disk
var fs = require('fs');
//fs.writeFile("packetDefinitions.json", json_out, 'utf8', function(err) {
fs.writeFile("podCmds_lst.json", json_out, function(err) {	
	if(err) {
		return console.log(err);
	}
});
