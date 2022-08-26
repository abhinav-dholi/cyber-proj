import os
import sys
import base64
from PIL import Image as Img
from Crypto.Cipher import AES
from PIL import ImageTk as ImgTk
from src.Encrypter import Encrypter
from src.Decrypter import Decrypter
from .ECC import ECC

def enc():
    with open("./src/image.jpg", "rb") as imageFile:
        value = base64.b64encode(imageFile.read())
        
    #myKey = "1234"
    aes_key = "57811460909138771071931939740208549692"
    ######################################################################################
    # Encrypt  AES_key with ECC public key
    ecc_obj_AESkey = ECC()
    private_key = 59450895769729158456103083586342075745962357150281762902433455229297926354304
    public_key = ecc_obj_AESkey.gen_pubKey(private_key)
    (C1_aesKey, C2_aesKey) = ecc_obj_AESkey.encryption(public_key, str(aes_key),isencrypted=True)
    x = Encrypter(value, aes_key)
    cipher = x.encrypt_image()
    fh = open("./src/cipher.txt", "wb")
    fh.write(cipher)
    fh.close()