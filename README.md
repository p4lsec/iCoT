# iCoT

iCoT is a Pythonista script for iOS designed to generate and forward CoT messages to [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer). 

## Requirements

1. iPhone or iPad
2. [Pythonista](http://omz-software.com/pythonista/)
3. [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer)

## Install from an iPhone:

Method 1: 
  
1. Install and configure StaSh: https://github.com/ywangd/stash
2. From the StaSh shell, run `git clone https://github.com/p4lsec/iCoT.git`
3. Locate and open the iCoT folder from the left hand menu

Method 2:

1.  Click here to download this script: https://github.com/p4lsec/iCoT/archive/main.zip
2.  Unzip the file by clicking on it in the 'Files' app
3.  Open Pythonista, Click External Files > Open > Folder
4.  Select the iCoT folder

If this doesn't work, just copy and paste the code over into a new folder in Pythonista.  Be sure you have iCoT.py and iCoT.conf in the same folder. 

## Configure

Open iCoT.conf, and modify the fields as appropriate.  Be sure takip and takport and the IP address and port for your FreeTAKServer. 

## Usage

When you're ready to start sending CoT messages, click the play button in the upper right hand corner.  

## Roadmap

1. Improve install/configuration documentation
2. Improve error handling
3. Test for background process timeouts
4. Build a Shortcut integration to start and stop iCot
5. Add argparse support for future feature additions
6. ???
7. Profit

## Support

Follow me on [Twitter](https://twitter.com/p4lsec) and [LinkedIn](https://www.linkedin.com/in/p4lsec/)
