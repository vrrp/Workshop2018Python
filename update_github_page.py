"""
source: 
    https://steadylearner.com/blog/read/How-to-automatically-commit-files-to-GitHub-with-Python
    https://realpython.com/python-git-github-intro/
    https://git-scm.com/book/en/v2

    https://www.fullstackpython.com/blog/first-steps-gitpython.html
    https://gitpython.readthedocs.io/en/stable/tutorial.html
    https://stackoverflow.com/questions/7119452/git-commit-from-python
    
# Create a new repository on the command line
    $ echo " algun mensaje" >> READE.md
    $ git init
    $ git add README.md
    $ git commit -m "first commit"
    $ git remote add origin https://github.com/vrrp/vrrp.github.io.git
    $ git push -u origin master

# Push an existing repository from the command line
    $ git remote  add origin https://github.com/vrrp/vrrp.github.io.git
    $ git push -u origin master

# Import code from another repository

# remover directorios de un repositorio git
	$ git rm miarchivo.php
	$ git rm -r micarpeta
	$ git commit -m "estoy removiendo archivos obsoletos"
	$ git -f push

# Some error
    From https://github.com/vrrp/vrrp.github.io
   7ef9fb3..3aa27a5  master     -> origin/master
Auto-merging training/index.html
CONFLICT (content): Merge conflict in training/index.html
error: could not apply 97e896d... up yml
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 97e896d... up yml

"""

import os
import subprocess as cmd
import datetime as dt


path_now = os.getcwd()
#path_project = path_now+"/vrrp.github.io"
#path_img = "/home/proyectos/pyprojects/coronavirus2020_api/"

#os.chdir(path_project)

time = dt.datetime.now()
date = time.strftime("%d-%B-%Y")
times= time.strftime("%H:%M:%S")
mensaje = times+" "+date
#year = date.year; month=date.month; day=date.day
"""
cp=cmd.run("echo 'Actualizando repositorio'", check=True, shell=True)

response = input("Do you want to use the default message for this commit?([y]/n)\n")
mensaje = "actualizando repositorio"

if response.startswith('n'):
    mensaje = str(input("Que mensaje desea colocar?\n"))

cmd.run(f"git init", check=True, shell=True)
#cmd.run(f"git add ", check=True, shell=True)
cmd.run(f"git add  *", check=True, shell=True)
#cmd.run(f"git commit -m '{mensaje}'", check=True, shell=True)
os.system(f"git commit -m "+mensaje)
os.system("git status")
#cmd.run(f"git remote add origin https://github.com/vrrp/vrrp.github.io.git", check=True, shell=True)
cmd.run("git push -u origin master", check=True, shell=True)
"""

os.system("git init")
os.system("git add .")
os.system(f"git commit -m '{mensaje}'")
os.system("git push origin main")

