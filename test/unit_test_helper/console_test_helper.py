import sys
from io import StringIO
import contextlib

from unit_test_helper import is_answer


@contextlib.contextmanager
def stdout_io(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_script_output(file_relative_path):
    import os
    dirname, filename = os.path.split(os.path.abspath(__file__))

    test_file_path_name = dirname + "/../../lab/" + file_relative_path
    if is_answer:
        test_file_path_name = test_file_path_name.replace(".py", "_ans.py")
    print("testing file: ", test_file_path_name)
    with stdout_io() as s:
        try:
            with open(test_file_path_name, "r") as f:
                exec(f.read())
        except:
            print("File " + test_file_path_name + " not found!")
            return ""
    return s.getvalue()
