from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
import sqlite
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
def all(request):

  # b = sqlite.getall(("ranjeet","python"))
  # data = []
  # for i in b:
  #     data.append({"firstname": i[0], "lastname": i[1]})
  #
  # print('>>>>>>>',b)
  # params = {'data1': data}
  return render(request, 'index.html')

@api_view(["GET", "POST"])
def login(request):
  # print(">>>>>", request.data['username'])

  print(request.data)
  if request.data:
    user = sqlite.getuser(request.data['username'])

    if user:
       request.session['logedinid']= user[0]
       return redirect("/addproblem")
    print(user)
  return render(request, "login.html")
@api_view(['GET','POST'])
def signup(request):
   if request.data:
       data = (request.data['firstname'], request.data['lastname'],request.data['email'],request.data['contact'],request.data['username'],request.data['password'])
       sqlite.createuser(data)
       return redirect("login")
   return render(request, "signup.html")
@api_view(['GET','POST'])
def addproblem(request):
    print(request.session['logedinid'])
    if request.data:
      data = (request.data['Status'], request.data['Title'], request.data['Solution'], request.data['Acceptance'], request.data['Difficulty'],request.session['logedinid'])
      sqlite.addproblem(data)
      return redirect("problems")
    return render(request, "addproblem.html")


@api_view(['GET', 'POST'])
def problems(request):
    data = sqlite.getall()
    dataobject = []
    for problem in data:
        dataobject.append({'id':problem[0],'status':problem[1],'title':problem[2], 'solution':problem[3],'acceptance':problem[4],'difficulty': problem[5] })

    params = {'data1': dataobject}
    return render(request, 'index.html', params)

@api_view(['GET','POST'])
def delete(request, id):
        sqlite.delete(id)
        return redirect("problems")




