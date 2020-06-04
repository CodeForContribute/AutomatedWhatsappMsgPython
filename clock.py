from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from automated_whatsapp_msg import send_msg

sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', hours=12)
sched.start()

if __name__ == '__main__':
    sched.start()