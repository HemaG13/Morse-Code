#!"C:\Python38\python.exe"
print("Content-Type:text/html")
print()
import cgi
import os
import webbrowser
import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

cmd = 'python morse.py --shape-predictor shape_predictor_68_face_landmarks.dat'

os.system(cmd)

webbrowser.open_new_tab("http://localhost/Morse_HTML/fourth.html")



#print("<script type='text/javascript'>const signUpButton = document.getElementById('signUp');const signInButton = document.getElementById('signIn');const container = document.getElementById('container');signUpButton.addEventListener('click', () => {container.classList.add('right-panel-active');});signInButton.addEventListener('click', () => {container.classList.remove('right-panel-active');});")
#print("<a href='http://localhost/Morse_HTML/fourth.html'>click here to go back</a>")


