import psutil
# get all PIDs
psutil.pids()
#[0, 4, 472, 648, 756, ...] but for iteration you should use process_iter()
for proc in psutil.process_iter():
     try:
         if proc.name() == "gpicview":
             proc.terminate()
     except psutil.NoSuchProcess:
         pass