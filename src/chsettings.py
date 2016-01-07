#!/usr/bin/python

import cgi, cgitb, ConfigParser

# Add Connection Function
def addconn( connection ):

	parser.add_section( connection )
	parser.set( connection, 'username', username )
	parser.set( connection, 'password', password )
	parser.set( connection, 'hostname', hostname )
	parser.set( connection, 'sid', sid )

	with open( "connections.ini", 'w' ) as config:
		parser.write( config )

# Edit Connection Function
def editconn( connection ):

        parser.set( connection, 'username', username )
        parser.set( connection, 'password', password )
        parser.set( connection, 'hostname', hostname )
        parser.set( connection, 'sid', sid )

        with open( "connections.ini", 'w' ) as config:
                parser.write( config )

# Remove Connection Function 
def rmconn( connection ):
	parser.remove_section( connection )

	with open( "connections.ini", 'w' ) as config:
		parser.write( config )

# Global Vars
form = cgi.FieldStorage()
parser = ConfigParser.SafeConfigParser()
parser.read( "connections.ini" )
sections = parser.sections()
submit = form.getvalue( 'submit' )
newconnection = form.getvalue( 'connection' )
sellectconnection = form.getvalue( 'connvar' )
username = form.getvalue( 'username' )
password = form.getvalue( 'password' )
hostname = form.getvalue( 'hostname' )
sid = form.getvalue( 'sid' )

print	"Content-type:text/html\r\n\r\n"
print	'<html>'
print	'<head>'
print	'<title>Oracle DaTabase Backup Report System</title>'
print	'</head>'

print	'<body>'

# Main Function
if submit == 'Add':
	if ( newconnection is None or
		username is None or
		password is None or
		hostname is None or
		sid is None     ):
			print	'<b><font style="color: red; background-color: black">Not all the fields have been filled out'

			print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
			print   '<form action="settings.py" method="get">'
			print   '<table>'
			print   '<tr>'
			print   '<td><input type="submit" value="Back"></td>'
			print   '</tr>'
			print   '</table>'
			print   '</form>'
			print	'</div>'
	
	elif not sections:
		addconn( newconnection )
		print	'<b><font style="color: lime; background-color: black">%s connection has been added' % newconnection

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'


	elif newconnection in sections:
		print	'<b><font style="color: red; background-color: black">%s connection name already exists<br>' % newconnection

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'

	else:
		addconn( newconnection )
		print	'<b><font style="color: lime; background-color: black">%s connection has been added' % newconnection

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'


elif submit == 'Edit':
	if (	username is None or
		password is None or
		hostname is None or
		sid is None	):
			print   '<b><font style="color: red; background-color: black">Not all the fields have been filled out'
		
			print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                        print   '<form action="settings.py" method="get">'
                        print   '<table>'
                        print   '<tr>'
                        print   '<td><input type="submit" value="Back"></td>'
                        print   '</tr>'
                        print   '</table>'
                        print   '</form>'
                        print   '</div>'


	elif sellectconnection in sections:
		editconn( sellectconnection )
		print	'<b><font style="color: lime; background-color: black">%s connection has been eddited' % sellectconnection

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'

elif submit == 'Remove':
	if sellectconnection in sections:
		rmconn( sellectconnection )	
		
		print   '<b><font style="color: lime; background-color: black">%s connection has been removed' % sellectconnection
		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
        	print   '<form action="settings.py" method="get">'
        	print   '<table>'
        	print   '<tr>'
        	print   '<td><input type="submit" value="Back"></td>'
        	print   '</tr>'
        	print   '</table>'
        	print   '</form>'
        	print   '</div>'

print   '</body>'
print   '</html>'
