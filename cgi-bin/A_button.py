#!/usr/bin/env python3

print("Content-type: text/html\n")
print("""
<!DOCTYPE HTML>
<html>
<head>
	<title>A_button</title>
</head>
<body>
	<form action="A_button.py">
	<input type="submit" value="A_button">
	</form>
""")

print('<p><{0}>ABOUT</{0}></p>'.format('i'))

print("""
</body>
</html>
""")