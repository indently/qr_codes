import qrcode
import cv2


def create_qr(data: str, file_name: str):
    qr = qrcode.QRCode(version=None, box_size=10, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


def test_qr(image: str):
    qr_code = cv2.imread(image)
    detector = cv2.QRCodeDetector()

    # Detect
    detect = detector.detectAndDecode(qr_code)
    print('QR Code says:', detect[0])


def main():
    file_name = 'test_qr.png'
    user_input = input('Write something: ')

    create_qr(user_input, file_name)
    test_qr(file_name)


if __name__ == '__main__':
    main()
