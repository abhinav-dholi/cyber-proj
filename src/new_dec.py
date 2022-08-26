import os
import io
import sys
import base64
from PIL import Image as Img
from Crypto.Cipher import AES
from PIL import ImageTk as ImgTk
from src.Encrypter import Encrypter
from src.Decrypter import Decrypter
from .ECC import ECC
from .enc_keys import C1_aesKey,C2_aesKey

def dec():
    #myKey = "1234"
    aes_key = "57811460909138771071931939740208549692"
    private_key = 59450895769729158456103083586342075745962357150281762902433455229297926354304
    ecc_AESkey = ECC()
    decryptedAESkey = ecc_AESkey.decryption(C1_aesKey, C2_aesKey, private_key,is_dec=True)
    file  = "./src/encrypted.txt"
    text=open(file).read()
    cipher= text.encode('utf-8')
    x = Decrypter(cipher)
    image=x.decrypt_image(aes_key)
    print(type(image))
    imag = Img.open(io.BytesIO(image))
    imag.save('./src/decryptedimage.png')