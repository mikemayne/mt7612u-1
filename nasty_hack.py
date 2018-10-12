with open("RT2870AP.dat") as file:
    for line in file:
        if line[0] is "#":
            continue
        print("\"{}\\n\"".format(line.rstrip()))
