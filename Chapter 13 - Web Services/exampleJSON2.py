import json

input = """
[
    {   "id":"001",
        "x":"2",
        "name":"Chuck"
    },
    {   "id":"009",
        "x":"7",
        "name":"Chuck"
    }
]"""

info = json.loads(input)
#print(info)
for item in info:
    print("id:",item["id"])
    print("Name:",item["name"])
    print("x:", item["x"])