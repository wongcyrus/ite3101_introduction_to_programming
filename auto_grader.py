import os
import shutil
import sys
from pathlib import Path

import pytest
import requests
from git import Repo

from config import API_ENDPOINT, API_KEY

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured


def git_push(message):
    try:
        shutil.copyfile('lab/autograding.json',
                        '.github/classroom/autograding.json')
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
        print("Commit and push with message: " + message)
    except BaseException:
        print('Some error occured while pushing the code')


try:
    argumentList = sys.argv[1:]
    print(argumentList)

    sourceCodeFilePath = "/".join(argumentList[0].split("/")[3:])

    print(sourceCodeFilePath)
    code = Path(argumentList[0]).read_text()
    print(code)

    source_code_file_path_segments = sourceCodeFilePath.split("/")
    test_code_file_path = os.path.join(
        "tests", source_code_file_path_segments[1], "test_"+source_code_file_path_segments[2])
    print(test_code_file_path)
    retcode = pytest.main(["-x", test_code_file_path])
    if pytest.ExitCode.OK != retcode:
        print("Test Failed!")
        git_push("[skip actions] " + sourceCodeFilePath)
        sys.exit(0)
    else:
        data = {
            "sourceCodeFilePath": sourceCodeFilePath,
            "sourceCode": code
        }
        print("Calling to Azure function and run test now, please wait.")
        r = requests.post(API_ENDPOINT+"/pytester", json=data,
                          headers={"Ocp-Apim-Subscription-Key": API_KEY})
        print(r.status_code)
        print(r.text)
        git_push(sourceCodeFilePath)

except BaseException as ex:
    print(f"Unexpected {ex=}, {type(ex)=}")
    print("Test Failed with exception")
