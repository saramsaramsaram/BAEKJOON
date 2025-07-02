a = input()

if (
    a[0] == '_' or
    a[-1] == '_' or
    '__' in a or
    (any(c == '_' for c in a) and any(c.isupper() for c in a)) or
    a[0].isupper()
):
    print("Error!")
else:
    if '_' in a:  # C++ → Java
        underbar = False
        for i in a:
            if i == '_':
                underbar = True
            elif underbar:
                print(i.upper(), end='')
                underbar = False
            else:
                print(i, end='')
    else:  # Java → C++
        for i in a:
            if i.isupper():
                print('_' + i.lower(), end='')
            else:
                print(i, end='')
