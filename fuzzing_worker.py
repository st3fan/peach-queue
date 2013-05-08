import subprocess
import time

from celery import Celery

celery = Celery('tasks', broker='amqp://guest@192.168.20.157//', backend='amqp')

@celery.task
def RunFuzzer(run_uuid, run_name, pit_name):
    print "Running fuzzer", run_uuid, run_name, pit_name
    subprocess.call(["/Users/stefan/Mozilla/mini-peach/env/bin/python", "/Users/stefan/Mozilla/mini-peach/peach.py", run_uuid, run_name, pit_name])
