import multiprocessing
import time

def worker(num):
    """Thread worker function"""
    print('Worker:', num)
    time.sleep(0.5)

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
