#!/usr/bin/env python
# -*- coding: UTF-8 -*

import sys
from lib.parse import results
from lib.db import Db

def main():
	sites = results(sys.argv[1])
	for site in sites:
		print site
	Db(sys.argv[1])
	db = Db()
	db.add(sites, sys.argv[1])

def db_data():
	db = Db()
	data = db.read_data(sys.argv[2])
	for returned in data:
	    print returned

def db_tables():
	db = Db()
	tables = db.read_tables()
	for table in tables:
		print table


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'Eg: ./similar.py google.com'
		print 'Or: ./similar.py read <site> to read from db'
		sys.exit(1)
	elif len(sys.argv) == 3 and 'read' in sys.argv[1]:
		db_data()
	elif len(sys.argv) == 2 and sys.argv[1] == 'read':
		db_tables()
	else:
		main()

