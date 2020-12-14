from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pizzashopapp.forms import PizzaShopForm,UserForm,UserFormForEdit,PizzaForm,ClientRoleForm,TestModelForm
from django.contrib.auth.models import User
from pizzashopapp.models import Pizza,ClentRole,TestModel


from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return redirect(pizzashop_home)

@login_required(login_url='/pizzashop/sign_in/')
def pizzashop_home(request):
    return  redirect(pizzashop_pizza)


def test_model(request):
    test = TestModel.objects.all()
    test_form = TestModelForm()

    if request.method=='POST':
        test_form = TestModelForm(request.POST)
        if test_form.is_valid():
            test_form.save()

    return render(request,'pizzashop/test.html',{'test':test,
                                                 'test_form':test_form})

def test_model_2(request,user_id):
    test = TestModel.objects.all()
    test_form = TestModelForm(instance=User.objects.get(id=user_id))
    user = User.objects.get(id=user_id)
    #role = TestModel.objects.filter(user=request.user.testuser)
    try:
        role = TestModel.objects.filter(user=user_id)
    except:
        print("An exception occurred")

    print(type(TestModel.objects.filter(user=user_id)))

    if request.method=='POST':
        test_form = TestModelForm(request.POST)
        if test_form.is_valid():
            test_form.save()

    return render(request,'pizzashop/test.html',{'user':user.get_full_name(),
                                                 'test_form':test_form})

def pizzashop_client_role(request,user_id):
    role = ClentRole.objects.all()
    role_form = ClientRoleForm(instance=User.objects.get(id=user_id))
    user = User.objects.get(id=user_id)

    if request.method=='POST':
        role_form = ClientRoleForm(request.POST,instance=User.objects.get(id=user_id))

        if role_form.is_valid():
            role_form.save()

    return render(request,'pizzashop/test.html',{'role':role
                                                 ,'role_form':role_form
                                                 ,'user':user})


def pizzashop_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    if request.method=='POST':
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST,request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)

            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request,authenticate(username= user_form.cleaned_data['username'],
                                       password= user_form.cleaned_data['password']))

            return redirect(pizzashop_home)


    return render(request, 'pizzashop/sign_up.html', {'user_form':user_form,
                                                      'pizzashop_form':pizzashop_form})


@login_required(login_url='/pizzashop/sign_in/')
def pizzashop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    pizzashop_form = PizzaShopForm(instance=request.user.pizzashop)

    if request.method=='POST':
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pizzashop_form = PizzaShopForm(request.POST,request.FILES,instance=request.user.pizzashop)


        if user_form.is_valid() and pizzashop_form.is_valid():
           user_form.save()
           pizzashop_form.save()

    return render(request,'pizzashop/account.html',{'user_form':user_form,
                                                    'pizzashop_form':pizzashop_form})

@login_required(login_url='/pizzashop/sign_in/')
def pizzashop_pizza(request):
    pizzas = Pizza.objects.filter(pizzashop=request.user.pizzashop).order_by("-id")

    return render(request,'pizzashop/pizza.html',{
        'pizzas': pizzas
    })

@login_required(login_url='/pizzashop/sign_in/')
def pizzashop_add_pizza(request):

    pizza_form = PizzaForm()

    if request.method=='POST':
        pizza_form = PizzaForm(request.POST, request.FILES)

        if pizza_form.is_valid():
            pizza = pizza_form.save(commit=False)
            pizza.pizzashop = request.user.pizzashop
            pizza.save()

            return redirect(pizzashop_pizza)

    return render(request,'pizzashop/add_pizza.html',{'pizza_form':pizza_form})

@login_required(login_url='/pizzashop/sign_in/')
def pizzashop_edit_pizza(request,pizza_id):
    pizza_form = PizzaForm(instance=Pizza.objects.get(id=pizza_id))

    if request.method=='POST':
        pizza_form = PizzaForm(request.POST,request.FILES,instance=Pizza.objects.get(id=pizza_id))

        if pizza_form.is_valid():
            pizza=pizza_form.save()
            return redirect(pizzashop_pizza)

    return render(request, 'pizzashop/edit_pizza.html',{
        'pizza_form':pizza_form
    })