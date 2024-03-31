def convert(message):
    replace_dict = {':)': '🙂', ':(': '🙁'}
    for old, new in replace_dict.items():
        message = message.replace(old, new)
    print(message)


def main():
    message = input()
    face_message = convert(message)
    return face_message


main()
