#!/usr/bin/python
import os
import subprocess
import random
import urllib2
import xml.etree.ElementTree as ET
import time
import webbrowser
import sys
import argparse

def getRSSUpdate():
    mspaFeed = "http://www.mspaintadventures.com/rss/rss.xml"

    url_info = urllib2.urlopen(mspaFeed)

    tree = ET.parse(url_info)
    rss = tree.getroot()
    channel = rss.getchildren()[0]
    newestItem = channel.find("item")
    #having found the newset item return the pudate of it to be compared
    newestItem = newestItem.find("pubDate")
    return ET.tostring(newestItem)

def pictureSelect():
    fileName = random.choice(os.listdir(os.getcwd()+"/Macros/"))
    widgetIcon = os.getcwd()+"/Macros/"+fileName
    return widgetIcon

def messageSelect():
    try:
        messageFile = open("updateLines.txt",'r')
        messageArray = messageFile.readlines()
        return random.choice(messageArray)
    except:
        return "MSPA Update"

def popUpdate(timeout):
    message = messageSelect()
    widgetIcon = pictureSelect()
    if timeout:
        subprocess.call(["notify-send","MSPA Update!",message,"-i",widgetIcon,
        "-t","-1"])
    else:
        subprocess.call(["notify-send","MSPA Update!",message,"-i",widgetIcon])
    return

def firstRun():
    popUpdate(False)
    current = getRSSUpdate()
    #create file
    saveFile = open("updateWatch.xml",'w+') 
    #write check to it
    saveFile.write(current)
    saveFile.close()
    return

def checkForUpdate(notifyTimeout):
    current = getRSSUpdate()
    try:
        saveFile = open("updateWatch.xml",'r+')
        saved = saveFile.readline()

        if current != saved:
            popUpdate(notifyTimeout)
            saveFile.close()
            saveFile = open("updateWatch.xml",'w+')
            saveFile.write(current)
            saveFile.close()
    
    except IOError as err:
        firstRun()
    return

def notificationLoop(timeBetweenChecks,notifyTimeout):
    while True:
        checkForUpdate(notifyTimeout)   
        time.sleep(timeBetweenChecks)
    return

def openSite():
    #game loading URL
    url = "http://www.mspaintadventures.com/?game=load"
    #opens default web browser with that url in a new tab if possible
    webbrowser.open_new_tab(url)
    return
#sets up the argument parser with correct flags, functionalized to keep shit out of the main
def setupParser():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-u','--update', type=int,help="The time between update checks in seconds default: 300 (5 min) can't go below 60 seconds")
    parser.add_argument('-d','--demo',action="store_true",help="This just pops an update to test the libnotify system is working correctly")
    parser.add_argument('-l','--link',action="store_true",help="This is to be used to create a quick click icon for going to a saved page see readme")
    parser.add_argument('-t','--timeout',action="store_true",help="Flag to tell the libnotify bubble to timeout, defaults to never timing out so you don't miss an UPDATE in your sleep")
    return parser

def main():
    #Notify.init("UPDATE")
    parser = setupParser()
    namespace = parser.parse_args(sys.argv[1:])
    argsDict = vars(namespace)
    #link takes precident over test which takes precident over update
    #only if others are blank will the monitor loop start
    timeoutAmount = argsDict['timeout']
    if argsDict['link'] == True:
        openSite()
    else:   
        if argsDict['demo'] == True:
            popUpdate(timeoutAmount)
        else:
            if argsDict['update'] == None:
                updateTimerAmount = 300
            else:
                updateTimerAmount = argsDict['update']
                
                if updateTimerAmount < 60:
                    sys.exit("No Flooding, 60 seconds or more on the clock")

            notificationLoop(updateTimerAmount,timeoutAmount)
    
    
    return

main()
