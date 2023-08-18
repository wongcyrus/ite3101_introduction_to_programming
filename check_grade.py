import requests
from config import API_ENDPOINT, API_KEY

try:
    print("Calling to Google Cloud function and check grade, please wait.")
    r = requests.post(API_ENDPOINT+"/testresults?key="+API_KEY)
    results = r.json()
    for result in results:
        print(result)

except BaseException as ex:
    print(f"Unexpected {ex=}, {type(ex)=}")
    print("Check grade Failed with exception")
