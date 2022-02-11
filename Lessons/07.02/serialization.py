import json
import pickle

text_json = """
{
    "width":500,
    "height":500,
    "resolution":96,
    "quality":96,
    "settings":[
        {
            "filename":"_preview1.jpg",
            "seek":10
        },
        {
            "filename":"_preview2.jpg",
            "seek":35
        },
        {
            "filename":"_preview3.jpg",
            "seek":70
        },
        {
            "filename":"_preview4.jpg",
            "seek":95
        }
    ]
}
"""

d = json.loads(text_json)
print(type(d), d)

print(d["settings"][0]["seek"])
d["settings"][0]["seek"] = 15

#print(json.dumps(d))

with open("test.json", 'w') as f:
    json.dump(d, f)

with open("test.json", 'r') as f:
    d = json.load(f)

d["test_tuple"] = (1,2,3,4,5,"six",7.0)

# with open("test.json", 'w') as f:
#     json.dump(d, f)

# with open("test.json", 'r') as f:
#     d = json.load(f)

print(d["test_tuple"], type(d["test_tuple"]))

pickled = pickle.dumps(d)
d = pickle.loads(pickled)
print(d["test_tuple"], type(d["test_tuple"]))

pickled = pickle.dumps(print)
new_print = pickle.loads(pickled)

new_print("hello from new print function")
print(id(print), id(new_print))