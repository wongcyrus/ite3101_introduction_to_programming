import os
import shutil
import sys
from pathlib import Path

import pytest
import requests
from git import Repo

from config import API_ENDPOINT, API_KEY

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured
SEP = os.sep


def git_push(message):
    try:
        shutil.copyfile(os.path.join('lab', 'autograding.json'),
                        os.path.join('.github', 'classroom', 'autograding.json'))
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
        print("Commit and push with message: " + message)
    except BaseException as bex:
        print(bex)
        print('Some error occured while pushing the code')


try:
    argument_list = sys.argv[1:]
    print(argument_list)
    source_code_file_path = SEP.join(argument_list[0].split(SEP)[-3:])
    print(source_code_file_path)
    code = Path(argument_list[0]).read_text()
    print(code)

    source_code_file_path_segments = source_code_file_path.split(SEP)
    test_code_file_path = os.path.join(
        "tests", source_code_file_path_segments[1], "test_"+source_code_file_path_segments[2])
    print(test_code_file_path)
    retcode = pytest.main(["-x", test_code_file_path])
    if pytest.ExitCode.OK != retcode:
        print("Test Failed!")
        git_push("[skip actions] " + source_code_file_path)        
    else:
        # Google Cloud function is Linux.
        data = {
            "sourceCodeFilePath": source_code_file_path.replace(SEP,"/"),
            "sourceCode": code
        }
        print("Calling to Google Cloud function and run test now, please wait.")
        r = requests.post(API_ENDPOINT+"/pytest?key="+API_KEY, json=data)
        print(r.status_code)
        print(r.text)
        if r.text != "Repeated Successful Test.":
            git_push(source_code_file_path)

except BaseException as ex:
    print(f"Unexpected {ex=}, {type(ex)=}")
    print("Test Failed with exception")
