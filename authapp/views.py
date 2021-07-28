from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import pyrebase
from django.contrib import auth

config={
    "apiKey": "AIzaSyAD4mXz-UOq6n7nZBzhhXwalc-vnX1hCVo",
    "authDomain": "authentication-7babf.firebaseapp.com",
    "databaseURL": "https://authentication-7babf-default-rtdb.firebaseio.com",
    "projectId": "authentication-7babf",
    "storageBucket": "authentication-7babf.appspot.com",
    "messagingSenderId": "440732563913",
    "appId": "1:440732563913:web:2efea0ba1bf5962e2e9018",
    

}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

# Welcome page 
def index(request):
    return render(request, 'index.html')


# Sign Up to new user
def handleSignup(request):
    firstname=request.POST.get('fname')
    lastname=request.POST.get('lname')
    DOB=request.POST.get('dob')
    Place_of_Birth=request.POST.get('pob')
    email=request.POST.get('email')
    password=request.POST.get('pswd')
    
    try:
        user=authe.create_user_with_email_and_password(email, password)
        messages="You have been successfully registered."

    except:
        messages="Unable to create account make sure your password must be strong. Try again!"
        return render(request, 'signUp.html', {'msg':messages})    
    uid=user['localId']
    data={"firstname": firstname, 'lastname':lastname, 'DOB':DOB, 'Place_of_Birth':Place_of_Birth, "status":"1"}
    database.child('user').child(uid).child('details').set(data)
    return render(request,'index.html', {'msg':messages, 'user':user})

# Sign In to registered user
def handleSignin(request):
    email=request.POST.get('email')
    password=request.POST.get('pswd')
    try:
        user=authe.sign_in_with_email_and_password(email, password)
        messages="Welcome! You have Successfully Loged In."
    except:
        messages='Invalid credentials'    
        return render(request, 'signIn.html',{ 'msg':messages})
    params={'user':user, 'msg': messages}
    return render(request, 'index.html', params)

# Logout to authenticate user    
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


# Reset Password
def reset(request):
    return render(request, "Reset.html")

# Send the email to reset the password  
def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "Reset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg":message})


# About our page
def about(request):
    return render(request, 'about.html')    

# To Contact our Team
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages='Your messages has been successfully sent!!'
        return render(request, 'index.html', {"msg":messages})    
    return render(request, 'contact.html')
