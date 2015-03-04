#!/usr/bin/env python3
import cgi

text1 = cgi.FieldStorage().getfirst("TEXT_1", "7")

print("Content-type: text/html\n")
print("""
<!DOCTYPE HTML>
<html>
<head>
	<title>Index</title>
</head>
<body>
	<form action="button.py">
	<input type="text" name="TEXT_1">
	<input type="submit" value="button">
	</form>
""")
if int(text1) < 7:
	print('<a href="../about.html"><H{0}>About</H{0}></a>'.format(text1))
	print("<p>SIZE of About: {}</p>".format(text1))
else:
	text1 = '2'
	print('<a href="../about.html"><H{0}>About</H{0}></a>'.format(text1))
	print("<p>SIZE of About: {} default</p>".format(text1))
print("""
</body>
</html>
""")