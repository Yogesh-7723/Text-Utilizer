from django.shortcuts import render 
from django.http import HttpResponse 

def index(request):
    return render(request,"index.html")

def Analyze(request):
    text = request.POST.get('text' , 'default')
    terms = request.POST.get('punc','off')
    capital = request.POST.get('capital','off')
    count = request.POST.get('count','off')
    remove_line = request.POST.get('removeline','off')
    punctuations = '''!()-[]{};;'"\,<>./?@#$%^&*_~'''
    analyzed_text = ''
    
    
    if terms == 'on' and capital == 'on' and count == 'on' :
        c=0
        for index,i in enumerate(text):
            if text[index]==' ' or text[index]=='\n':
                continue
            else: 
                c+=1
        for index,i in enumerate(text):
            if text[index]==' ' and text[index+1]==' ':
                continue
            else: 
                analyzed_text += i
        text = analyzed_text
        analyzed_text=''
        for i in text:
            new = ''
            if i in punctuations:
               continue 
            else:
               analyzed_text += i
        analyzed_text = analyzed_text.upper()
        result ={'purpose':'Remove Punctualation an Capitalize it.','analyzed_text':analyzed_text,'text':text,'c':c}
        return render(request,'capfirst.html',result) 
    
    
    elif terms == 'on':
        for i in text:
            if i in punctuations:
               continue 
            else:
               analyzed_text+=i 
            
        result ={'purpose':'Remove Punctualation','analyzed_text':analyzed_text,'text':text}
        return render(request,'capfirst.html',result) 
    
    
    elif count == 'on':
        c = 0
        for index,i in enumerate(text):
            if text[index]==' ' or text[index]=='\n':
                continue
            else: 
                c+=1
            
        result ={'purpose':'Count number of Charactor','analyzed_text':c,'text':text}
        return render(request,'capfirst.html',result)
    
    
    elif remove_line == 'on':
        for index,i in enumerate(text):
            if text[index]==' ' and text[index+1]==' ':
                continue
            else: 
                analyzed_text += i
        result ={'purpose':'Count number of Charactor','analyzed_text':analyzed_text,'text':text}
        return render(request,'capfirst.html',result)
    
     
    elif capital == 'on':
        analyzed_tex = text.upper()
        result ={'purpose':'Capitalize text','analyzed_text':analyzed_tex,'text':text}
        return render(request,'capfirst.html',result)
      
    else:
        result = "Please Select any option"
        return render(request,'capfirst.html',result)
        
        

