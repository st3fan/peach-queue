from celery import Celery

celery = Celery('tasks', broker='amqp://guest@192.168.20.157//')

@celery.task
def OnRunStarting(run_uuid, run_name):
    print "Starting run", run_uuid, run_name

@celery.task
def OnTestStarting(run_uuid, run_name, test_name):
    print "Starting test", run_uuid, run_name, test_name

@celery.task
def OnTestFinished(run_uuid, run_name, test_name):
    print "Finished test", run_uuid, run_name, test_name

@celery.task
def OnRunFinished(run_uuid, run_name):
    print "Finished run", run_uuid, run_name
