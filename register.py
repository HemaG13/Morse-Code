#!"C:\Python38\python.exe"
print("Content-Type:text/html")
print()
import cgi
import webbrowser


form = cgi.FieldStorage()

fname = form.getvalue("fname")
lname = form.getvalue("lname")
email = form.getvalue("email")
mobnum = form.getvalue("mobnum")
password = form.getvalue("password")
password2 = form.getvalue("password2")


import mysql.connector

con = mysql.connector.connect(user='root', password='', host='localhost', database='webpython')
cur = con.cursor()

#if password==password2:
cur.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,mobnum,password,password2))

#else:
	#print("Incorrect Password")
con.commit()
cur.close()
con.close()
webbrowser.open("http://localhost/Morse_HTML/second.html")
#print("<h3>data inserted successfully</h3>")
#print("<a href='http://localhost/Morse_HTML/first.html'>click here to go back</a>")