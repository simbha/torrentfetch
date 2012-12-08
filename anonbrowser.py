#! /usr/env python
"""anonbrowser.py - Methods for viewing HTML pages, sources and parsing information anonymously.
   author:hkpeprah
   
   Description
      Anonymously connect to a server and use methods for gaining source code, parsing
   information, returning appropriate code, etc.
"""
#Modules and methods to be imported
import mechanize, random, cookielib


class anonBrowser(mechanize.Browser):
    #Class for anonymously browsing and searching the web
    def __init__(self, proxies=[], user_agents=[]):
        """Initializes the class"""
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = user_agents + ['Mozilla/4.0 ', 'Firefox/6.01', 'ExactSearch', 'Nokia7110/1.0']
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()
    def clear_cookies(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents))
        self.addheaders = [('User-agent', (self.user_agents[index]))]
    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http': self.proxies[index]})
    def anonymize(self, sleep = False):
        self.clear_cookies()
        self.change_user_agent()
        self.change_proxy()
        if sleep: time.sleep(60)






