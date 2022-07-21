import errno
import os
import platform
import signal
from functools import wraps
from threading import Timer


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _window_handle_timeout():
            os.kill(os.getpid(), signal.CTRL_C_EVENT)

        def _linux_handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            if platform.system() == "Windows":
                timer = Timer(seconds, _window_handle_timeout)
                try:
                    timer.start()
                    result = func(*args, **kwargs)
                finally:
                    timer.cancel()
                return result
            else:
                signal.signal(signal.SIGALRM, _linux_handle_timeout)
                signal.alarm(seconds)
                try:
                    result = func(*args, **kwargs)
                finally:
                    signal.alarm(0)
                return result

        return wraps(func)(wrapper)

    return decorator
