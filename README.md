Torrent Fetch
================================================================================================

Fetch and download torrents from the internet.  Currently a work in-progress.
Runs in the command-line to get torrents from the internet.


####Details
* Uses ThePirateBay as a torrent search engine.
* Search and download select torrents.
* Search, download, and stay up-to-date with torrent series.
* Note, you may need to run as root ( 'sudo' or 'su' ) to install the dependant python libraries.


####Requirements
* An internet connection.
* transmission, transmission-daemon, transmission-remote
  * sudo apt-get install transmission
  * sudo apt-get install transmission-daemon
  * sudo apt-get install transmission-remote
* mechanize
  * easy_install mechanize 
* RssLibraries (feedparser)
  * easy_install feedparser