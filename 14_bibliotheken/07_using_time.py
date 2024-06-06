import time
seconds = time.time()
print("Sekunden seit 1970", seconds)
local_time = time.ctime(seconds)
print("Ortszeit:", local_time)
