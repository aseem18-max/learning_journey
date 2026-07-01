import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 130)
names = ["Aarav Sharma", "Priya Patel", "Arjun Singh", "Ananya Iyer", "Rohan Gupta", "Saanvi Reddy", "Ishaan Verma", "Aditi Rao", "Vihaan Malhotra", "Kavya Nair"]
for name in names:
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()
engine.say("Thank You")
engine.runAndWait()