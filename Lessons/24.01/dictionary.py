d = {3:"three","one":1}
print(d, type(d))

d = {}
d["new key"] = "new value"
d["pi"] = 3.14
print(d)

print(d["pi"])
d["pi"] = 3.141
# d[12345]
print(d.get("non-existing key", "default value"))
print(d.get("non-existing key"))

print("pi" in d, 456789 in d)
print(d.keys())
print(3.141 in list(d.values()))
print(d.items())

# x = d.popitem()
x = d.pop('pi')
print(d, x)

del d['new key']
print(d)

del d