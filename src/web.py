#!/usr/bin/python

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.read( "connections.ini" )
sections = parser.sections()

print	"Content-type:text/html\r\n\r\n"
print   '<html>'
print	'<head>'
print	'<title>Oracle DaTabase Backup Report System</title>'
print	'</head>'
print	'<body>'
print	'<h2>Oracle DaTabase Backup Report System:</h2>'
print	'<br>'

print   '<div style="position:absolute; top: 75px; left:0%; right:0%">'
print	'<form action="driver.sh" method="get">'

print	'<table style="width:35%" border="1" cellpadding="5">'
print	'<tr>'
print	'<td colspan="4" align="center">'
print	'<select name="connvar">'
print	'<option value=allinstances>All Instances</option>'

for connection in sections:
        print   '<option value=%s>%s</option>' % (connection, connection)

print	'</select>'
print	'</td>'
print	'</tr>'

print	'<tr>'
print	'<td align="center">Backup: </td>'
print	'<td align="center"><input type="checkbox" name="bckvar" value="currentdaySQL"> Current</td>'
print	'<td colspan="2" align="center"><input type="checkbox" name="bckvar" value="historySQL"> History</td>'
print	'</tr>'
print	'<tr>'
print	'<td align="center">Report: </td>'
print	'<td align="left"><input type="checkbox" name="repvar" value="full"> Full</td>'
print	'<td align="center"><input type="checkbox" name="repvar" value="completed"> Completed</td>'
print	'<td align="center"><input type="checkbox" name="repvar" value="issue"> Issue</td>'
print	'</tr>'

print	'<tr>'
print	'<td colspan="4" align="center"><input type="submit" name="submit" value="Generate"></td>'
print	'</tr>'
print   '</table>'

print	'</form>'
print	'</div>'

print   '<div style="position:absolute; bottom: 0px; left:0%; right:0%">'
print	'<form action="settings.py" method="get">'
print 	'<table style="width:100%">'
print   '<tr>'
print	'<td><input type="submit" value="Settings"></td>'
print	'<td align="right">Developed By Petru Garstea</td>'
print   '</tr>'
print	'</table>'
print	'</form>'
print   '</div>'

print	'</body>'
print	'</html>'
