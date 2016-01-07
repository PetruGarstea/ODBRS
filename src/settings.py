#!/usr/bin/python

import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.read( "connections.ini" )
sections = parser.sections()

print   "Content-type:text/html\r\n\r\n"
print   '<html>'
print   '<head>'
print   '<title>Oracle DaTabase Backup Report System</title>'
print   '</head>'
print   '<body>'
print   '<h2>Oracle DaTabase Backup Report System Settings:</h2>'
print   '<br>'

print   '<div style="position:absolute; top: 75px; left:0%; right:0%">'
print   '<table style="width:59%" border="1" cellpadding="5">'

print	'<tr>'
print   '<form action="chsettings.py" method="get">'
print   '<td align="center"><input type="text" name="connection" placeholder="Connection"></td>'
print	'<td align="center"><input type="text" name="username" placeholder="Username"></td>'
print   '<td align="center"><input type="text" name="password" placeholder="Password"></td>'
print   '<td align="center"><input type="text" name="hostname" placeholder="Hostname"></td>'
print   '<td align="center"><input type="text" name="sid" placeholder="SID"></td>'
print	'<td align="center"><input type="submit" name="submit" value="Add"></td>'
print	'</form>'
print	'</tr>'

print   '<tr>'
print   '<form action="chsettings.py" method="get">'
print   '<td align="center"><select name="connvar">'

for connection in sections:
	print	'<option value=%s>%s</option>' % (connection, connection)

print	'</select></td>'
print   '<td align="center"><input type="text" name="username" placeholder="Username"></td>'
print   '<td align="center"><input type="text" name="password" placeholder="Password"></td>'
print   '<td align="center"><input type="text" name="hostname" placeholder="Hostname"></td>'
print   '<td align="center"><input type="text" name="sid" placeholder="SID"></td>'
print   '<td align="center"><input type="submit" name="submit" value="Edit"></td>'
print	'</form>'
print   '</tr>'

print   '<tr>'
print   '<form action="chsettings.py" method="get">'
print   '<td colspan="3" align="center"><select name="connvar">'

for connection in sections:
        print   '<option value=%s>%s</option>' % (connection, connection)

print	'</select></td>'
print	'<td colspan="3" align="center"><input type="submit" name="submit" value="Remove"></td>'
print   '</form>'
print	'</tr>'

print   '</table>'
print	'</div>'

print   '<div style="position:absolute; top: 190px; left:0%; right:0%">'
print   '<table>'
print   '<tr>'
print   '<td><b>*** Before Adding/Editing please use Test Connection</b></td>'
print   '</tr>'
print   '</table>'
print	'</div>'

print   '<div style="position:absolute; top: 300px; left:0%; right:0%">'
print   '<form action="driver.sh" method="get">'
print   '<table style="width:59%" border="1" cellpadding="5">'
print   '<tr>'
print   '<td align="center"><input type="text" name="connection" placeholder="Connection"></td>'
print   '<td align="center"><input type="text" name="username" placeholder="Username"></td>'
print   '<td align="center"><input type="text" name="password" placeholder="Password"></td>'
print   '<td align="center"><input type="text" name="hostname" placeholder="Hostname"></td>'
print   '<td align="center"><input type="text" name="sid" placeholder="SID"></td>'
print   '<td align="center"><input type="submit" name="submit" value="Test Connection"></td>'
print   '</tr>'
print   '</table>'
print   '</form>'
print   '</div>'

print   '<div style="position:absolute; bottom: 0px; left:0%; right:0%">'
print   '<form action="web.py" method="get">'
print   '<table style="width:100%">'
print   '<tr>'
print   '<td><input type="submit" value="Home"></td>'
print   '<td align="right">Developed By Petru Garstea</td>'
print   '</tr>'
print   '</table>'
print   '</form>'
print   '</div>'

print   '</body>'
print   '</html>'
