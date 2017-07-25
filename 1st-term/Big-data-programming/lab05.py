# 1
def pinkify():
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath("garden.jpg")
    pic = makePicture(fn)

    width = getWidth(pic)
    height = getHeight(pic)
    for x in range(width):
        for y in range(height):
            p = getPixel(pic, x, y)
            if getRed(p) > 100 and getGreen(p) > 100 and getBlue(p) > 100:
                setColor(p, pink)
    show(pic)

# pinkify()

# 2
def pickPosterizeValue(current):
    if current < 64: return 31
    elif current < 128: return 95
    elif current < 192: return 159
    elif current < 256: return 223

def posterize(picture):
    for p in getPixels(picture):
        setRed(p, pickPosterizeValue(getRed(p)))
        setGreen(p, pickPosterizeValue(getGreen(p)))
        setBlue(p, pickPosterizeValue(getBlue(p)))
    return picture

def main_ex2():
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath("anthony.jpg")
    pic = makePicture(fn)
    pic = posterize(pic)
    show(pic)

# main_ex2()

# 3
def change_sky_to_blue(pic):
    for p in getPixels(pic):
        if getRed(p) + getGreen(p) < getBlue(p) + 100:
            setColor(p, blue)
    return pic

def chromakey(des, src):
    width = getWidth(des)
    height = getHeight(des)

    for x in range(width):
        for y in range(height):
            src_p = getPixel(src, x, y)
            des_p = getPixel(des, x, y)
            if getColor(des_p) == blue:
                setColor(des_p, getColor(src_p))
    return des

def main_ex3():
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath("statue-tower.jpg")
    statue_tower = makePicture(fn)
    fn = getMediaPath("jungle2.jpg")
    jungle = makePicture(fn)

    statue_tower = change_sky_to_blue(statue_tower)
    statue_tower = chromakey(statue_tower, jungle)
    show(statue_tower)

# main_ex3()

# 4
def make_grey_scale(pic):
    for p in getPixels(pic):
        mean = (getRed(p) + getGreen(p) + getBlue(p)) / 3
        # setColor(p, makeColor(mean*0.299, mean*0.587, mean*0.114)) # better gray scale
        setColor(p, makeColor(mean, mean, mean))
    return pic

def bit_plane_slicing(pics):
    for pic in pics:
        pic = make_grey_scale(pic)
    width = getWidth(pic)
    height = getHeight(pic)

    for x in range(width):
        for y in range(height):
            bits = getRed(getPixel(pic, x, y))
            for i in range(8):
                if bits & 2**i == 2**i:
                    setColor(getPixel(pics[i], x, y), white)
                else:
                    setColor(getPixel(pics[i], x, y), black)
    return pics

def main_ex4():
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath("eiffel.jpg")
    eiffels = [makePicture(fn) for _ in range(8)]

    eiffels = bit_plane_slicing(eiffels)
    for e in eiffels:
        show(e)

# main_ex4()

# 5.
def make_grey_scale(pic):
    for p in getPixels(pic):
        mean = (getRed(p) + getGreen(p) + getBlue(p)) / 3
        # setColor(p, makeColor(mean*0.299, mean*0.587, mean*0.114)) # better gray scale
        setColor(p, makeColor(mean, mean, mean))
    return pic

def test_compress(pic, fn):
    width = getWidth(pic)
    height = getHeight(pic)
    result = makeEmptyPicture(width / 2, height)

    for x in range(width):
        for y in range(height):
            p = getPixel(pic, x, y)
            c = getRed(p) & int('11110000', 2)
            setColor(getPixel(pic, x, y), makeColor(c, c, c))
    return pic

def compress_picture(pic, fn):
    width = getWidth(pic)
    height = getHeight(pic)
    result = makeEmptyPicture(width / 2, height)

    for dest_x, x in enumerate(range(0, width, 2)):
        for y in range(height):
            p1 = getPixel(pic, x, y)
            p2 = getPixel(pic, x + 1, y)
            c_p1 = getRed(p1) & int('11110000', 2)
            c_p2 = getRed(p2) & int('11110000', 2)
            comp = c_p1 + (c_p2 >> 4)
            setColor(getPixel(result, dest_x, y), makeColor(comp, comp, comp))
    writePictureTo(result, fn)
    return

def extract_picture(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath(fn)
    comp_pic = makePicture(fn)
    width = getWidth(comp_pic)
    height = getHeight(comp_pic)
    result = makeEmptyPicture(width * 2, height)

    for src_x, x in enumerate(range(0, width * 2, 2)):
        for y in range(height):
            p = getPixel(comp_pic, src_x, y)
            bits = getRed(p)
            l = bits & int('11110000', 2)
            r = (bits & int('00001111', 2)) << 4
            setColor(getPixel(result, x, y), makeColor(l, l, l))
            setColor(getPixel(result, x + 1, y), makeColor(r, r, r))
    return result

def main_ex5():
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    fn = getMediaPath("eiffel.jpg")
    eiffel = makePicture(fn)
    eiffel = make_grey_scale(eiffel)

    dest_fn = 'aaaaaaaaaaaaaaaaaaaaaaaaa.jpg'
    compress_picture(eiffel, dest_fn)
    pic = extract_picture(dest_fn)
    show(pic)
    show(test_compress(eiffel, dest_fn))


main_ex5()
