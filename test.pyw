
import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts.ics"
redirect="127.0.0.1"
website_list=["www.instagram.com","www.facebook.com","www.csgo.com"]
with open(hosts_path,'r') as file:
    content_file=file.read()
    file.close()
while 1:
    if (dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,22)) :
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'w') as file:
            file.write(content_file)
            file.close()
