import qrcode


def generate_qr(uuid : str, path : str):
    
    qr=qrcode.make(uuid)
    qr.save(path)
    