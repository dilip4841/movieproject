from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies,LoginForm,Purchases
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def index(request):
    telugu_movies = Movies.objects.filter(language='Telugu')[:5]
    hindi_movies = Movies.objects.filter(language='Hindi')[:5]
    english_movies = Movies.objects.filter(language='English')[:5]
    tamil_movies = Movies.objects.filter(language='Tamil')[:5]
    return render(request,'home.html', {'telugu_movies': telugu_movies,
                  'hindi_movies':hindi_movies,
                  'english_movies': english_movies,
                  'tamil_movies': tamil_movies})


def dispaly_genre(request,language):
    movie_list = Movies.objects.filter(language=language)
    page = request.GET.get('page', 1)
    paginator = Paginator(movie_list,3)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = Paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)


    return render(request,'genres.html', {'movies': movies})

def display_movieinfo(request,mid):
    if request.session.get('id'):
        try:
            user = Purchases.objects.get(user=request.session.get('id'))
            if user:
                 movie = Movies.objects.get(movie_id = mid )
                 return render(request, 'single.html',{'movie': movie})
            else:
                return render(request, 'paymentgateway.html')
        except:
            return render(request, 'paymentgateway.html')

def login_form(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        LoginForm(user=Username,
                  password=Password,
                  mail=Email,
                  phone=Phone).save()
        return redirect('home_page')


def login(request):
    if request.method == 'POST':
        try:
            user = LoginForm.objects.get(mail=request.POST['email'],password = request.POST['password'])
            print('user= ',user)
            request.session['username']=user.user
            request.session['email']=user.mail
            request.session['id']=user.id
            return redirect('home_page')
        except LoginForm.DoesNotExist as e:
            return HttpResponse('invalid credinatls')
    return redirect('home_page')


def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('home_page')
    return redirect('home_page')



