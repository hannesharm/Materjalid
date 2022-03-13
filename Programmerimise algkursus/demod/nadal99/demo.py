## lugemine
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)

    sum = 0
    for line in lines:
        sum += int(line.strip())

    print(sum)

##kirjutamine
with open("write.txt", "a") as f:
    f.write("sisu\na\n")
    f.write("veel sisu")
