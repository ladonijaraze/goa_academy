def getVolumeOfcuboid(length, width, height):
    return length * width * height

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)