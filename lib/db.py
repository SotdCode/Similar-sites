#!/usr/bin/env python
# -*- coding: UTF-8 -*

import sqlite3
import os

class Db(object):
    """Interact with the sqlite database"""
    def __init__(self, url=None):
        self.dbfile = os.getcwd() + "/lib/database/similar.db"
        self.conn = sqlite3.connect(self.dbfile)
        self.conn.text_factory = str
        self.curs = self.conn.cursor()
        if url:
            self.url = url.replace('.', '')
            self.curs.execute("""CREATE TABLE IF NOT EXISTS """ + self.url + """ (similar VARCHAR(50)) """)
        self.conn.commit()

    def add(self, sites, site):
        """Add similar sites to the relevant table"""
        name = site.replace('.', '')
        for site in sites:
            try:
                self.curs.execute("""INSERT OR REPLACE INTO """ + name + """ (similar) VALUES(?)""", [str(site)])
            except:
                print 'Error writing'
            else:
                self.conn.commit()
    
    def read_data(self, site):
        """Read stored data in relevant table"""
        target = site.replace('.', '')
        try:
            self.curs.execute("SELECT * FROM " + target)
            result = [element[0] for element in self.curs.fetchall()]
        except:
            print "Error reading data"
        else:
            return result

    def read_tables(self):
        """Read tables from database"""
        try:
            self.curs.execute("SELECT * FROM sqlite_master")
            result = [element[1] for element in self.curs.fetchall()]
        except:
            print "Error reading tables"
        else:
            return result

