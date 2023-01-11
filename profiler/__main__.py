import gevent
import csv
import sys
from locust.env import Environment
from locust.log import setup_logging

from .locustfile import BasicUser

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
runner.start(4, spawn_rate=5)

# in 60 seconds stop the runner
gevent.spawn_later(60, lambda: runner.quit())

# wait for the greenlets
runner.greenlet.join()
name = sys.argv[1]
if not name:
    name = 'test'
with open(f'{name}_fullstats.csv', 'w', newline='') as csvfile:
    fieldnames = list(env.request_meta_data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    for row in env.request_meta_data:
        writer.writerow(row)
