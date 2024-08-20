from lighthouseweb3 import Lighthouse

lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_path = "D:/PROGRAMMING/WORK/lighthouse-test/resources/chashka_chernyj_belyj_135256_3840x2160.jpg"
image_tag = "test"

response = lighthouse.upload(source=image_path, tag=image_tag)

print("Response: ", response)

"""
It works correctly.
"""
