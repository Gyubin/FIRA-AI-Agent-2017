# 1.
def smallValue(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    path = getMediaPath(fn)
    sound = makeSound(path)

    minimum = getSampleValueAt(sound, 0)
    for s in getSamples(sound):
        v = getSampleValue(s)
        if v < minimum:
            minimum = v

    return minimum

def main_ex1():
    fn = "computer.wav"
    print("Minimum sample value of " + fn + " is", smallValue(fn))

# main_ex1()

# 2.
def negToZero(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    path = getMediaPath(fn)
    sound = makeSound(path)

    for s in getSamples(sound):
        if getSampleValue(s) < 0:
            setSampleValue(s, 0)

    return sound

def justPlay(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    path = getMediaPath(fn)
    sound = makeSound(path)
    play(sound)

def main_ex2():
    fn = "preamble.wav"

    # Play original one
    # justPlay(fn)

    # Play modified one
    modified = negToZero(fn)
    play(modified)

# main_ex2()

# 3.
def changeVol(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    path = getMediaPath(fn)
    sound = makeSound(path)

    for s in getSamples(sound):
        v = getSampleValue(s)
        if v < 0:
            setSampleValue(s, int(v * 0.5))
        elif v * 2 > 32767:
            setSampleValue(s, 32767)
        else:
            setSampleValue(s, v * 2)

    return sound

def main_ex3():
    fn = "preamble.wav"

    # Play original one
    # justPlay(fn)

    modified = changeVol(fn)
    play(modified)

# main_ex3()

# 4.
def inReverse(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    path = getMediaPath(fn)
    sound = makeSound(path)

    length = getLength(sound)
    for i in range(length / 2):
        tmp = getSampleValueAt(sound, i)
        setSampleValueAt(sound, i, getSampleValueAt(sound, length - 1 - i))
        setSampleValueAt(sound, length - 1 - i, tmp)

    return sound

def main_ex4():
    fn = "airplane.wav"

    # Play original one
    # justPlay(fn)

    modified = inReverse(fn)
    play(modified)

# main_ex4()

# 5.
def merge(*args):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    sounds = [makeSound(getMediaPath(fn)) for fn in args]

    total_len = sum(map(getLength, sounds))
    result = makeEmptySound(total_len)
    i = 0
    for sound in sounds:
        for s in getSamples(sound):
            setSampleValueAt(result, i, getSampleValue(s))
            i += 1

    return result

def main_ex5():
    f1, f2, f3 = "computer.wav", "is.wav", "fun.wav"
    sound = merge(f1, f2, f3)
    play(sound)

main_ex5()
