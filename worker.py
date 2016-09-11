import os
from redis import Redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']
if __name__ == '__main__':
    with Connection(Redis()):
        worker = Worker(map(Queue, listen))
        print("Working!")
        worker.work()
