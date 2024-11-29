# from decouple import config
from outline_vpn.outline_vpn import OutlineVPN


# api_url = config("API_URL")
# cert_sha256 = config("CERT_SHA")
api_url = "https://92.38.241.233:33369/eGm6CkCA6HP6M02h90Pi4Q"
cert_sha256 = "49BA1DE527294356267D2E93E05A204CBBD76A0C30D185CC95C231FF9D1EE820"

client = OutlineVPN(api_url=api_url, cert_sha256=cert_sha256)

