import threading
import time

# class thread uses threading module
# takes arguements thread_id, a function(func), and it's argument(args)
class Thread(threading.Thread):
    def __init__(self, thread_id, func, args):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.func = func
        self.args = args

    def run(self):
        print("Starting " + self.name)
        self.func(self.args)


# used to to test module
def test_function(arg):
    print("test", arg)


# used to to test module
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    start_time = time.time()
    for a in arr:
        thread = Thread(a, test_function, a)
        thread.start()
        thread.join()
    total_time = time.time() - start_time

    print("time:", total_time)
