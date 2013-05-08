#!/bin/sh

celery -A logging_worker worker --loglevel=info --autoscale=1 -Q logger -n two

