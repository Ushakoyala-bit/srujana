import pyqrcode

s = "https://www.youtube.com/c/techdecode"

url = pyqrcode.create(s)

url.svg("qr.svg",scale = 7)