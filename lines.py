def drawline(length, direction):
    if direction == "h":
        print("-" * length, end="")
    if direction == "v":
        print(("|" + "\n") *length ) 
drawline(5, "v")
