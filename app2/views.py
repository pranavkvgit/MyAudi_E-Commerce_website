from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from app2.models import Reg,Login,addproduct,cart,order_child,order_master

from django.shortcuts import render, get_object_or_404,redirect

import datetime

# Create your views here.

def Home_pge(request):  
    template=loader.get_template("Home.html")
    context={}
    return HttpResponse(template.render(context,request))


def Login_Pge(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        if Login.objects.filter(uname=uname,pword=pwd):
            l=Login.objects.get(uname=uname,pword=pwd)
            if l.utype=="user":
                request.session["uid"]=l.uid_id
                return HttpResponse("<script>alert('welcome user');window.location='/user_page';</script>")
            elif l.utype=='admin':
                return HttpResponse("<script>alert('welcome admin');window.location='/admin_page';</script>")
            else:
                return HttpResponse("<script>alert('invalid user');window.location='/Login_page2';</script>")
        else:
            return HttpResponse("<script>alert('invalid user');window.location='/Login_page2';</script>")
            

    else:
        template=loader.get_template("Login_Page.html")
        context={}
        return HttpResponse(template.render(context,request))

def Register_pge(request):
    if request.method=='POST':
        r=Reg()
        r.name=request.POST.get('name')
        r.age=request.POST.get("age")
        r.gender=request.POST.get("gender")
        r.email=request.POST.get("email")
        r.addr=request.POST.get("address")
        r.phon=request.POST.get("mobile")
        r.loc=request.POST.get("location")
        r.save()
        id=Reg.objects.latest("id").id
        l=Login()
        l.uname=request.POST.get("username")
        l.pword=request.POST.get("password")
        l.utype='user'
        l.uid_id=id
        l.save()
        return HttpResponse("<script>alert('Registration Succussfully');window.location='/Registration_Form';</script>")

    else:
        template=loader.get_template("Registration_Page.html")
        context={}
        return HttpResponse(template.render(context,request))
    
    
def user_pge(request):
    template=loader.get_template("user_page.html")
    context={}
    return HttpResponse(template.render(context,request))

def admin_pge(request):
    template=loader.get_template("admin_page.html")
    context={}
    return HttpResponse(template.render(context,request))  



def product_pge(request):
    if request.method=='POST':
        p=addproduct()
        p.pname=request.POST.get('pname')
        p.price=request.POST.get("price")
        p.discription=request.POST.get("discription")
        p.category=request.POST.get("category")
        p.image=request.FILES['file']
        p.save()
        return HttpResponse("<script>alert('Product added');window.location='/product_page';</script>")

    else:
        template=loader.get_template("product_add_page.html")
        context={}
        return HttpResponse(template.render(context,request))
    
    
def viewproduct(request):
    u=addproduct.objects.all()
    template=loader.get_template("product_view_page.html")
    context={'products':u}
    return HttpResponse(template.render(context,request))


def product_details(request, sid):
    product = get_object_or_404(addproduct, id=sid)
    request.session["pid"]=sid
    if request.method == "POST":
        cart_item = cart.objects.filter(uid=request.user, pid=product).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            new_cart_item = cart(
                uid=request.user, 
                pid=product,
                pname=product.pname,
                price=product.price,
                category=product.category,
                discription=product.discription,
                image=product.image,
                quantity=1
            )
            new_cart_item.save()

        return redirect('view_cart') 

    context = {'product': product}
    return render(request, "product_details.html", context)




def add_to_cart(request):
    if request.method == 'POST':
        qty = request.POST.get("quantity")
        if qty is None or qty == '':
            qty = 1
        else:
            try:
                qty = int(qty)
            except ValueError:
                qty = 1  # If quantity is invalid, default to 1

        c = cart()
        c.date = datetime.datetime.now()
        c.quantity = qty
        c.uid_id = request.session.get("uid")  # Get user ID from session
        c.pid_id = request.session.get("pid")  # Get product ID from session

        try:
            product = addproduct.objects.get(id=c.pid_id)
            price = product.price if product.price is not None else 0
        except addproduct.DoesNotExist:
            price = 0 

        c.total = qty * price
        c.save()

        return HttpResponse("<script>alert('Item added to cart');window.location='/cart_page';</script>")

    return redirect('/cart_page')

             
        
        
def cart_page(request):
    if request.method=="POST":
        c=cart.objects.all()
        om=order_master()
        om.date=datetime.datetime.today()
        om.uid_id=request.session["uid"]
        om.gtotal=0
        om.save()
        id=order_master.objects.latest("id").id
        for i in c:
            oc=order_child()
            oc.pid_id=i.pid_id
            oc.qty=i.quantity
            oc.total=i.total
            oc.status='completed'
            oc.oid_id=id
            oc.save()
        c.delete()
        return HttpResponse("<script>alert('order placed successfully');window.location='/order_list';</script>")

    else:
        u=cart.objects.raw("select * from app2_cart,app2_addproduct where app2_addproduct.id=app2_cart.pid_id")
        gtotal = 0
        for item in u:
            gtotal += item.total if item.total is not None else 0
        template=loader.get_template("cart.html")
        context={'u':u,'total':gtotal}
        return HttpResponse(template.render(context,request))





def remove_item(request,id):
    c=cart.objects.get(id=id)
    c.delete()
    return HttpResponse("<script>alert('Item Removed');window.location='/cart_page';</script>")



def order_list(request):
    user_id = request.session.get('uid')
    d=order_master.objects.raw("select * from app2_order_child,app2_order_master,app2_addproduct where app2_addproduct.id=app2_order_child.pid_id and app2_order_child.oid_id=app2_order_master.id and app2_order_master.uid_id=%s",[user_id])
    context = {
        'orders': d,
    }
    return render(request, 'order_list.html', context)


def remove_from_cart(request, item_id):
    item = get_object_or_404(cart, id=item_id)
    item.delete()
    return redirect('orderlist')

def delete_order(request, order_child_id):
    if request.method == "POST":
        orderchild = get_object_or_404(order_child, id=order_child_id)
        orderchild.status = 'cancelled'
        orderchild.save()
        return HttpResponse("<script>alert('Order cancelled');window.location='/order_list';</script>")
    
    


