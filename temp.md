def login_view(request,*args,**kwargs):
    form = LoginFrom(request.POST or None)
    username=request.POST.get("username")
    warning=''
    if len(str(username))<6:
        warning='Too short username\n用户名过短，请重新输入'
    data=LoginText.objects.filter(username=username)
    if data:
        for item in data:
            db_password=item.password
        if db_password==request.POST.get("pass"):
            print("login success")
        else:
            print("wrong password")
    else:
        print("user not exist")
    context={
        'form':form,
        'warning':warning

    }
    if request.method=='POST':
        print(request.POST)
    return render(request,"polls/login_a.html",context)
