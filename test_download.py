from lighthouseweb3 import Lighthouse

lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_cid = "bafkreiel3btqgn4jf7ohc5b3ay4qfdyehmxmwv7cd6dt2kbwbxup7wetiq"

file_bytes, file_type = lighthouse.download(image_cid)

print("File type: ", file_type)

with open("./resources/downloaded.jpg", "wb") as f:
    f.write(file_bytes)

"""
It works correctly.
"""
