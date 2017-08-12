// @file traverse_packetDef.js
// @author Ernest Yeung, rLoop
// @example To use this, do this in the command prompt: node traverse_packetDef.js  
var packetDefs_obj = require('./config/packetDefinitions.js');

//var L = packetDefs_obj.length; // undefined
//var packetDef_obj = packetDefs_obj[0]; // error

// successful line, reproduces what is desired from packetDefinitions.js; I print it out with console.log
//console.log(packetDefs_obj);

console.log( Object.keys( packetDefs_obj) );  // 'packetDefinitions'  

// (since we're now in node.js version of a list, indexed counting from 0, it'll just give numbers
// observe there are 32 packet definitions (1+31)
// console.log( Object.keys( packetDefs_obj.packetDefinitions ) ); 

var number_packetDefinitions = packetDefs_obj.packetDefinitions.length;
for (var idx = 0; idx < number_packetDefinitions; idx++) 
{
	// prints out the keys available
	console.log( packetDefs_obj.packetDefinitions[idx].Name );
}
console.log(" \n ");


//
// File I/O with json of these packet definitions
//

// @ref https://stackoverflow.com/questions/34156282/how-do-i-save-json-to-local-text-file
// Convert it from an object to string with stringify
var json_out = JSON.stringify( packetDefs_obj.packetDefinitions );

// use fs to write file to disk
var fs = require('fs');
//fs.writeFile("packetDefinitions.json", json_out, 'utf8', function(err) {
fs.writeFile("packetDefinitions.json", json_out, function(err) {	
	if(err) {
		return console.log(err);
	}
});
