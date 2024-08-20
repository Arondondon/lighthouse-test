from lighthouseweb3 import Lighthouse

lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_cid = "bafkreiel3btqgn4jf7ohc5b3ay4qfdyehmxmwv7cd6dt2kbwbxup7wetiq"
image_tag = "test"

downloaded_files = lighthouse.getTagged(image_tag)

print("Downloaded files: ", downloaded_files)

"""
It works correctly.
"""
