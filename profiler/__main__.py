import gevent
import csv
import sys
from locust.env import Environment
from locust.log import setup_logging

from .locustfile import BasicUser

import argparse


parser = argparse.ArgumentParser(description='Run a load test.')
parser.add_argument('name', type=str, 
                    help='test name')
parser.add_argument('time', type=int, default=60, nargs='?',)
parser.add_argument('users', type=int, default=4, nargs='?',)

args = parser.parse_args()

setup_logging("INFO", None)

class StatsEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_meta_data = []

# setup Environment and Runner
env = StatsEnvironment(user_classes=[BasicUser])
runner = env.create_local_runner()

# execute init event handlers (only really needed if you have registered any)
env.events.init.fire(environment=env, runner=runner)

# start the test
runner.start(args.users, spawn_rate=5)

# in 60 seconds stop the runner
gevent.spawn_later(args.time, lambda: runner.quit())

# wait for the greenlets
runner.greenlet.join()

with open(f'{args.name}_fullstats.csv', 'w', newline='') as csvfile:
    fieldnames = list(env.request_meta_data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    for row in env.request_meta_data:
        writer.writerow(row)
