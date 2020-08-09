"# DjangoWeb" 
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
              django-admin startproject "src(projectname)"
              cd "src(porjectname)"\ 
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
ADD APP IN THE PROJECT

       step.1 open the IED whatever you wnat and open project
       
       step.2 open terminal screem and type ## also you can runserver here by "python manage.py runserver"
              python manage.py startapp "name of app"
              
