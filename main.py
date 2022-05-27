import qrcode


def create_qr(data: str, file_name: str):
    qr = qrcode.QRCode(version=None, box_size=25, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="blue")
    img.save(file_name)


if __name__ == '__main__':
    file_name = 'sample_qr.png'
    create_qr('Script Candy', file_name)
