import random
import threading
import time


class WorkerThread(threading.Thread):

    def __init__(self, data=None):
        threading.Thread.__init__(self)
        self.data = data
        self.stop = False

    def run(self):
        # while True:
        #     if self.done:
        #         print('Background thread shutting down cleanly')
        #         break
        #     self.delegate()
        #     # Sleep for a little bit ...
        #     time.sleep(random.uniform(0.01, 0.1))
        self.payload()

    def cancel(self):
        """Cancel the execution task

        :return:
        """
        self.stop = True

    def payload(self):
        raise Exception('Please subclass and implement WorkingThread.payload()')
