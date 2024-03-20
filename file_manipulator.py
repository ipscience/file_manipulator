import sys

if sys.argv[1] == "reverse":
    with open(sys.argv[2]) as f:
        contents = f.read()
        reversed_contents = contents[::-1]
    
    with open(sys.argv[3], 'w') as f:
        f.write(reversed_contents)

elif sys.argv[1] == "copy":
    with open(sys.argv[2]) as f:
        contents = f.read()

    with open(sys.argv[3], 'w') as f:
        f.write(contents)

elif sys.argv[1] == "duplicate-contents":
    with open(sys.argv[2]) as f:
        contents = f.read()

    with open(sys.argv[2], 'w') as f:

        for i in range(int(sys.argv[3])):
            f.write(contents)

elif sys.argv[1] == "replace-string":
    with open(sys.argv[2]) as f:
        contents = f.read()
        replaced_contents = contents.replace(sys.argv[3], sys.argv[4])

    with open(sys.argv[2], 'w') as f:
        f.write(replaced_contents)