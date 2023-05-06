# from django.shortcuts import render
# import mysql.connector as sql

# em=''
# pwd=''
# # Create your views here.
# def loginpage(request):
#     global em,pwd
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="#Akash@12",database='akash')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
            
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value
        
#         c="select * from users where email='{}' password='{}'".format(em,pwd)
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             return render(request,'error.html')
#         else:
#             return render(request,'welcome.html')
#         m.commit()

#     return render(request,'login.html')
                
# # Create your views here.
# #def loginpage(request):
from django.shortcuts import render
import mysql.connector as sql
from login.models import Contact
from django.contrib import messages
from datetime import datetime
em=''
pwd=''
# Create your views here.
def loginpage(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="#Akash@12",database='akash')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select *from users where Email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')

    return render(request,'login.html')
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
#def index(request):
   # return render(request,"index.html")
def home(request):
    return render(request,"home.html")
#def contact(request):
def contact(request):
    
    if request.method=='POST':
        
        
        #error=None
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your problem is submitted!")
    return render(request,"contact.html")    
    #return render(request,"contact.html")
    
