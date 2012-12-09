#! /usr/env python
"""torrentfeed.py - Script for getting a torrent, and the torrent and series classes.
   author: hkpeprah
   
   The purpose of this script is to get the feeds for a torrent and/or series, and
   either download them or notify the user."""


import re, json, urllib, sys, subprocess, feedparser
from anonbrowser import *


def scheduleTorrent():
    """Schedules a torrent.  Reads a particular feed and waits for the torrent to become available.
       Two sources are used for respective feeds (Movies, TVShows)"""
    


def downloadTorrent( torrentlink ):
    """Takes a string corresponding to the page for a torrent and downloads the matching torrent on that
       page and returns the magnet link."""
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(torrentlink)
    html = page.read()
    linknames = re.compile('href="/torrent/(.*?)"').findall( html )
    magnetlinks =  re.compile('href="magnet(.*?)"').findall( html )
    print "Select a torrent, enter 'n' to see next 3, 'e' to exit:"
    torrentindex = 0
    while len(linknames) > 0:
        bound = 3 if (len(linknames) > 2) else len(linknames)
        for i in range(0, bound):
            i += torrentindex
            print str(i) + ". Torrent Name: " + linknames[i]
        torrentindex += bound
        i = raw_input("> ")
        if ( str(i) == "e" ): break
        elif ( not( str(i) == "n" )):
            ab.close()
            return (linknames[int(i)], magnetlinks[int(i)])
    ab.close()
    return -1


def addTorrent( torrentname ):
    """Adds a torrent, creates the torrent from the class, determines if it should be downloaded,
       then begins to download if applicable.  Fetches the torrent from the web."""
    tpb_query = re.sub("[ +]", "+", torrentname) + "/0/7/0"
    sites = ["http://thepiratebay.se/tag/"]
    sites[0] = sites[0] + tpb_query
    torrent = downloadTorrent(str(sites[0]))
    if torrent == -1:
        print "Could not find torrent."
        return ""
    else:
        print 'Downloading...%s' %torrent[0]
        command = 'xdg-open magnet%s' %torrent[1]
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return torrent[0]
