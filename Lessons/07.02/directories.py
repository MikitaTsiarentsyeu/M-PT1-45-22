import os

print(os.name)

print(os.path.sep)

print(f"test{os.path.sep}test{os.path.sep}test.txt")

print(os.path.join("test", "test", "test.txt"))

print(os.getcwd())

#with open("test.txt", 'r') as f: pass

# os.chdir("test")

print(os.getcwd())

# os.mkdir("test level 2/test level 3/test level 4")

# os.makedirs("test level 2/test level 3/test level 4")

print(os.listdir())

print(list(os.walk(os.getcwd())))

#os.remove("test.txt")

os.removedirs("test")