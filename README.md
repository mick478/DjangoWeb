"# DjangoWeb" 

Django----src                      
              --setting
              --urls                    
              --wsgi
        --app                      
              --migrations
              --admin
              --apps
              --models
              --views
        --template
              --html
        --static
              --css
              --img

1.BUILD DJANGO PROJECT
2.ADD APP IN PROJECT
3.ADD TEMPLATE IN PROJECT
4.ADD STATIC IN PROJECT


BUILDING THE DJANGO PROJECT ##you could skip the step 1 and 5

       step.1 github add new repository

       step.2 add new project file

              dos:
              cd "project file"
              python -m venv "project name"

       step.3 start venv&install djangDJo

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

       step.1 create Template ## for frontend
              
              add new directory below src
              add new HTML file in template(base, page1, page2...etc)
              add "TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')" in the setting.py ## create the path
              of template (BASE_DIR='C:\Users\'USER'\PycharmProjects\DjangoWeb') so TEMPLATE_DIR='C:\Users
              \'USER'\PycharmProjects\DjangoWeb\template'  if you create the name of directory is tmp the 
              code must be "TEMPLATE_DIR = os.path.join(BASE_DIR, 'tmp')"
              
       step.2 add the adress to django
              add TEMPLATE_DIR, to 'DIRS': [], which in setting.py\TEMPLATE
              
       step.3 connect your views with html
              type in views
              def homepage_view (request):
                     return render(request, 'base.html')
       step.4 connect your views with urls
              type in urls
              from my_app import views
              urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.homepage_view, name='home'),       ##add this one  **name is for calling in html EX:action="{% url 'home' %}"
              ]
     
CONNECT CSS AND IMG TO HTML
       
                     
       step.1 create directory of static
              add directory below project named"static"
              add directory below static named"css" and "img"
              also you could create static below app                   ##when you do this way then your can type <img src="/static/img/view.jpg"> in your html to show the pic
                                                                       ##or add {% load static %} top of html and type  <img src="{% static 'img/view.jpg'%}"> 
              then you should creat the static-root below project      
              
              type in setting
              STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static') ##announce the address of static-root
              run "python manage.py collectstatic" it will collect all static in to static-root
              
       
       step.2 connect to html
              type in setting
              STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) ##announce the address of static  if have other static in app prefer change the name common_static
              then connect your css
              <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css">
              <img src="/static/img/view.jpg">
            
