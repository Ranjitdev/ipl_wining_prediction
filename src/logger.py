import logging
import os
import sys
from datetime import datetime

log_time = f"{datetime.now().strftime('%a %d-%b-%Y %H-%M-%S')}"
log_path = os.path.join(os.getcwd(), 'logs', log_time)
log_name = os.path.join(log_path, log_time+'.log')
os.makedirs(log_path, exist_ok=True)

logging.basicConfig(
    filename=log_name,
    format="[%(asctime)s] [%(lineno)d %(name)s %(levelname)s] %(message)s",
    level=logging.INFO
)