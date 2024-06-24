from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import AddComputer, AddCyberUser

@login_required(login_url='/')
def BASE(request):
    return render(request, 'base.html')

@login_required(login_url='/')
def INDEX(request):
    computer_count = AddComputer.objects.all().count()
    user_count = AddCyberUser.objects.all().count()
    context = {
        'computer_count': computer_count,
        'user_count': user_count,
    }
    return render(request, 'main/index.html', context)

@login_required(login_url='/')
def Add_Computer(request):
    if request.method == "POST":
        compname = request.POST.get('compname')
        comploc = request.POST.get('comploc')
        idadd = request.POST.get('idadd')
        
        computer = AddComputer(compname=compname, comploc=comploc, idadd=idadd)
        computer.save()
        
        messages.success(request, "Computer details have been saved")
        return redirect('add_computer')  # Redirect to the same page after form submission
    
    return render(request, 'main/add-computer.html')

@login_required(login_url='/')
def MANAGE_Computer(request):
    computers = AddComputer.objects.all()
    context = {'computers': computers}
    return render(request, 'main/manage-computer.html', context)

@login_required(login_url='/')
def DELETE_Computer(request, id):
    computer = get_object_or_404(AddComputer, id=id)
    computer.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('manage_computer')

@login_required(login_url='/')
def UPDATE_Computer(request, id):
    computer = get_object_or_404(AddComputer, id=id)
    context = {
        'computer': computer,
    }
    return render(request, 'main/update-computer.html', context)

@login_required(login_url='/')
def UPDATE_COMPUTER_DETAILS(request):
    if request.method == 'POST':
        computer_id = request.POST.get('computer_id')
        compname = request.POST.get('compname')
        comploc = request.POST.get('comploc')
        idadd = request.POST.get('idadd')

        computer = get_object_or_404(AddComputer, id=computer_id)
        computer.compname = compname
        computer.comploc = comploc
        computer.idadd = idadd
        computer.save()

        messages.success(request, "Computer details have been updated successfully")
        return redirect('manage_computer')

    return render(request, 'main/update-computer.html')


@login_required(login_url = '/')
def Add_User(request):
    computer = AddComputer.objects.all()
    if request.method == "POST":
       
            name = request.POST.get('name')
            address = request.POST.get('address')
            mobilenumber = request.POST.get('mobilenumber')
            email = request.POST.get('email')
            idproof = request.POST.get('idproof')
            computeruse_id = request.POST.get('computeruse_id')
            entryid = request.POST.get('entryid')
            
             
            if  AddCyberUser.objects.filter(entryid=entryid).exists():
                
                messages.success(request,"This entry id is already exist")
                return redirect('add_user')
                
            else:
                computer =AddComputer.objects.get(id=computeruse_id)
                userdetail = AddCyberUser(name = name,
            address = address,            
            mobilenumber = mobilenumber,
            email=email,
            idproof=idproof,
            
            entryid=entryid,
            computeruse_id=computer.id
            )
            
                           
            userdetail.save()
            

            messages.success(request,"User details has been saved")
            return redirect('add_user')

    context = {'computers':computer}
     
    return render(request, 'main/add-cyber-user.html',context)



@login_required(login_url='/')
def MANAGE_User(request):
    cyber_users = AddCyberUser.objects.all()
    context = {'cyber_users': cyber_users}
    return render(request, 'main/manage-cyber-user.html', context)

@login_required(login_url='/')
def DELETE_User(request, id):
    user = get_object_or_404(AddCyberUser, id=id)
    
    if request.method == "POST":
        user.delete()
        messages.success(request, 'User record deleted successfully!')
        return redirect('manage_user')
    
    context = {'user': user}
    return render(request, 'main/manage-cyber-user.html', context)

@login_required(login_url='/')
def UPDATE_USER(request, id):
    user = get_object_or_404(AddCyberUser, id=id)
    computers = AddComputer.objects.all()

    if request.method == "POST":
        try:
            user.name = request.POST.get('name')
            user.address = request.POST.get('address')
            user.mobilenumber = request.POST.get('mobilenumber')
            user.email = request.POST.get('email')
            user.idproof = request.POST.get('idproof')
            user.computeruse_id = request.POST.get('computeruse_id')
            user.remark = request.POST.get('remark')
            user.status = request.POST.get('status')          
            fees = request.POST.get('fees', 0)  
            print(fees)
            user.fees = int(fees)  
            user.save()
            messages.success(request, 'User details updated successfully!')
            return redirect('manage_user')
        except Exception as e:
            messages.error(request, f"Error updating user: {e}")
            return redirect('update_user', id=id)

    context = {'user': user, 'computers': computers}
    return render(request, 'main/update-cyber-user.html', context)



@login_required(login_url='/')
def Manage_Old_USER(request):
    cyber_users = AddCyberUser.objects.all()
    print("Fetched cyber_users:", cyber_users)
    for user in cyber_users:
        print(f"User: {user.name}, Status: {user.status}")
    context = {'cyber_users': cyber_users}
    return render(request, 'main/manage-cyber-old_user.html', context)



@login_required(login_url='/')
def VIEW_Old_USER(request, id):
    user = get_object_or_404(AddCyberUser, id=id)
    context = {'user': user}
    return render(request, 'main/view-user_details.html', context)


@login_required(login_url='/')
def Search(request):
    query = request.GET.get('query', '')
    cyberusers = []
    if query:
        cyberusers = AddCyberUser.objects.filter(entryid__icontains=query)
        if cyberusers.exists():
            messages.success(request, "Search results for: " + query)
        else:
            messages.warning(request, "No results found for: " + query)
    return render(request, 'main/search.html', {'cyberusers': cyberusers})

@login_required(login_url='/')
def Between_Date_Report(request):
    if request.method == "POST":
        fdate = request.POST.get('fdate')
        todate = request.POST.get('todate')
        searchresult = AddCyberUser.objects.filter(created_at__gte=fdate, created_at__lte=todate)
        messages.success(request, "Search data from " + fdate + " to " + todate)
        return render(request, 'main/between-date.html', {"data": searchresult})
    return render(request, 'main/between-date.html', {})

@login_required(login_url='/')
def TotalUser(request):
    cyber_users = AddCyberUser.objects.all()
    context = {'cyber_users': cyber_users}
    return render(request, 'main/total-users.html', context)
