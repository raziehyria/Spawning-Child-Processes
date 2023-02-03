# Spawning-Child-Processes
CmpSc472 Lab
Programming Lab: Parent Process starts two Child Processes
# Requirements
1. “Processes” are what the operating system calls a program.

2. Students shall write a program that will Start two other processes.

3. The two programs that get executed as child processes, can be any programs. I suggest you execute two system processes, such as Notepad, Calculator or Wordpad.  However, you can demonstrate that any two processes are started.  It can even be an EXE that you wrote.

4. When starting a process, a path may be required.

5. Your program shall check the status to ensure the processes started.  If they did not 
start, display an appropriate error message to the user (monitor).

6. If the two processes start successfully, your program shall go into a wait state.  Stay 
suspended until both child processes exit.

7. When a child process ends, display a message stating so.

8. When both childer processes send, your parent program can get out of the 
suspended state, display a message stating that, and exit itself.