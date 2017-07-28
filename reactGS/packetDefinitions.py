"""
@file packetDefinitions.py
@author ernestyalumni, rLoop
@brief Once you have the packet definitions in json file format, 
		you can turn it into a Python dictionary, preserving the 
		original tree structure  
"""  
import json 

def read_json_file_return_list(filename="./packetDefinitions.json"):
	"""
	@fn read_json_file_return_list=read_json_file_return_list(filename)
	@brief This reads the packet definitions in json and returns a 
			list that preserves the original tree structure from the node.js 
				script packetDefinitions.js.  
			From here, with that list, you can do all the queries you want 
				with the usual, common Python methods, .keys(), .[]
			
	@param filename : string with file location, with its name 
	
	@note To be implemented; check that makes sure the file is there.  
	"""  
	
	f_packetDef_json = open(filename,'rb')
	rawjson_packetDef=f_packetDef_json.read()
	f_packetDef_json.close()
	packetdef_lst = json.loads(rawjson_packetDef)
	return packetdef_lst
		
