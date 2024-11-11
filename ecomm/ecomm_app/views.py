from django.shortcuts import render,HttpResponse,redirect
from ecomm_app.models import Msg

def home(request):
    return HttpResponse("Hello Linked SUccessfully....!")

def create(request):
    if request.method == 'POST':
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,message=msg)
        m.save()

        print(n,mail,mob,msg)
        # return HttpResponse("Data Inserted Successfully")
        return redirect('/dashboard')
    else:
        # return HttpResponse("I am in create section")
        print("request is:",request.method)
        return render(request,'create.html')
    
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    # return HttpResponse("Data fetched successfully")
    return render(request,'dashboard.html',context)

def delete(request,rid):
    # print("id to be deleted:",rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    # return HttpResponse("id:"+rid)
    return redirect('/dashboard')

def edit(request,rid):
    if request.method == 'POST':
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=mob,message=msg)
        return redirect('/dashboard')
    
    else:
        #display from with old data
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)

    # print("id to be edited",rid)
    # return HttpResponse("id:"+rid)