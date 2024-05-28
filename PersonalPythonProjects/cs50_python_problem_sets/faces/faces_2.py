def main():
    message = input()
    face_message = convert(message)
    print(face_message)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace (":(", "🙁")
    return message


main()
