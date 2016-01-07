#!/usr/bin/python

import cx_Oracle, cgi, cgitb, ConfigParser, sys

# Oracle DB Class
class DBconnection:
	
	def __init__( self, username, password, hostname, sid ):
	
		self.username = username
		self.password = password
		self.hostname = hostname
		self.sid = sid
			
		self.connection = cx_Oracle.connect( '%s/%s@%s/%s' % ( self.username, self.password, self.hostname, self.sid ) )
	
	def dbrequest ( self, sql ):
		
		cursor = self.connection.cursor()
		cursor.execute( sql )
		
		return cursor.fetchall()
		
	def __del__( self ):
		
		self.connection.close()

# Backup Type Function 
def bcktype( sql, report, dbconnections ):

	dbrequests = []
	
	for connection in dbconnections:
		dbrequests.append( [ connection, bckrequest( connection, sql ) ] )
	
	if sql == currentdaySQL:
		bckvalidation ( dbrequests )
		
	bckreport( dbrequests, report, sql )	

# Database SQL Query		
def	bckrequest( connection, sql ):

	return connection.dbrequest( sql )		

# Current Backup Validation Funtion
def bckvalidation( dbrequests ):
	
	for query in dbrequests:
		if not query[ 1 ]:
			query[ 1 ] = bckrequest( query[ 0 ], onedaybeforeSQL )

# Backup Report Type Function
def bckreport( dbrequests, report, sql ):		

	if report == 'bckfullreport':
		print '<h2>Backup Full Report:</h2>'
		for query in dbrequests:
			if not query[ 1 ]:
				sqlvar = id( sql )
				currentdaySQLvar = id( currentdaySQL )
				if sqlvar == currentdaySQLvar:
					print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
					print	'<br>SID: %s' % query[ 0 ].sid
					print	'<br><b><font style="color: red; background-color: black">STATUS: RMAN DB FULL DID NOT RUN</font></b>'
					print   '<br><font style="color: forestgreen">--------------------------------------------</font>'
				else:
					print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
					print	'<br>SID: %s' % query[ 0 ].sid
					print	'<br><b><font style="color: red; background-color: black">STATUS: RMAN DB FULL HAS NEVER RUN</font></b>'
					print	'<br><font style="color: forestgreen">--------------------------------------------</font>'
			else:				
				for bcktype, status, start, end, duration in query[ 1 ]:
					print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
					print	'<br>SID: %s' % query[ 0 ].sid
					print	'<br>BCKTYPE: %s' % bcktype
					if status == 'COMPLETED':
						print   '<br><b><font style="color: lime; background-color: black">STATUS: %s' % status
						print   '</b></font>'
					else:
						print	'<br><b><font style="color: red; background-color: black">STATUS: %s' % status
						print   '</b></font>'
					print	'<br>START: %s' % start
					print	'<br>END: %s' % end
					print	'<br>DURATION: %s HOUR' % duration
					print   '<br><font style="color: forestgreen">--------------------------------------------</font>'
		
                print   '<form action="web.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'

	elif report == 'bckcompletedreport':
		print '<h2>Backup Completed Report:</h2>'
		for query in dbrequests:
			if query[ 1 ]:	
				for bcktype, status, start, end, duration in query[ 1 ]:
					if status == 'COMPLETED':
						print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
						print	'<br>SID: %s' % query[ 0 ].sid
						print	'<br>BCKTYPE: %s' % bcktype
						print	'<br><b><font style="color: lime; background-color: black">STATUS: %s' % status
						print	'</b></font>'
						print	'<br>START: %s' % start
						print	'<br>END: %s' % end
						print	'<br>DURATION: %s HOUR' % duration
						print	'<br><font style="color: forestgreen">--------------------------------------------</font>'
		
                print   '<form action="web.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'

	elif report == 'bckissuereport':
		print '<h2>Backup Issues Report:</h2>'
		for query in dbrequests:
			if not query[ 1 ]:
				sqlvar = id( sql )
				currentdaySQLvar = id( currentdaySQL )
				if sqlvar == currentdaySQLvar:
					print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
					print	'<br>SID: %s' % query[ 0 ].sid
					print	'<br><b><font style="color: red; background-color: black">STATUS: RMAN DB FULL DID NOT RUN</font></b>'
					print	'<br><font style="color: forestgreen">--------------------------------------------</font>'
				else:
					print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
					print	'<br>SID: %s' % query[ 0 ].sid
					print	'<br><b><font style="color: red; background-color: black">STATUS: RMAN DB FULL HAS NEVER RUN</font></b>'
					print	'<br><font style="color: forestgreen">--------------------------------------------</font>'
			else:
				for bcktype, status, start, end, duration in query[ 1 ]:
					if status != 'COMPLETED':
						print	'<br>HOSTNAME: %s' % query[ 0 ].hostname
						print	'<br>SID: %s' % query[ 0 ].sid
						print	'<br>BCKTYPE: %s' % bcktype
						print	'<br><b><font style="color: red; background-color: black">STATUS: %s' % status
						print	'</b></font>'
						print	'<br>START: %s' % start
						print	'<br>END: %s' % end
						print	'<br>DURATION: %s HOUR' % duration
						print	'<br><font style="color: forestgreen">--------------------------------------------</font>'

                print   '<form action="web.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'

# Database Test Connection Function
def testconn():

	conname = form.getvalue( 'connection' )
	username = form.getvalue( 'username' )
	password = form.getvalue( 'password' )
	hostname = form.getvalue( 'hostname' )
	sid = form.getvalue( 'sid' )

	try:
		connection = cx_Oracle.connect( '%s/%s@%s/%s' % ( username, password, hostname, sid ) )
		connver = connection.version
		print	'<b><font style="color: lime; background-color: black">%s connection has been established %s' % ( conname, connver )

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'
	except:
		print   '<b><font style="color: red; background-color: black">%s connection has not been established' % conname

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                print   '<form action="settings.py" method="get">'
                print   '<table>'
                print   '<tr>'
                print   '<td><input type="submit" value="Back"></td>'
                print   '</tr>'
                print   '</table>'
                print   '</form>'
                print   '</div>'

# Database Connection Init Function
def dbconinit():

	sellectconnection = form.getvalue( 'connvar' )
	parser = ConfigParser.SafeConfigParser()
	parser.read( 'connections.ini' )
	sections = parser.sections()

	connvar = {}
	dbconnections = []
	
	if sellectconnection == 'allinstances':
		for connection in sections:
			values = []
			for item, value in parser.items( connection ):
				values.append( value )
			connvar[ connection ] =  values

		for connection in connvar:
			try:
				connection = DBconnection( connvar[ connection ][0], connvar[ connection ][1], connvar[ connection ][2], connvar[ connection ][3] )
				dbconnections.append( connection )
			except:				
				print	'<b><font style="color: red; background-color: black">%s connection cannot be established, Remove/Edit it before running the report' % connection
				
				print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                		print   '<form action="web.py" method="get">'
                		print   '<table>'
               			print   '<tr>'
                		print   '<td><input type="submit" value="Back"></td>'
                		print   '</tr>'
                		print   '</table>'
        	        	print   '</form>'
	                	print   '</div>'

				sys.exit()

	elif sellectconnection in sections:
		values = []
		for item, value in parser.items( sellectconnection ):
			values.append( value )

		try:
			sellectconnection = DBconnection( values[0], values[1], values[2], values[3] )
			dbconnections.append( sellectconnection )
		except:
			print   '<b><font style="color: red; background-color: black">%s connection cannot be established, Remove/Edit it before running the report' % sellectconnection
	
			print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
                	print   '<form action="web.py" method="get">'
               		print   '<table>'
                	print   '<tr>'
                	print   '<td><input type="submit" value="Back"></td>'
                	print   '</tr>'
                	print   '</table>'
                	print   '</form>'
                	print   '</div>'		
	
			sys.exit()

	return dbconnections

# Backup Report Init Function
def repinit():

	dbconnections = dbconinit()	

	backup = form.getvalue( 'bckvar' )
	report = form.getvalue( 'repvar' )

	if backup == 'currentdaySQL' and report == 'full':
		bcktype( currentdaySQL, full, dbconnections )

	elif backup == 'currentdaySQL' and report == 'completed':
		bcktype( currentdaySQL, completed, dbconnections )

	elif backup == 'currentdaySQL' and report == 'issue':
		bcktype( currentdaySQL, issue, dbconnections )

	elif backup == 'historySQL' and report == 'full':
		bcktype( historySQL, full, dbconnections )

	elif backup == 'historySQL' and report == 'completed':
		bcktype( historySQL, completed, dbconnections )

	elif backup == 'historySQL' and report == 'issue':
		bcktype( historySQL, issue, dbconnections )

	else:
		print   '<b><font style="color: red; background-color: black">Please choose 1 Backup Type and 1 Report Type, You cannot use none or multiple Backup/Report Types'	

		print   '<div style="position:absolute; top: 50px; left:0.5%; right:0%">'
        	print   '<form action="web.py" method="get">'
        	print   '<table>'
        	print   '<tr>'
        	print   '<td><input type="submit" value="Back"></td>'
        	print   '</tr>'
        	print   '</table>'
        	print   '</form>'
        	print   '</div>'

# Global Vars
currentdaySQL =	"""SELECT
			INPUT_TYPE,
			STATUS,
			TO_CHAR(START_TIME,'dd/mm/yy hh24:mi') start_time,
			TO_CHAR(END_TIME,'dd/mm/yy hh24:mi') end_time,
			ROUND(ELAPSED_SECONDS/3600,1) hrs
		FROM V$RMAN_BACKUP_JOB_DETAILS
		WHERE INPUT_TYPE='DB FULL' AND TO_DATE(END_TIME,'dd-mm-yy')=TO_DATE(SYSDATE)"""
	
onedaybeforeSQL = """SELECT
			INPUT_TYPE,
			STATUS,
			TO_CHAR(START_TIME,'dd/mm/yy hh24:mi') start_time,
			TO_CHAR(END_TIME,'dd/mm/yy hh24:mi') end_time,
			ROUND(ELAPSED_SECONDS/3600,1) hrs
		FROM V$RMAN_BACKUP_JOB_DETAILS
		WHERE INPUT_TYPE='DB FULL' AND TO_DATE(END_TIME,'dd-mm-yy')=TO_DATE(SYSDATE-1)"""
						
historySQL = """SELECT
			INPUT_TYPE,
			STATUS,
			TO_CHAR(START_TIME,'dd/mm/yy hh24:mi') start_time,
			TO_CHAR(END_TIME,'dd/mm/yy hh24:mi') end_time,
			ROUND(ELAPSED_SECONDS/3600,1) hrs
		FROM V$RMAN_BACKUP_JOB_DETAILS
		WHERE INPUT_TYPE='DB FULL'"""					
	
full = 'bckfullreport'
completed = 'bckcompletedreport'
issue = 'bckissuereport'

# Main Function
if __name__ == "__main__":

	print	"Content-type: text/html\r\n\r\n"
	print	'<head>'
	print	'<title>Oracle DaTabase Backup Report System</title>'
	print	'</head>'
	
	form = cgi.FieldStorage()
	submit = form.getvalue( 'submit' )

	if submit == "Generate":
        	repinit()

	if submit == "Test Connection":
		testconn()
