from django.shortcuts import redirect, render,HttpResponse
from app1.models import Signup,Product
from django.contrib.auth.hashers import make_password 
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def hello (request):
    return HttpResponse("welcome to hello page")
def contact (request):
    return render(request,'contact.html')

def search_view(request):

    if request.method == 'GET':
        q = request.GET.get('search')
    else:
        q = None

    if q:
        res = Product.objects.all()
        res = Product.objects.filter(Q(name__icontains = q)| Q(des__icontains = q) | Q(price__icontains = q))
        data = res
    else:
        data = None

    return {'res':data,'ask':q}

def home (request):
    data = search_view(request)

    if 'name' in request.session.keys():
        user_name = request.session['name']
    else:
        user_name = None
    
    items = Product.objects.all()
    
    return render(request,'home.html',{'images':items ,"data":data})


def about (request):
    if 'name' in request.session.keys():
        user_name = request.session['name']
    else:
        user_name = None
    return render(request,'about.html')


def signup(request):

    if 'name' in request.session.keys():
        user_name = request.session['name']
    else:
        user_name = None

    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone = request.POST.get('user_phone')
        mail = request.POST.get('user_mail')
        # password = make_password(request.POST.get('user_password'),None,'md5')
        password = request.POST.get('user_password')

        signup_data = Signup(name=name,mail=mail,phone=phone,pswd=password)
        signup_data.save()
        
        
    return render(request,'signup.html')

def signin_view(request):
    if 'id' in request.session.keys() :
        
        messages.info(request, "you have already logged in !!")
        
        return redirect("/products/")
    else:

        if request.method == 'POST':
            try:
                
                mail = Signup.objects.get(mail = request.POST.get('user_email'))
            
                if mail.pswd == request.POST.get('user_password'):
                    request.session['id'] = mail.id
                    request.session['name'] = mail.name

                    return redirect("/products/")
                else:
                    return HttpResponse("wrong password")
            except:
                return HttpResponse("wrong email")
                

    return render(request,'signin.html')


def products(request):
    if 'id' not in request.session.keys():
        messages.info(request, "you have to login first!!")
        return redirect('/signin/')
    data = search_view(request)
    pro = Product.objects.all()

    # for paginantion
    pag_provider = Paginator(pro,3)
    page_number = request.GET.get('page')
    pro_final = pag_provider.get_page(page_number)

    if 'id' in request.session.keys():
        is_a_vendor = Signup.objects.get(id=request.session['id'])

    
    return render(request,'products_list_view.html',{'q':pro_final , 'data' : data, 'is_a_vendor': is_a_vendor.vendor})



def product_view(request,no):
    if 'id' not in request.session.keys():
        messages.info(request, "You have to login first!!")
        return redirect('/signin/')

       
    pro = Product.objects.get(id=no)
    return render(request,'product_view.html',{'q':pro})



def logout_view(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['vendor']
    except:
        pass    
    return redirect('/signin/')


def user_details_view(request):
    if 'id' in request.session.keys():
        try:
            user = Signup.objects.get(id = request.session['id'])
            return user
        except:
            pass
    return ""


def edit_product_view(request,no):
    pro = Product.objects.get(id=no)

    if request.method == "POST":
        p = Product.objects.get(id=no)

        name = request.POST['pname']
        price = request.POST['pprice']
        desc = request.POST['pdes']
        review = request.POST['preview']
        if request.FILES:
            image = request.FILES['pimage']
        else:
            image = None

        p.name = name
        p.price = price
        p.des = desc
        p.review = review
        if image == None or image == "":
            pass
        else:
            p.image = image
            

        p.save()
        messages.info(request,'Product updated succesfully!!')
        return render(request,'edit_product_page.html',{'pro':p})


    return render(request,'edit_product_page.html',{'pro':pro})


def add_product_view(request):
    if request.method == "POST":
        

        name = request.POST['pname']
        price = request.POST['pprice']
        desc = request.POST['pdes']
        review = request.POST['preview']
        if request.FILES:
            image = request.FILES['pimage']
        else:
            image = None
        
        p = Product(name=name, price=price, des = desc , review = review, image = image)    
        p.save()
        messages.info(request,'Product added succesfully!!')
        return render(request,'add_product_page.html')

    return render(request,'add_product_page.html')


def delete_product_view(request,no):
    pro = Product.objects.get(id=no)
    
    item = pro.delete()
    messages.info(request,'Product deleted succesfully!!')
    return redirect('products_url')      
         
    
