// @file :: traverse_podCmds_example.js
// @brief :: "Pedagogical" version of learning about podCommands.js, i.e. I explicitly step through, in the node Interactive session, 
// how to navigate through podCommands.js
// @author :: Ernest Yeung, rLoop
// @example :: To use this, do this in the command prompt: node traverse_podCommands.js  
// Note that you HAVE TO run this in the directory containing podCommands.js and binary.js because podCommands.js 
// refers relative to itself to binary.js (in its file directory tree)
// we'll also have to comment out the line that requires 'chalk'

//var podCmds_= require('./server/udp/podCommands.js'); // doesn't work because we need ./binary which is referenced from the original podCommands.js
var podCmds = require('./podCommands.js')

typeof podCmds  // [Function]

console.log(typeof podCmds)  // [Function]

// podCommands.js require './binary' so make sure to include that 
const binary_obj  = require('./binary.js') 

// podCommands.js exports 1 (single) big function; call it function (udp) (it wasn't named; you don't need to name your functions in node.js) 
console.log(podCmds_obj)  // [Function]

// function (udp) takes variable udp; udp is the entire folder with all its scripts in /server/udp/ (!!!)
// this is evident by how udp is using a "function method" .tx which is in /server/udp/tx.js

// "instantiate" the output of this function (udp)
console.log(podCmds())

typeof podCmds() // 'object'

console.log(typeof podCmds() )

// pod Commands list
const podCmds_lst = podCmds()

// cf. Object.getOwnPropertyNames() - returns an array of all properties found directly upon a given object
console.log( Object.getOwnPropertyNames(podCmds_lst) )

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

