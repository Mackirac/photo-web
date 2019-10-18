from PIL import Image

def to_bin (dec):
    if (0 <= dec and dec <= 255):
        bin = []
        for _ in range(8):
            bin.append(int(dec % 2))
            dec = int(dec / 2)
        return bin

def to_dec (bin):
    if (isinstance(bin, list) and len(bin) == 8):
        dec = 0
        for i in range(8): dec += bin[i] * pow(2, i)
        return dec
    print(isinstance(bin, list))

def hide_character (buffer, idx, character):
    if len(buffer) >= idx + 8:
        for b in to_bin(character):
            if (buffer[idx] % 2 != b):
                if (b == 1): buffer[idx] += 1
                else: buffer[idx] -= 1
            idx += 1
    return idx

def hide_message (image, text):
    data, idx = list(image.tobytes()), 0
    for c in bytes(text, 'utf8'): idx = hide_character(data, idx, c)
    hide_character(data, idx, 3)
    return Image.frombytes(image.mode, image.size, bytes(data))

def seek_character (image, idx):
    if len(image) < idx + 8: return 3, 0
    character = []
    for _ in range(8):
        character.append(image[idx] % 2)
        idx += 1
    return to_dec(character), idx

def seek_message (image):
    message, image = [], image.tobytes()
    character, idx = seek_character(image, 0)
    while character != 3:
        message.append(character)
        character, idx = seek_character(image, idx)
    try: return bytes(message).decode('utf8')
    except UnicodeDecodeError: return None
