import random
import threading
import time


class WorkerThread(threading.Thread):

    def __init__(self, delegate):
        threading.Thread.__init__(self)
        self.delegate = delegate
        self.done = False

    def run(self):
        while True:
            if self.done:
                print('Background thread shutting down cleanly')
                break
            if hasattr(self.delegate, "refresh_in_thread"):
                self.delegate.refresh_in_thread()

            # Sleep for a little bit ...
            time.sleep(random.uniform(0.01, 0.1))
