for x in range (1,6):
    lines = str(x)
    for y in range (1,6):
        lines += ('\t%3d' % (x*y))
    print(lines)

