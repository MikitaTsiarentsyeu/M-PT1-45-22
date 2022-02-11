# f = open("test.txt", 'w')
# f.close()

# with open("C:\\Projects\\IT Academy\\Python\\M-PT1-45-22\\repo\\M-PT1-45-22\\Lessons\\04.02\\test.txt", 'w') as f:
#     f.write("test")

# with open(r"C:\Projects\IT Academy\Python\M-PT1-45-22\repo\M-PT1-45-22\Lessons\04.02\test.txt", 'w') as f:
#     f.write("test")

with open("test.txt", 'w') as f:
    # for i in range(5):
    #     f.write(str(i))
    f.write("some new content\n")
    f.write("more of the new content\n")
    f.writelines(["new line 1\n", "new line 2\n", "new line 3\n"])
    f.writelines("long\nstring\n")
    # f.read()

with open("test.txt", 'r') as f:
    for line in f:
        print(line)

    #print(f.readlines())

    # while True:
    #     print("reading")
    #     if not f.readline():
    #         break
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # f.seek(0)
    # print(repr(f.readline()))
    # print(repr(f.readline()))


    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))

with open("test.txt", 'a') as f:
    f.seek(0)
    f.write("some appended content\n")

with open("test.txt", 'a+') as f:
    f.write("more of the appended content\n")
    f.seek(0)
    print(f.read())

with open("test.txt", 'r+') as f:
    f.write("some content from read")
    for line in f:
        print(line)

with open("test.txt", 'w+') as f:
    f.write("totally new file")
    f.seek(0)
    f.write("test")
    print(f.read())