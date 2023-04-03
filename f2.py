# BONA FERUZZA
# 10950675
# FPEN
import PySimpleGUI as sg
import pyttsx3

# initialize the text-to-speech engine
Crystal = pyttsx3.init()

# define the GUI layout
layout = [
    [sg.Text("Enter your text here:")],
    [sg.InputText(key="input_text")],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", group_id="voice", key="male_voice"), sg.Radio("Female", group_id="voice", key="female_voice")],
    [sg.Button("Speak"), sg.Button("Stop")]
]

# create the GUI window
window = sg.Window("Text-to-Speech App", layout)

# main event loop
while True:
    event, values = window.read()

    # exit the app if the window is closed or "Stop" button is clicked
    if event == sg.WINDOW_CLOSED or event == "Stop":
        break

    # speak the input text with the selected voice when "Speak" button is clicked
    if event == "Speak":
        # set the voice type based on the user selection
        if values["male_voice"]:
            voices = Crystal.getProperty('voices')
            Crystal.setProperty("voice", voices[0].id)
        elif values["female_voice"]:
            voices= Crystal.getProperty('voices')
            Crystal.setProperty("voice", voices[1].id)

        # set the speaking speed and volume (optional)
        Crystal.setProperty("rate", 150)
        Crystal.setProperty("volume", 1.0)

        # convert the input text to spoken words
        Crystal.say(values["input_text"])
        Crystal.runAndWait()

# close the window and release the resources
window.close()
Crystal.stop()