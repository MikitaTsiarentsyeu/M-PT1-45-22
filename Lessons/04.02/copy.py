chunk = 10000000

with open("test.mp4", 'rb') as donor:
    with open("test_copy.mp4", 'wb') as receiver:
        number = 1
        while True:
            # print(f"copying chunk number {number}")
            piece = donor.read(chunk)
            if piece:
                receiver.write(piece)
                number += 1
            else:
                break
        print("done!")