from django.shortcuts import render,redirect
from math import ceil
from srkapp.models import Jobs
from srkapp.models import UpdateProfile,Resume,Blog,Contact,Apply
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def home(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Jobs.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Jobs.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,'index.html',params)


def job(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Jobs.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Jobs.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,'job.html',params)



def apply(request):
    return render(request,'apply.html')

def applying(request):
    if request.method=="POST":
        username=request.POST.get('username')
        date=request.POST.get('date')
        email=request.POST.get('email')
        work=request.POST.get('work')
        expierence=request.POST.get('expierence')
        graduatedat=request.POST.get('graduatedat')
        Apply.date=date
        Apply.work=work
        Apply.expierence=expierence
        Apply.graduatedat=graduatedat
        apply=Apply(username=username,email=email,date=date,work=work,expierence=expierence,graduatedat=graduatedat)
        apply.save()
        messages.info(request,"Your application is applied successfully!.Please check your email for further information")
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
         
        email_client=mail.EmailMessage('Strawberry',f'Hello {username}\nGreetings of the day\n, Your application is applied successfully.We will get back to you after your application is verified',from_email,[email],connection=connection)
        connection.send_messages([email_client])
        connection.close()
        return redirect('/')
    return render(request,'index.html')   

def profile(request):

    current_user=request.user.username
    posts=UpdateProfile.objects.filter(username=current_user)
    context={"posts":posts}
    return render(request,'profile.html',context)

def about(request):
    return render(request,'about.html')
def blog(request):
    messages.info(request," For each user only one blog is allowed")
    if request.method=="POST":
        username1=request.user.username
        title=request.POST['title']
        blog=request.POST['blog']
        date=request.POST['date']
        Blog.title=title
        Blog.blog=blog
        Blog.date=date
        view_blog=Blog(username=username1,title=title,blog=blog,date=date)
        view_blog.save()
        messages.info(request," Blog is Updated to My Blogs page  successfully,Go and check once")
    return render(request,'blog.html')

def view_blog(request):
    messages.info(request," For each user only one blog is allowed")
    current_user=request.user.username
    jobs=Blog.objects.filter(username=current_user)
    context={"jobs":jobs}
    return render(request,'view_blog.html',context)

def resume(request):
    if request.method=="POST":
        username1=request.user.username
        fullname=request.POST['fullname']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        ssc=request.POST['ssc']
        inter=request.POST['inter']
        degree=request.POST['degree']
        Resume.fullname=fullname
        Resume.fathername=fathername
        Resume.mothername=mothername
        Resume.ssc=ssc
        Resume.inter=inter
        Resume.degree=degree
        
        resumee=Resume(username=username1,fullname=fullname,fathername=fathername,mothername=mothername,ssc=ssc,inter=inter,degree=degree)
        resumee.save()
        messages.info(request," Resume is Updated to database successfully,Don't update again which may lead to mismatch the data!")
    return render(request,'resume.html')

def resume1(request):

    return render(request,'resume1.html')


def resume2(request): 
    current_user=request.user.username
    resumes=Resume.objects.filter(username=current_user)
    context={"resumes":resumes}
   
    return render(request,'resume2.html',context)

def updateprofile(request):
    if request.method=="POST":
        username1=request.user.username
        email1=request.user.email
        mobile=request.POST['mobile']
        address1=request.POST['address1']
        address2=request.POST['address2']
        bio=request.POST['bio']
        dob=request.POST['dob']
        UpdateProfile.mobile=mobile
        UpdateProfile.address1=address1
        UpdateProfile.address2=address2
        UpdateProfile.bio=bio
        UpdateProfile.dob=dob
        
        user_profile=UpdateProfile(username=username1,email=email1,mobile=mobile,address1=address1,address2=address2,bio=bio,dob=dob)
        user_profile.save()
        all_members=UpdateProfile.objects.all()
        messages.info(request," Profile is Updated to database successfully!")
        return render(request,'profile.html')
        
    return render(request,'updateprofile.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        num=request.POST.get('num')
        desc=request.POST.get('desc')
        # print(name,email,numb,desc)
        query=Contact(name=name,email=email,num=num,desc=desc)
        query.save()
        from_email=settings.EMAIL_HOST_USER
        # Email starts here
        connection=mail.get_connection()
        connection.open()
        email_messge=mail.EmailMessage(f'Email from {name},'f'Subject : {num},'f'User Email : {email}\n,'f'Query : {desc}',from_email,['2100030510@kluniversity.in'],connection=connection)  
        email_client=mail.EmailMessage('Strawberry',f'Hello {name}\nGreetings of the day\n,Your 'f'Query:{num}\nThanks For Visiting Our site will get back you soon after your query is solved',from_email,[email],connection=connection)
        connection.send_messages([email_messge,email_client])
        connection.close()
        
         
      
        return redirect('/')

    return render(request,'index.html')


