import time
from datetime import datetime

ts = time.time()
print(f"Seconds since January 1, 1970: {ts:,.4f} or {ts:.2e} in scientific notation")
now = datetime.now()
formatted_time = now.strftime("%b %d %Y")
print(formatted_time)