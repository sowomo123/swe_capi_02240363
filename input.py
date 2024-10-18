import re
#imported the textfile using our last 3 digit code
url = 'https://csf101-server-cap1.onrender.com/get/input/363'
txt_file = re.get(url)
#converting the textfile into txt.file
with open('363.txt', 'wb') as file:
    data = file.write(txt_file.content)

print("Download 363.txt")
