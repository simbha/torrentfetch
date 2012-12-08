#! /usr/env python
"""torrentfeed.py - Script for getting a torrent, and the torrent and series classes.
   author: hkpeprah
   
   The purpose of this script is to get the feeds for a torrent and/or series, and
   either download them or notify the user."""


import re, json, urllib, sys, subprocess
from anonbrowser import *


#Sites for torrents
sites = ["http://thepiratebay.se/tag/"]


def downloadTorrent( torrentlink ):
    """Takes a string corresponding to the page for a torrent and downloads the matching torrent on that
       page and returns the magnet link."""
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(torrentlink)
    html = page.read()
    linknames = re.compile('href="/torrent/(.*?)"').findall( html )
    magnetlinks =  re.compile('href="magnet(.*?)"').findall( html )
    print "\nSelect a torrent:"
    for i in range(0, 3):
        print str(i) + ". Torrent Name: " + linknames[i]
    i = raw_input("> ")
    return (linknames[int(i)], magnetlinks[int(i)])


def addTorrent( torrentname ):
    """Adds a torrent, creates the torrent from the class, determines if it should be downloaded,
       then begins to download if applicable.  Fetches the torrent from the web."""
    tpb_query = re.sub("[ +]", "+", torrentname) + "/0/7/0"
    sites[0] = sites[0] + tpb_query
    torrent = downloadTorrent(str(sites[0]))
    print 'Downloading...%s' %torrent[0]
    command = 'xdg-open magnet%s' %torrent[1]
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return torrent[0]
