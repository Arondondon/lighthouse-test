from lighthouseweb3 import Lighthouse

public_key = "0xe5d1fa424de4689f9d2687353b75d7a8987900fd"
another_key = "0xB23809427cFc9B3346AEC5Bb70E7e574696cAF80"
lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_cid = "bafkreiel3btqgn4jf7ohc5b3ay4qfdyehmxmwv7cd6dt2kbwbxup7wetiq"

# uploads_info = lighthouse.getUploads(public_key)
uploads_info = lighthouse.getUploads(another_key)

print("Uploads_info:", uploads_info)

"""
It doesn't work.
# What is the "public key" (parameter of "getUploads") in this context?
# It's definitely not the same as "image cid", and it doesn't work with the wallet address either.
"""
