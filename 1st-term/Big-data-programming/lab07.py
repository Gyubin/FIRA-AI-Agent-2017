# 1.
def blend_sounds(*args):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    sounds = [makeSound(getMediaPath(fn)) for fn in args]

    total_len = getLength(sounds[0])
    for i in range(1, len(args)):
        total_len += getLength(sounds[i]) / 2

    result = makeEmptySound(total_len)
    prev_index = 0
    for i in range(len(args)):
        if i == 0:
            for idx, s in enumerate(getSamples(sounds[i])):
                setSampleValueAt(result, idx, getSampleValue(s))
            prev_index = idx
        else:
            idx = prev_index - getLength(sounds[i]) / 2 - 1
            for s in getSamples(sounds[i]):
                prev_value = getSampleValueAt(result, idx)
                add_value = getSampleValue(s)
                setSampleValueAt(result, idx, prev_value + add_value)
                idx += 1
            prev_index = idx

    return result

def main_ex1():
    f1, f2, f3 = "bassoon-c4.wav", "bassoon-e4.wav", "bassoon-g4.wav"
    blended = blend_sounds(f1, f2, f3)
    play(blended)

# main_ex1()

# 2.
def get_single_cycle(max_amp, rate_per_freq, step):
    sound = makeEmptySound(rate_per_freq)
    for i, s in enumerate(getSamples(sound)):
        if i < rate_per_freq / 2:
            setSampleValue(s, step * i * -1)
        else:
            setSampleValue(s, getSampleValueAt(sound, i - 1) + step)

    return sound

def triangle_wave(freq, max_amp, sec):
    sound = makeEmptySoundBySeconds(sec)
    rate_per_freq = getLength(sound) / freq
    step = (2 * max_amp) / rate_per_freq

    single_cycle = get_single_cycle(max_amp, rate_per_freq, step)

    i = 0
    while i < getLength(sound):
        for s in getSamples(single_cycle):
            setSampleValueAt(sound, i, getSampleValue(s))
            i += 1
            if i >= getLength(sound):
                break

    return sound

def main_ex2():
    explore(triangle_wave(60, 4000, 3))

# main_ex2()

# 3.
def first_half_double(source):
    length = getLength(source) / 4 + 1
    target = makeEmptySound(length)
    targetIndex = 0
    for sourceIndex in range(0, getLength(source) / 2, 2):
        value = getSampleValueAt(source, sourceIndex)
        setSampleValueAt(target, targetIndex, value)
        targetIndex = targetIndex + 1
    return target

def hiphop_dj(fn):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    sound = makeSound(getMediaPath(fn))
    result = makeEmptySound(int(getLength(sound) * 1.5))

    length = getLength(result)
    doubled = first_half_double(sound)
    for i in range(0, length / 6):
        setSampleValueAt(result, i, getSampleValueAt(doubled, i))
    for x, i in enumerate(range(length / 6 + 1, length / 3)):
        setSampleValueAt(result, i, getSampleValueAt(doubled, length / 6 - x))
    for x, i in enumerate(range(length / 3 + 1, length)):
        setSampleValueAt(result, i, getSampleValueAt(sound, x))

    return result

def main_ex3():
    sound = hiphop_dj('backpack.wav')
    play(sound)

# main_ex3()

# 4.
def decode_sound(f1, f2):
    setMediaPath("/Users/qbinson/Downloads/FIRA_JES/mediasources-4ed")
    s1 = makeSound(getMediaPath(f1))
    s2 = makeSound(getMediaPath(f2))

    result = ""
    for i in range(getLength(s1)):
        tmp = getSampleValueAt(s1, i) ^ getSampleValueAt(s2, i)
        if tmp != 0:
            result += chr(tmp)

    return result

def main_ex4():
    f1, f2 = 'steg.wav', 'c4.wav'
    result = decode_sound(f1, f2)
    print("result:", result)

main_ex4()
