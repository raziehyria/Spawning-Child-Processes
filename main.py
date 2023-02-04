# start process
'''

Razie Hyria
CMPSC 472 - Operating Systems
Lab 2 - Spawning Child Processes
2/3/23

Programming Lab: Parent Process starts two Child Processes

'''

'''import psutil    
"someProgram" in (p.name() for p in psutil.process_iter())

https://stackoverflow.com/questions/7787120/check-if-a-process-is-running-or-not-on-windows
'''

# importing the subprocess library to open
import subprocess

# defining the paths for the apps we intend to open 
calc_path = '/System/Applications/Calculator.app/Contents/MacOS/Calculator' # system calc path (mac)
notes_path = "/System/Applications/Notes.app/Contents/MacOS/Notes" # system calc path (window)

subprocess.Popen(['open', notes_path])
isRunning = False

while isRunning: 
    print("Initializing..") # starting the loop
    print("Starting the calculator app....") # opening the calc app
    print("Starting the notes app....") # opening the notes app
    print("Calculator app closed!")
    print("Notes app closed!")
    print("Come back ")

    pass



if __name__ == "__main__" :
    print("hi")
