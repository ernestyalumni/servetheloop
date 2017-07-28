# servetheloop
Code related to the Hyperloop, 

## Table of Contents

| codename | directory/location | brief description, key words |  
| :------  | :----------------- | ---------------------------: | 
| `./reactGS/` | `./`      | This folder mirrors parts of the [`react-groundstation` github repository](https://github.com/rLoopTeam/react-groundstation), only parts needed to be separately tested; it'll "mirror" or copy the directory structure of that github repo as much as possible |
| `traverse_packetDefs.js`  | `./reactGS/`  | Javascript/node.js script that prints out the various key, value pairs of the packet definitions found in [`react-groundstation/config/packetDefinitions.js`](https://github.com/rLoopTeam/react-groundstation/blob/master/config/packetDefinitions.js), and does *file I/O*, i.e. saves to a `.json` file the packet definitions.  There is no manual copying and pasting as the packet definitions are `module.exports`'ed as a JavaScript object to this script and then saved exactly to a JSON file.  Then go to the Python Jupyter notebook to see examples of using it, [`packetDefinitions.ipynb`]() |  
|`traverse_packetDefs_draft.js`  | `./reactGS/`  | Draft of `traverse_packetDefs.js` - contains a lot of commands commented out, but might be useful pedagogically as I was learning node.js |  
| `packetDefinitions.json` | `./reactGS/` | This is created by running `node traverse_packetDefs_draft.js` in the command prompt; it's a JSON file of the packet definitions used in `react-groundstation`, directly from `packetDefinitions.js` in that repo; then manipulate this data however you want (Excel file, Python dict, etc.) |
| `packetDefinitions.ipynb` | `./reactGS/` | Go here.  It steps you through saving the packetdefinitions directly into JSON format and then reading it into a Python list for easy manipulation |  

## [`eng-software-pod`](https://github.com/rLoopTeam/eng-software-pod/tree/development/FIRMWARE)

I'll try to explain the structure and what everything is in [`eng-software-pod`](https://github.com/rLoopTeam/eng-software-pod/tree/development/FIRMWARE).  There are the doxygen documentation that are both comprehensive and look really nice.  But these explanations are for somone like me who isn't sophisticated with programming and software.

Note which *branch* you are looking at, "checking out" (i.e. `git checkout <branch>`).  We are mainly on the `development` branch most of the time, rather than `master`.  

### [`eng-software-pod/FIRMWARE`](https://github.com/rLoopTeam/eng-software-pod/tree/development/FIRMWARE)

I'm not sure what `LFW*` stands for.

#### [`eng-software-pod/FIRMWARE/PROJECT_CODE`](https://github.com/rLoopTeam/eng-software-pod/tree/development/FIRMWARE/PROJECT_CODE)







