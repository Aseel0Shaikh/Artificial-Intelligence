import requests

url = requests.get("http://localhost/view.php")
htmltext = url.text
print(htmltext)