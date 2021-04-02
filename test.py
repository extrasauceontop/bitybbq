import requests

session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "Trailers",
}

session.get("https://www.citybbq.com/locations/?zip=27560", headers=headers)

response = session.post("https://www.citybbq.com/wp-content/themes/city-bbq/api/get-closest-locations.php?lat=35.88&lng=-78.79&LtHuECgeIQ=C*vzLiD&TwxREKLOyMvt=QSP4Y3r0T]@&sPhClLYka=uGrEZVd&msX-IdWfKch=qBC1X.Fbp[8", headers=headers).text


with open("file.txt", "w", encoding="utf-8") as output:
    print(response, file=output)