from django.shortcuts import render
from django.views import View
from requests import request
from .forms import admin_form
from .models import admin_post , comments,Information
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from .forms import signup_form , user_logedin_form
from django.contrib.auth import authenticate,login,logout
# Create your views here.



class home_page(View):

    templates_name = 'home.html'
    def get(  self , request ):
        if request.user.is_authenticated:
            data = admin_post.objects.all()

            return render(request , self.templates_name , {'data' : data})
        else:

            return HttpResponseRedirect('/login/')

class save_comments(View):
    template_name = 'home.html'
    def post(self, request , id ):
        data = admin_post.objects.all()
        comment = request.POST['comments']
        print(comment)
        current_user = request.user
        print(current_user)
        print(id)
        send_data_to_database = comments(user = current_user , user_id = id , message = comment)
        send_data_to_database.save()
        return render(request , self.template_name , {'data' : data})


class Information_view(View):

    template_name = 'information.html'
    def get(self,request):
        if request.user.is_authenticated:
            titel = request.GET.get('title')
            date = request.GET.get('date')
            if titel and date is not None:
                Information.objects.create(title = titel ,date = date)
            data = Information.objects.all().order_by('-id')
            return render(request, self.template_name,{'data': data})
        else:
            return  HttpResponseRedirect('/login/')
class show_comments(View):
    templates_name = 'show_comments.html'
    def get(self, request , id ):
        data  = comments.objects.filter(user_id = id )
        single_data = admin_post.objects.get(pk = id)
        
        return render(request , self.templates_name , {'data':data , 'data1':single_data})

class upload_post(View):
    templates_name = 'upload_post.html'

    def get(self , request):
        if request.user.is_superuser:
            
            form = admin_form()
        else:
            messages.success(request,'Only admin can upload posts')
            return HttpResponseRedirect('/')

        return render(request , self.templates_name , {'form' : form})
    def post(self , request):
        print('this is post request')
        form = admin_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Uploded")
            return HttpResponseRedirect('/')
            
        return render(request , self.templates_name , {'form' : form})


def edit_post(request , id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            edit_id = admin_post.objects.get(pk = id )
            form=admin_form(request.POST,instance=edit_id)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            edit_id=admin_post.objects.get(pk=id)
            form=admin_form(instance=edit_id)
        return render(request , "edit.html" , {'form' : form})
    else:
        return HttpResponseRedirect('/login/')

class delete_post(View):
    def get(self,request,id):
            data1=admin_post.objects.get(id=id)
            data1.delete()
            return HttpResponseRedirect('/')



class sighup_form(View):
    templates_name = 'sign_up.html'

    def get (self ,request):
        form = signup_form()
        return render(request , self.templates_name , {'form' : form})

    def post(self , request):

        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'Congratulations !! you are a user of our website ')
            group=Group.objects.get(name='user_group')
            user.groups.add(group)
            return HttpResponseRedirect('/')
            
        return render(request , self.templates_name , {'form' : form})



class login_form(View):
    templates_name = "login.html"

    def get(self , request):
        form = user_logedin_form ()
        return render(request , self.templates_name , {'form' : form })


    def post(self , request) :
        form = user_logedin_form(request=request,data=request.POST)
        if form.is_valid():
                username_of_user=form.cleaned_data['username']
                password_of_user=form.cleaned_data['password']
                print(username_of_user)
                print(password_of_user)
                user=authenticate(username=username_of_user,password=password_of_user)
                if user is not None:
                    request.session['username'] = username_of_user
                    return HttpResponseRedirect('/otp_page/')
                    # login(request,user)
                    # return HttpResponseRedirect('/')
        return render(request , self.templates_name , {'form' : form })


class user_logout(View):
    def get(self , request ):
            
        logout(request)
        return HttpResponseRedirect ('/')



def Delete_information(request,id):
    print(id)
    try :
        Information.objects.get(pk = id).delete()
    except Information.DoesNotExist as error:
        print(error)

    return HttpResponseRedirect('/information/')

class Otp_page(View):
    template_name = 'otp_page.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        code = "mona12345"
        otp = request.POST['password']
        if code == otp:
            username = request.session['username']
            user=authenticate(username=username,password='admin')
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else :
                return HttpResponseRedirect('/login/')
        else :
            return HttpResponseRedirect('/login/')