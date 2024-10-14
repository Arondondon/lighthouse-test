from lighthouseweb3 import Lighthouse
import json
import tempfile

lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_path = "D:/PROGRAMMING/WORK/lighthouse-test/resources/metadata.json"
image_tag = "test"

data = {
    "number1": 3,
    "number2": 4,
    "str1": "str1",
    "str2": "str2",
    "list1": [1, 2, 3],
    "list2": [4, 5, 6],
    "dict1": {"key1": "value1", "key2": "value2"},
}

json_data = json.dumps(data).encode("utf-8")
tmp = tempfile.NamedTemporaryFile(delete=False)
with open(tmp.name, "wb") as f:
    f.write(json_data)
response = lighthouse.upload(source=tmp.name, tag=image_tag)

print("Response: ", response['data']['Hash'])

"""
It works correctly.
"""
