from lighthouseweb3 import Lighthouse
import json

lighthouse = Lighthouse(" ")
image_cid = "bafkreiel3btqgn4jf7ohc5b3ay4qfdyehmxmwv7cd6dt2kbwbxup7wetiq"
json_cid = "bafkreig6u2ihrpm3jfdaaikkaon5zd7rukvb2dvtvymyjn6d4su5utklce"

file_bytes, file_type = lighthouse.download(json_cid)

print("File type: ", file_type)

print(json.loads(file_bytes))

with open("./resources/downloaded.json", "wb") as f:
    f.write(file_bytes)

"""
It works correctly.
"""
