s = "my very long string"

print(s[0])

x = s.upper()

print(x, s)

x = x.lower()
print(x, x==s)

print(x.capitalize())
print(x.title())

print(s.find("n"))
print(s.find("!"))
print(s.find("long"))

print(s.replace('n', 'N').replace('r', 'R'), s)
print(s.replace(' ', "___"))
print(s.replace("very", "not so"))

print(s.split())
print(s.split('very'))

bar_code = "123-45345-56768-3455"
print(bar_code.split('-'))

print("too     many    spaces".split())
#print("too     many    spaces".replace("  ", "")) bad one

x = "too     many    spaces".split()
print(" ".join(x))
print("---some kind of space here---".join(x))

#print(",".join([1,2,3,4,5]))

c, d, p = "cat", "dog", "parrot"
s = "a " + c + ", a " + d + " and a " + p
print(s)

print("a {}, a {} and a {}".format(c, d, p))
print("a {}, a {} and a {}".format(p, d, c))
print("a {2}, a {0} and a {1}".format(c, d, p))
print("a {k1}, a {k2} and a {k3}".format(k1=c, k2=d, k3=p))

print(f"a {c}, a {d} and a {p}")
print(f"5 + 2 = {5+2}")