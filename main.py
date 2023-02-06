# start process

'''
Razie Hyria
CMPSC 472 - Operating Systems
Lab 2 - Spawning Child Processes
2/3/23

Programming Lab: Parent Process starts two Child Processes
“Processes” are what the operating system calls a program. Students shall write a program that will Start two other processes.

'''

'''import psutil    
"someProgram" in (p.name() for p in psutil.process_iter())

https://stackoverflow.com/questions/7787120/check-if-a-process-is-running-or-not-on-windows
'''
import subprocess # importing the subprocess library to open

# defining the paths for the apps we intend to open 
'''mac file path'''
#mac_calc_path = '/System/Applications/Calculator.app/Contents/MacOS/Calculator' 
#mac_notes_path = "/System/Applications/Notes.app/Contents/MacOS/Notes" 

'''win file path'''
win_calc_path = 'C:\\Windows\\System32\\calc.exe'
win_notes_path = 'C:\\Windows\\System32\\notepad.exe'

#storing the open command into a variable to call on later
calc = subprocess.Popen(win_calc_path)
notes = subprocess.Popen(win_notes_path)
error_flag = False


''' Borrowed "progress exits" function from stackoverflow to use the subprocess functions to check
if the processes we start ared still running and havent been closed by the user

Ref:
https://stackoverflow.com/a/64707896/17628672'''

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False


def starting_subprocess():
    isRunning = True # variable to enter while loop

    while isRunning: # starting the loop

        # opening the apps
        print("Initializing..") 
        print("Starting the calculator app....") 
        notes
        print("Starting the notes app....") 
        calc

        # check if the programs opened successfully
        if calc.poll() is None: 
            print("\nCalc Started Successfully!")
        else:
            print("\Calc failed to load!")
            print("\nExiting Program!")
            error_flag = True
            isRunning = False
        
        if notes.poll() is None: # notes check
            print("\nNotes Started Successfully!")
        else:
            print("\nNotes failed to load!")
            print("\nExiting Program!")
            error_flag = True
            isRunning = False
        
        print("\nclose the programs when you are done!, I'll wait till then..")
        print("\n\n...ZZzzzZZZZzzzz")
        
        # check if the programs were closed/ are running
        process_running = True
        while process_running:

             # checks and alerts which app is open/closed 
            if process_exists("CalculatorApp.exe") == False: #ensuring calculator is running
                print("\n\nCalculator Closed!")
            else:
                print("Calculator is still running!")

            if process_exists("notepad.exe") == False: #ensuring notepad is running
                print("\n\nNotes app closeed!")
            else:
                print("Notes is still running!")
            
            # keeps the program in the while loop
            if process_exists("calc.exe") or process_exists("notepad.exe"):
                continue
            else: # exit nested while loop
                print("Both apps closed")
                process_running = False
        
        # alert user of closure
        print("\nBye! Ill see myself out.. ")
        print("\n\nExiting program")
        isRunning = False # exit nested while loop


if __name__ == "__main__" :
    starting_subprocess()
    if error_flag:
        print("\nSomething went wrong! close any apps, and try the program again")
    else:
        print("\nProgram completed Successfully.")

    # wait()
    # p.terminate()
