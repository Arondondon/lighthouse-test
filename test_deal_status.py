from lighthouseweb3 import Lighthouse

lighthouse = Lighthouse(token="df71b647.26458965ab2e48068c3fee36bba31a13")
image_cid = "bafkreiel3btqgn4jf7ohc5b3ay4qfdyehmxmwv7cd6dt2kbwbxup7wetiq"
another_cid = "QmT9shXpKcn4HRbJhXJ1ZywzwjEo2QWbxAx4SVgW4eYKjG"

# deal_status = lighthouse.getDealStatus(image_cid)
deal_status = lighthouse.getDealStatus(another_cid)

# print("Deal_status: ", deal_status)
print("Deal_status: ", *deal_status[0].items(), sep="\n")

"""
It works, but an empty list is returned.
Apparently, this cannot be done until the deal is completed, but that's not certain
because the same result is return with random CID
Edited: It works correctly some time after loading
"""
