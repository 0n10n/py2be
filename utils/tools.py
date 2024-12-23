from datetime import datetime
import time

def print_msg(*args, **kwargs):
    msg = ''
    for val in args:
        msg += f'{val}, '
    current_time = datetime.now()
    local_timezone = time.tzname[0] if time.daylight == 0 else time.tzname[1]
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    sep = kwargs['sep'] if 'sep' in kwargs  else ''
    print(f'{formatted_time}|{local_timezone} {sep} {msg[0:-2]}')
    
