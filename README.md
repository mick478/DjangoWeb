"# DjangoWeb" 

SUMMARY

       1.create project
       2.create app
       3.create html and connect to app
       4.create css and img then connect to app

BUILDING THE DJANGO PROJECT ##you could skip the step 1 and 5

       step.1 github add new repository

       step.2 add new project file

              dos:
              cd "project file"
              python -m venv "project name"

       step.3 start venv&install django

              dos:
              "project name"\script\activate.bat
              pip install django==2.0.7

       step.4 start django project

              dos:
              django-admin startproject "src(filename to put your code)"
              cd "src(filename to put code)"
              python manage.py runserver

       THE WEB IS WORKING NOW.(CTRL+Fn+B TO END)

       step.5 update to github

              dos:
              echo "Title" >> README.md                                      ##create readme file
              git init                                                       ##start git process
              git status                                                     ##check file status
              git add "file name"                                            ##include the files
              git commit -m "first commit"                                   ##commit
              git remote add origin "https://github.com/mick478/test.git"    ##connect respostory address
              git remote rm origin                                           ##clean
              git push -u origin master                                      ##update project
              
              
              git pull origin master --allow-unrelated-histories             ##if you created the README.md when you added the repository
              git pull                                                       ##when erro for push try pull then push again
                                                                             sometimes the datas donnot match eachother 
              
ADD APP IN THE PROJECT

       step.1 open the IED whatever you wnat and open project
       
       step.2 open terminal screem and type ## also you can runserver here by "python manage.py runserver"
              
              python manage.py startapp "name of app"
              
       step.3 add your app in the setting
              
              find the INSTALLED_APPS in setting.py and add your name of app

FIRST VIEW IN DJANGO
       
       Basic  if create templates below app skip this parts.
              step.1 create Template ## for frontend

                     add new directory below src
                     add new HTML file in template(base, page1, page2...etc)
                     add "TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')" in the setting.py ## create the path
                     of template (BASE_DIR='C:\Users\'USER'\PycharmProjects\DjangoWeb') so TEMPLATE_DIR='C:\Users
                     \'USER'\PycharmProjects\DjangoWeb\template'  if you create the name of directory is tmp the 
                     code must be "TEMPLATE_DIR = os.path.join(BASE_DIR, 'tmp')"

              step.2 add the adress to django
                     add TEMPLATE_DIR, to 'DIRS': [], which in setting.py\TEMPLATE
       A.
              step.1 connect your views with html
                     type in views
                     def homepage_view (request):
                            return render(request, 'base.html')
              step.2 connect your views with urls
                     type in urls
                     from my_app import views
                     urlpatterns = [
                         path('admin/', admin.site.urls),
                         path('', views.homepage_view, name='home'),       ##add this one  **name is for calling in html EX:action="{% url 'home' %}"
                     ]
       B.
              step.1 create Template ## for frontend       
                     add new directory below src
                     add new HTML file in template(base, page1, page2...etc)
                     add new python files below app. name "urls"              
              step.2 connect urls between app and src
                     type in urls of app(copy from urls of src)
                     from django.urls path
                     from . import views                        ##add this to connect all files in list

                     urlpatterns = [
                         #path('admin/', admin.site.urls),
                     ]
                     
                     type in urls of srcs
                     from django.urls import path , include    ##add include
                     urlpatterns = [
                         path('admin/', admin.site.urls),
                         path('user/', include('user.urls'))   ##connect urls from app"named user"
                     ]
              step.3 connect your views with html
                     type in views
                     def homepage_view (request):
                            return render(request, 'base.html')

CONNECT HTML WITH CSS AND IMG
       
       step.1 
              create diretory below project "static"
              create diretort "css" and "img" below static
              type STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) in setting
              then the html will connect by
              <% load static %>
              <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css">
              <img src="{% static 'img/test.jpg'%}">
              update css must "python manage.py collectstatic"
                            
       other 
              also can create diretory below app then don't need to setting django will search byself
              when you have different apps then you need collect all static by share to each other app
              setting.py  STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
              "python manage.py collectstatic" will collect all 
       

              
          
