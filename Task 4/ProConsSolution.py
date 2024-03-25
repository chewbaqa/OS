import threading
import queue
import time
import random

# Create a queue of size 5
buffer = queue.Queue(maxsize=5)


class ProducerThread(threading.Thread):
    def run(self):
        for _ in range(20):
            if not buffer.full():
                item = random.randint(1, 10)
                buffer.put(item)
                print(
                    f"Producer added item {item} to buffer. Buffer size is {buffer.qsize()}"
                )
            time.sleep(random.randint(1, 5))


class ConsumerThread(threading.Thread):
    def run(self):
        for _ in range(20):
            if not buffer.empty():
                item = buffer.get()
                print(
                    f"Consumer consumed item {item} from buffer. Buffer size is {buffer.qsize()}"
                )
            time.sleep(random.randint(1, 5))


# Create one producer and one consumer
ProducerThread().start()
ConsumerThread().start()
