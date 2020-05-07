i = 0
while i < 5:
    f = open("input.txt", "r")
    char = f.read(1)
    f.close
    if char == "^":
        f = open("input.txt", "r+")
        f.truncate()
        f.write("$h\n")
        f.close()
        i = i + 1
    response = open("response_mirobot.txt", "r")
    data = response.readlines()
    response.close()
    length = len(data)
    if length > 0:
        while 1:
            if "ok" in data[length - 2]:
                break
            response = open("response_mirobot.txt", "r")
            data = response.readlines()
            response.close()
            length = len(data)        
