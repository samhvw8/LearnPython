#! coding: utf-8
import sys
from rq import Queue
from redis import Redis
from function import checkport
import time


if len(sys.argv) != 2:
    print "please run like format\n"
    exit("python {} [File-contain-ip:port-to-check]\n".format(sys.argv[0]))

f = open(sys.argv[1], "r")

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)

jobs = []

for ip_and_port in f:

    detail = ip_and_port.strip().split(":")
    job = q.enqueue(checkport, detail[0], int(detail[1]))
    jobs.append(job)


checked = dict()

while True:
    for job in jobs:
        is_change = 0
        while job.result is None:
            continue

        ip_and_port = "{}:{}".format(job.args[0], job.args[1])  # e.g 127.0.0.0:80
        if ip_and_port in checked:
            if checked[ip_and_port] != job.result:
                checked[ip_and_port] = job.result
                is_change = 1
        else:
            checked[ip_and_port] = job.result
            is_change = 1

        if is_change:
            if job.result:
                print "[Y]", ip_and_port
            else:
                print "[N]", ip_and_port

        jobs.remove(job)
        job = q.enqueue(checkport, job.args[0], job.args[1])
        jobs.append(job)
