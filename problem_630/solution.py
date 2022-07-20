import time

# This problem was asked by Apple.
# 
# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.


def wait_and_run(f, wait_time, busy=False, *args, **kwargs):
    seconds = wait_time/1000.0
    if busy:
        now = time.time()
        while (now - time.time()) < seconds:
            pass
    else:
        time.sleep(seconds)
    
    return f(*args, **kwargs)


def test_wait_and_run():
    wait_time = 1  # seconds
    arg = 1
    def plus_two(n):
        return n + 2
    start = time.time()
    ret = wait_and_run(plus_two, wait_time*1000, n=arg)
    end = time.time()
    assert ret == plus_two(arg)
    assert (end - start) > wait_time
    assert (end - start) < 1.05*wait_time


if __name__ == "__main__":
    test_wait_and_run()
