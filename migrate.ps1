#!/bin/bash


Write-Output ""
Write-Output "Migrando la aplicacion 'access'..."
python.exe .\manage.py makemigrations access


Write-Output ""
Write-Output "Migrando la aplicacion 'dates'..."
python.exe .\manage.py makemigrations dates


Write-Output ""
Write-Output "Migrando la aplicacion 'groups'..."
python.exe .\manage.py makemigrations groups


Write-Output ""
Write-Output "Migrando la aplicacion 'invitations'..."
python.exe .\manage.py makemigrations invitations


Write-Output ""
Write-Output "Migrando la aplicacion 'organizations'..."
python.exe .\manage.py makemigrations organizations


Write-Output ""
Write-Output "Migrando la aplicacion 'projects'..."
python.exe .\manage.py makemigrations projects


Write-Output ""
Write-Output "Migrando la aplicacion 'tasks'..."
python.exe .\manage.py makemigrations tasks



Write-Output ""
Write-Output "Aplicando en la bdd..."
python.exe .\manage.py migrate

Write-Output ""
Write-Output "FIN"