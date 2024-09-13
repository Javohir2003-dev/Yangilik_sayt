from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import (NewsForm, CategoryForm, CommentForm, 
                    UserForm,UserEditForm, 
                    Comment,LoginForm
                    ,PasswordForm)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import News


def keraksiz(request):
   return render(request, 'keraksiz.html')


def home(request):
    
    if request.user.is_authenticated:
        hammasi=News.objects.all()
        cantext={'news':hammasi.order_by('-id')}

        if request.POST:
            news_id = request.POST['one']
            one_news = News.objects.get(id=news_id)

            if request.user in one_news.likes.all():

                one_news.likes.remove(request.user)
                
            else:

                one_news.likes.add(request.user)


        return render(request, 'home.html',cantext)
    return login_(request)
    
def CreateCategory(request):
    form = CategoryForm()

    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'create_category.html', {'form': form})


def user_register(request):
    form = UserForm()
    print(form)

    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
         user = form.save()
         parol = form.cleaned_data['password']
         user.set_password(parol)
         user.save()
        return redirect('Login')
    return render(request, 'register.html', {'form': form})    


def user_edit(request):    
   form = UserEditForm(instance=request.user)
   if request.POST:            
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
         
            return redirect('home')
   return render(request, 'user_edit.html', {'form': form})


def password_edit(request):
    form = PasswordForm()
    if request.POST:
        form = PasswordForm(request.POST)
        p_1 = form.data['eski_password']
        p_2 = form.data['yangi_password']
        user = request.user
        if user.check_password(p_1):
            user.set_password(p_2)
            user.save()
            return redirect('home')
        
    return render(request, 'pasword_edit.html', {'form': form})


def createnews(request):
    if request.user.is_authenticated:
        form = NewsForm()

        if request.POST:
            form = NewsForm()
            if request.POST:
                form=NewsForm(request.POST,files=request.FILES)
            if form.is_valid():
                News.objects.create(
                    author = request.user,
                    title = form.cleaned_data['title'],
                    text = form.cleaned_data['text'],
                    tur = form.cleaned_data['tur'],
                    rasm = form.cleaned_data['rasm']
                    )
            return redirect('home')
        return render(request, 'create_news.html', {'form': form}) 
    return login_(request)

def detail(request, id):

    a = News.objects.get(id = id)
    
    a.views += 100
    a.save()
    form=CommentForm()
    if request.POST:
      form=CommentForm(request.POST)
      if form.is_valid():
        Comment.objects.create(
            izoh=form.cleaned_data['izoh'],
            user=request.user,
            news=a
            )
        return redirect('detail',a.id)
    return render(request, 'detail.html', {'one': a, 'form':form})


def delete(request, id):
    b = News.objects.get(id=id)
    b.delete()

    return redirect('home')


def delete_comment(request, id, one):
    # news = News.objects.get(id=id)
    
	comment = Comment.objects.get(id=id)
	comment.delete()

	return redirect('detail', one)


def createComment(request, id): 
   news = News.objects.get(id=id)
   form = CommentForm()

   if request.POST:
      form = CommentForm(request.POST)
      if form.is_valid():
         Comment.objects.create(
             izoh = form.cleaned_data['izoh'],
             user = request.user,
             news = news 
            )
         return redirect('detail', news.id)
   return render(request, 'detail.html', {'form': form})


def edit(request,id):
   
    tahrirlash = News.objects.get(id=id)
    form = NewsForm(instance=tahrirlash)
    if request.method =='POST':
      form = NewsForm(request.POST, files=request.FILES, instance=tahrirlash)


    if form.is_valid():
            tahrirlash.title = form.cleaned_data['title']
            tahrirlash.text = form.cleaned_data['text']
            tahrirlash.tur = form.cleaned_data['tur']
            tahrirlash.rasm = form.cleaned_data['rasm']
      
            tahrirlash.save()
            return redirect('home')
    return render(request, 'tahrirlash.html',{'form':form})


def login_(request):
    login_form = LoginForm()
    if request.POST:
        login_form = LoginForm(request.POST)
    
        if login_form.is_valid():
           username = login_form.cleaned_data['username']
           password = login_form.cleaned_data['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:            
            login(request, user)    
            messages.success(request, f"Siz , {user.username}, login qilindingiz !")

            return redirect('home')
    # print(login_form)
    return render(request, 'login.html', {'form': login_form})


def Logout(request):
    logout(request)
    messages.info(request, 'Siz muvaffaqiyatli log out bo\'ldingiz !')
    return redirect('home')



def yordam(request):
    ...
    
    return render(request, 'yordam.html')


