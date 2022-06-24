#digital time infinite loop 
#import time 

#while True: 
  #localtime = time.localtime() 
  #result = time.strftime("%I:%M:%S %p", localtime)
  #print(result) 
  #time.sleep(1) 



from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	
