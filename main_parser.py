from bs4 import BeautifulSoup
import requests as req
from fake_useragent import UserAgent

resp = req.get("https://www.airfleets.net/listing/a321-43.htm", headers={'User-Agent': UserAgent().chrome})

soup = BeautifulSoup(resp.text, 'html.parser')
last_page = soup.find('a', attrs={'class': "page2"})

# print(soup)
page = last_page.text
num_page = page.split('/')
#print(num_page)
list_page = int(num_page[-1])
print(list_page)
count_plane = 0
for i in range(1,list_page+1):
    link = "https://www.airfleets.net/listing/a321-%s.htm" % (str(i))
    resp = req.get(link,  headers={'User-Agent': UserAgent().chrome})

    soup = BeautifulSoup(resp.text, 'html.parser')
    obj = soup.find('table', attrs={'class': "tab800"})
    # print(soup)
    a = obj.text
    b = a.split()

    f = []
    for i in range(len(b)):
        if b[i][0].isdigit() and b[i][1].isdigit() and (b[i][2].isdigit() or b[i][2] == '/') :
            # i+=1  :
            # i+=1
            f.append(b[i])
    #print(f)
    t=[]
    for i in range(len(f)):
        if '/' in f[i] or '-' in f[i]:
            t.append(f[i])
        else:
            continue
    #print(t)
    q=[]
    for i in range(len(t)):
        if t[i][-1].isalpha():
            #print(f[i])
            pass
        elif i != len(t) - 1:
            if '-' in t[i] and '/' in t[i+1]:
                q.append(t[i])
                q.append(t[i + 1])
    #print(q)


    count_planes = []
    for i in range(1,len(q)+1,2):
        if int(q[i][-4:]) >= 2012:
            count_planes.append(q[i - 1])
    #print((count_planes))
    print(len(count_planes))
    count_plane+=len(count_planes)

print(count_plane)

    # print(soup.tbody.text)
    # print(soup.title.parent)