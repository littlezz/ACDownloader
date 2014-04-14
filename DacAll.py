

from Lib.Dacfast import Dac,anals
import pickle
import os



#define
Time=10
NumOfS=1

with open('url.txt',encoding='utf-8') as f:
    url=f.read().rstrip(r'/')


#print(BaseLink)

if (os.path.exists('jpg'))==False:
    os.makedirs('jpg')
os.chdir('jpg')

try:
    WantPg=max(int(input('how many pages do you want to download\n')),0)
except:
    print("输入纯数字")
    input()
else:
    if os.path.exists('save.pickle'):
        with open('save.pickle','rb') as f:
            save=pickle.load(f)
    else: save={'g':0}

    if save['g']:
        url=save['url']

    # save
   
    save['g']=1
    
    BaseLink=url.split(r'?')[0]
    old=url.split(r'?')[-1]
#    if url.find(r'?pn')>-1:
#        GetPg=int(url.split('=')[-1])
#    else: GetPg=1
   
    Tot=anals(url)
   
    for Pg in range(min(Tot,WantPg)):
        print(url)
        NextHref=Dac(url)
        if NextHref==old:break
        old=NextHref
        print('go')
        if (Pg%NumOfS==0):
            save['url']=url
           
            with open('save.pickle','wb') as f:
                
                pickle.dump(save,f)
            
        url=BaseLink+NextHref
        
        
 #   save['g']=0
 #   with open('save.pickle','wb') as f:
 #       pickle.dump(save,f)
    if os.path.exists('save.pickle'):os.remove('save.pickle')
    # del save.pickle
    print('all done!')
