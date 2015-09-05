
#for rendering template

from django.shortcuts import render
from django.shortcuts import render_to_response

#for using class based view

from django.views.generic import View
from django.views.generic import TemplateView

#for user authentication

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#for redirecting user from one view to another

from django.http import HttpResponseRedirect

#module for changing url into url that is used to redirect

from django.core.urlresolvers import reverse



from catalog.form import UserForm, CarForm, BrandForm, Car


# Create your views here.

class LoginView(TemplateView):

    template_name = 'home/login.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        #nabs the data from the form, mate
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate the chap that is trying to log in, mate
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))



        return render(request,self.template_name)

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get(self,request):
        return render(request,self.template_name)

class CarlotView(TemplateView):

    template_name = 'carlot.html'

    def get(self,request):
        return render(request,self.template_name)

class AboutView(TemplateView):

    template_name = 'about.html'

    def get(self,request):
        return render(request,self.template_name)

class FaqView(TemplateView):

    template_name = 'faq.html'

    def get(self,request):
        return render(request,self.template_name)


class DashboardView(TemplateView):

    template_name = 'home/dashboard.html'

    def get(self,request):
        return render(request,self.template_name,{'user': request.user})

class RegisterView(TemplateView):
    template_name =  'home/register.html'

    def get(self,request):
        form = UserForm()
        return render(request,self.template_name, {'register_form':form})

    def post(self,request):
        user = None
        form = UserForm(request.POST or None, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, self.template_name, {'form':form})

class ProfileView(TemplateView):

    template_name = 'home/profile.html'

    def get(self,request):
        return render(request,self.template_name)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))

class AddcarView(TemplateView):

    template_name = 'addcar.html'

    def get(self, request):
        form = CarForm(initial={'owner':request.user})

        return render(request,self.template_name, {'CarForm':form})

    def post(self, request):
        car = None
        form = CarForm(request.POST or None, instance=car)

        if form.is_valid():
            new_car = form.save(commit=False)
            new_car.save()
            return HttpResponseRedirect(reverse('cardetail',kwargs={"car_id":new_car.id}))
        else:
            return render(request,self.template_name,{'CarForm':CarForm})

class CardetailView(TemplateView):

    template_name = 'cardetail.html'
    car_id = None

    def get(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return HttpResponseRedirect(reverse('not-found'))

        return render(request,self.template_name,{'car':car})

class AddbrandView(TemplateView):

    template_name = 'addbrand.html'

    def get(self, request):
        form = BrandForm()
        return render(request,self.template_name,{'BrandForm':form})

    def post(self, request):
        new_brand = None
        form = BrandForm(request.POST or None, instance = new_brand)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,self.template_name,{'BrandForm':form})

class MycarsView(TemplateView):

    template_name = 'mycars.html'
    owner_id = None

    def get(self, request):
        my_cars = Car.objects.filter(owner_id=request.user.id)
        return render(request, self.template_name)





