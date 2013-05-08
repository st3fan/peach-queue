import sys
import subprocess

import logging_worker

if __name__ == "__main__":

    run_uuid = sys.argv[1]
    run_name = sys.argv[2]
    pit_path = sys.argv[3]

    print "Starting peach with", run_uuid, run_name, pit_path

    logging_worker.OnRunStarting.apply_async([run_uuid, run_name], queue='logger')

    #p = subprocess.Popen(["ping", "www.google.com"])
    #print "Process id is", p.pid
    #p.wait()

    logging_worker.OnRunFinished.apply_async([run_uuid, run_name], queue='logger')
