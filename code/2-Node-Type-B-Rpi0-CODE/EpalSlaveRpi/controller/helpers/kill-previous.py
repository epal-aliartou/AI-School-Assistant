import os
import signal
from subprocess import check_output

def get_pid(name):
    return check_output(["pidof", name])

def main():
    os.kill(get_pid("gpicview"), signal.SIGTERM) #or signal.SIGKILL 

if __name__ == "__main__":
    main()