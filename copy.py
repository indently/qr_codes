import qrcode


def create_qr(data: str, file_name: str):
    qr = qrcode.QRCode(version=None, box_size=10, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="blue")
    img.save(file_name)


def main():
    file_name = 'test_qr.png'
    user_input = input('Write something: ')

    create_qr(user_input, file_name)


if __name__ == '__main__':
    main()
