import urllib.request as rt

from bs4 import BeautifulSoup
import os.path as op
import re

def Dac(url):
    
    base=url.split(r'/')[-1].replace('?','')
   # base=url.split(r'/')[-1].split(r'?')[0]
    
    
    u=BeautifulSoup(rt.urlopen(url))

    
    no=0
    pt=re.compile(r'(\.jpg|\.png|\.gif|\.PNG)$')
   
    TagA=u.find_all('a',href=re.compile(pt))
    tot=len(TagA)

    #

    head={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
          'Accept-Encoding':'gzip'}
   
    for w in range(tot):
        
        i=TagA[w]
        #if re.search(pt,i.get('href')):
            
        no+=1
        print('downloading...',no)
        filename=base+'_'+str(no)+'.jpg'
        DlUrl=i.get('href')
        #filename=DlUrl.split(r'/')[-1]
        
        if op.exists(filename)and op.getsize(filename)>0:continue
        #with open(filename,'wb') as f:
            
        r=rt.Request(DlUrl,headers=head)
        with open(filename,'wb')as f:
            f.write(rt.urlopen(r).read())
         
           
                   
    print(base,'...ok')
    # next page
    return u.find('a',text='下一页').get('href')
    
    
    
def anals(url):
    u=BeautifulSoup(rt.urlopen(url))
    i=u.find("a",text="最后页")
    return(int(i.get('href').split('=')[-1]))

        
#Dac(input())

    
