import requests

from config import API_ENDPOINT, API_KEY

try:
    print("Calling to Azure function and check grade, please wait.")
    r = requests.post(API_ENDPOINT+"/test-results",
                      headers={"Ocp-Apim-Subscription-Key": API_KEY})
    print(r.status_code)
    result = r.json()
    list(map(lambda x: print(x['RowKey'].replace(
        "->", "/")), sorted(result, key=lambda x: x['RowKey'])))

except BaseException as ex:
    print(f"Unexpected {ex=}, {type(ex)=}")
    print("Check grade Failed with exception")
