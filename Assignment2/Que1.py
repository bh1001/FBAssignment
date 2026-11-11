#Convert the time entered in hh,min and sec into seconds.

from datetime import timedelta

sec = 6010
print('Time in Seconds:', sec)

td = timedelta(seconds=sec)
print('Time in hh:mm:ss:', td)

# Use the below code if you want it in a string
print(str(timedelta(seconds=sec)))