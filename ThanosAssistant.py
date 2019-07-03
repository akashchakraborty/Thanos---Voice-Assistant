import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from selenium import webdriver
import os
import smtplib



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
#print(voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()



def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak(" Good    Morning Sir!")
	elif hour>=12 and hour<18:
		speak(" Good    Afternoon  Sir!")
	else:
		speak(" Good    Evening  Sir!")

	speak("I am Thaaanooos ! How may I help you?")

def takeCommand():
	# It takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source :
		print("Listening... ")
		#r.pause_threshold = 0.8
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User Said: {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"
	return query

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('YOURMAILID', 'YOURPASSWORD')
	server.sendmail('YOURMAILID',to,content)
	server.close()


if __name__ == '__main__':
	#speak("Akash is a good boy")
	wishMe()
	while True:
		query = takeCommand().lower()

		# logic for executing tasks
		if 'wikipedia' in query:
			speak('Searching wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 2)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'google' in query:
			webbrowser.open("google.com")

		elif 'stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'play some smooth music' in query:
			webbrowser.open("gaana.com/song/smooth-music")
		elif 'weather' in query:
			driver = webdriver.Firefox()
			city = str(input("Enter the name of the city you want the forecast for: "))
			driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
			we = driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text
			speak(we)
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")
		elif 'open text editor' in query:
			editor_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(editor_path)

		elif "email to harry" in query:
			try:
				speak("What should I say ?")
				content = takeCommand()
				to = "HARRY'SMAILID"
				sendEmail(to,content)
				speak("Email has been sent")

			except Exception as e:
				print(e)
				speak(" I am afraid I could not perform the task successfully ")

		elif "thank you" in query:
			speak("It's my pleasure to help you sir!")
