#!/bin/sh

celery -A fuzzing_worker worker --loglevel=info --autoscale=8 -Q fuzzer

