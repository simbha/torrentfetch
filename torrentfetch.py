#! /usr/bin/python
"""torrentfetch.py - Script for updating/downloading/staying connected to torrent
   author: hkpeprah

   The purpose of this script is to allow the user to download torrents and stay connected to torrents that
   are recurring (i.e. Television Series).  The legality of such is bared by the user and has nothing to do
   with this script.

   This is the main body of the program which basically acts as an information handler to listen for the user's
   input and act accordingly.
   
   Functions: fetchTorrent, fetchSeries, downloads"""

import os, sys, re, optparse
from torrentfeed import *

ver = "0.1.0"
contributers = [] #List of contributors


def fetchTorrent( ):
    """Fetches the torrent with the given string by using the torrent sources.
       The torrent is downloaded if it has a specific number of seeders/positive rating."""
    s = raw_input("Enter torrent name:\n> ")
    string = addTorrent(s)
    if not( string == None ):
        with open("download_torrents.txt", "a") as myfile:
            myfile.write(string + "\n")


def fetchSeries( ):
    """Adds the new series to the list, and fetches the individual torrents up-to-and
       including the one that the user specifies.  Torrent must have a specific number
       of seeders and a certain positive rating."""
    print "0. Schedule a torrent (fetches the torrent when it finds it has been added)\n1. Schedule a series (recurring torrent download)"


def downloads( ):
    """Lists the latest torrent downloads that the user has completed.  If no number is specified it
       defaults at 10."""
    print "Listing last 10 downloads:"
    try:
        with open("download_torrents.txt", "r") as myfile:
            index = 0
            for line in myfile:
                if index > 9: break;
                print line
                index += 1
    except:
        print "No downloads as of yet."



def main():
    """Function that accepts the main input that branches the script.  The user will select options based on what
       what they wish to do.  Depending on the input, the program will switch to the appropriate branch and receive
       and or provide input."""
    while True:
        print "Enter the corresponding number: \n0. Download new torrent.\n1. Schedule torrent or connect to series (RSS).\n2. List latest downloads.",
        print "\n3. View current downloads.\n4. View scheduled torrents and series.\n5. Exit"
        branch = int(raw_input("> "))
        if branch == 0:
            while True:
                fetchTorrent()
                if (not( raw_input("Download another torrent, 'y' or 'n'?\n> ") == "y")): break
        elif branch == 1: 
            while True:
                fetchSeries()
                if (not( raw_input("Schedule another torrent, 'y' or 'n'?\n> ") == "y")): break
        elif branch == 2: downloads()
        elif branch == 3: print "Current downloads"
        elif branch == 4: print "Scheduled torrents"
        else: break


if __name__ == "__main__":
    """Main execution of the script, simply provides information about the contributers, author and the current version.
       Provides some information about the program then executes the main function for branching.  Exits on end of the
       main program."""
    parser = optparse.OptionParser("usage: %prog [ options ]")
    parser.add_option("-t", "--torrent", dest="torrent", help="enter the torrent name to search for")
    parser.add_option("-s", "--series", dest="series", help="enter the series name to add and fetch episodes")
    parser.add_option("-v", "--version", dest="version", default=False, help="the program's version", action='store_true')
    parser.add_option("-d", "--downloads", dest="downloads", default=False, help="recent ten downloads", action='store_true')
    parser.add_option("-l", "--list", dest="list_series", default=False, help="list all the series that are added", action='store_true')
    (options, args) = parser.parse_args()
    if ( len(sys.argv) == 1 ):
        print "Torrent Feeder Script\nVersion: " + ver + "\nauthor: hkpeprah\nContributors: "
        for person in range(0, len(contributers)): print contributors[person] + " "
        print "This script acts as a tool for enabling the user to download torrents\nand stay connected to recurring torrents.\n"
        main()
    elif ( sys.argv > 1) :
        #Parse the command-line arguments
        if ( options.version == True ): print "Version: " + str(ver)
        elif ( options.downloads == True  ): downloads()
        elif ( not( options.torrent == None ) and options.series == None ): fetchTorrent( str(torrent) )
        elif ( not( options.series == None ) ): fetchSeries( str(series) )
        else: print parser.usage
    exit
   
