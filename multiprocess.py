import time

def worker(num):
    """Thread worker function"""
    print('Worker:', num)
    time.sleep(0.5)

if __name__ == '__main__':
    for i in range(5):
        worker(i)
