Requirements:
python
libnotify which requires gtk
permission to make something executable

Install instructions:
Download the script and unpack it to wherever you please, then give it execute permission

example:
chmod +x MSPA_notifier.py

After this is done if you wish to start it on startup add it to your startup script. 

For ubuntu users this is located in either
System > Preferences > Sessions
or
System > Preferences > Startup Applications

other distros should know where they keep the startup manager and/or how to write your own

You can add other update macros to the Macros folder, they don’t HAVE to be pngs, any image format that libnotify supports should be fine.

To get new messages simply add them to the updateLines.txt folder

usage: MSPA_notifier.py [-h] [-u UPDATE] [-d] [-l] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -u UPDATE, --update UPDATE
                        The time between update checks in seconds default: 300
                        (5 min) can't go below 60 seconds
  -d, --demo            This just pops an update to test the libnotify system
                        is working correctly
  -l, --link            This is to be used to create a quick click icon for
                        going to a saved page see readme
  -t, --timeout         Flag to tell the libnotify bubble to timeout, defaults
                        to never timing out so you don't miss an UPDATE in
                        your sleep

Usage of the -l

As we all may know some systems (such as Ubuntu) are transitioning away from applets. This is unfortunate because my first instinct was to just make an applet. There isn't a cross distro way to do this yet so -l is the solution. -l will simply instruct the script to open your saved MSPA game in a new tab in your default browser and then close. 

For instance I use xubuntu so I made a launcher applet and told it to launch the script with the -l option on. Until I figure out this dbus magic this is the best way to do it. You don't NEED a quick launch, you could just go to the site when you see an update but I like it. The icon in the Icons directory is included for use with the applet launcher 