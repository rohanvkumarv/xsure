from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from main.models import Lancer
from .mixins import MessaHandler  # Import your MessageHandler module
import random 
from main import *
# Create your views here.

from django.shortcuts import render,redirect, reverse
from .models import *
import random
from .mixins import MessaHandler
# Create your views here.
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render

from django.contrib.auth import login, logout

# def index(request):
#    from django.http import JsonResponse

# def index(request):
#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')
        
#         if 'combined_data' not in request.session:
#             request.session['combined_data'] = {'Step 1 Data': {}, 'Step 2 Data': {}}
        
#         if form_type == 'step1':
#             request.session['combined_data']['Step 1 Data'] = {
#                 'file_name': request.POST.get('file_name'),
#                 'email': request.POST.get('email'),
#                 'message': request.POST.get('message')
#             }
#             request.session.modified = True  # Mark the session as modified
            
#             # Process Step 1 form data here
            
#         elif form_type == 'step2':
#             request.session['combined_data']['Step 2 Data'] = {
#                 'phone_number': request.POST.get('phone_number')
#             }
#             request.session.modified = True  # Mark the session as modified
            
            
#             phone_number = request.session['combined_data']['Step 2 Data'].get('phone_number')

#             if phone_number:
#                 # Generate a random 4-digit number as OTP
#                 random_number = str(random.randint(1000, 9999))

#                 # Call your MessageHandler function to send the OTP to the provided phone number
#                 message_handler = MessaHandler(phone_number, random_number)
#                 otp_sent = message_handler.send_otp_on_phone()
            
#             # Process Step 2 form data here

#         # Print combined data
#         print("Combined Data:")
#         print(request.session['combined_data'])
        
#         return JsonResponse({'message': 'Form data received successfully'})
#     else:
#         return render(request, 'index.html')


# def index(request):

#     if request.method == 'POST':
#         # Check which step's form data was submitted based on the presence of specific fields
#         if 'file_name' in request.POST and 'email' in request.POST and 'message' in request.POST and 'radio' in request.POST:
#             # Process step 1 form data
#             file_name = request.POST.get('file_name')
#             email = request.POST.get('email')
#             message = request.POST.get('message')
#             radio = request.POST.get('radio')

#             # Process or save the data from step 1 form

#             # Return JSON response or any necessary data
#             return JsonResponse({'success': True, 'step': 1})

#         elif 'phone-number' in request.POST:
#             # Process step 2 form data
#             phone_number = request.POST.get('phone-number')

#             # Process or save the data from step 2 form

#             # Return JSON response or any necessary data
#             return JsonResponse({'success': True, 'step': 2})

#         elif 'otp' in request.POST:
#             # Process step 3 form data
#             otp = request.POST.get('otp')

#             # Process or save the data from step 3 form

#             # Return JSON response or any necessary data
#             return JsonResponse({'success': True, 'step': 3})

    

#     return render (request ,'index.html')
    
def index1(request):
    return render (request ,'index1.html')
def indexfinal(request):
    return render (request ,'indexFINAL.html')
def indexking(request):
    return render (request ,'index.html')
def test1(request):
    return render (request ,'test1.html')
def test2(request):
    return render (request ,'test2.html')
def test3(request):
    return render (request ,'test3.html')
def otp_ver(request):
    return render (request ,'otp_ver.html')
def about(request):
    return render (request ,'about.html')
def login(request):
    return render (request ,'login.html')



# logic part here 

# views.py

from django.shortcuts import render, redirect

def index(request):
    
    
    request.session.pop('file_name', None)
    request.session.pop('cost', None)
    request.session.pop('message', None)
    request.session.pop('allow_without_pay', None)
    request.session.pop('tempfileid', None)

    if request.method == 'POST':
        # Get form data
        file_name = request.POST.get('file_name')
        cost = request.POST.get('cost')  # Assuming 'email' is for 'cost'
        message = request.POST.get('message')  # Assuming 'message' for message field
        allow_without_pay = request.POST.get('radio')
        

        uploaded_file = request.FILES.get('file_upload')
        tempfileid = None 
        
        
        # if uploaded_file:
        #     tempfile = TempFile(file=uploaded_file)
        #     tempfile.save()

        #     # Save the unique identifier (tempfile.id) in the session
        #     request.session['tempfileid'] = tempfile.id
            

        if uploaded_file:
            tempfile = TempFile(file=uploaded_file)
            tempfile.save()

            # Save the unique identifier (tempfile.id) in the session
            request.session['tempfileid'] = tempfile.id
            tempfileid = tempfile.id  # Assign tempfile.id to tempfileid
       
            
            
        
            
            

            
        # Store form data in session
        request.session['file_name'] = file_name
        request.session['cost'] = cost
        request.session['message'] = message
        request.session['allow_without_pay'] = allow_without_pay
        
        

        print("File Name:", file_name)
        print("Cost:", cost)
        print("Message:", message)
        print("Allow Without Pay:", allow_without_pay)
        # print('file id ',tempfileid)
        print('File ID:', tempfileid) 
        
        return redirect('/veri')  
    
    
    return render(request, 'index.html')  # Replace 'your_template.html' with your actual template name


# def veri(request):
#   if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
        
#         # profile =  Lancer.objects.filter(phone_number=phone_number)
        
#         # if profile.exists():
#         #     phone = '+91' + phone_number
#         #     random_number = random.randint(1000, 9999)
#         #     request.session['random_number'] = random_number
#         #     request.session['phone_number'] = phone_number

#         #     print(f'Variable1: {random_number}')
#         #     return redirect('/otp/') 
        
        
#         # user_id = uuid.uuid4()
        
#         # request.session['user_id'] = str(user_id)
        
#         phone ='+91' + phone_number
#         random_number = random.randint(1000, 9999)
#         request.session['random_number'] = random_number
#         request.session['phone_number'] = phone_number
        
#         print(f'Variable1: {random_number}')
        
#         # message_handler = MessaHandler(phone,random_number ).send_otp_on_phone()
#         return redirect('/otp/')
#   return render(request, 'veri.html')
#         #
    
    
    
def veri(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        print(phone_number)
        
        if phone_number is not None:  # Check if phone_number is not None
            phone = '+91' + phone_number
            random_number = random.randint(1000, 9999)
            request.session['random_number'] = random_number
            request.session['phone_number'] = phone_number
            
            num=request.session['tempfileid']
            print("num", num)
            request.session['temper'] = num
            
            
            print

            print(f'Variable1: {random_number}')
            return redirect('/otp')
        else:
            # Handle the case where phone_number is None (optional)
            error_message = "Phone number is missing."
            return render(request, 'veri.html', {'error_message': error_message})
    
    return render(request, 'veri.html')

from django.utils.text import slugify


import string
import random


def generate_username(counter):
    human_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jack']
    name_index = counter % len(human_names)
    username = human_names[name_index] + str(counter // len(human_names))
    return username
def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


from django.contrib.auth import login 
def otp_ver(request):
    if request.method == 'POST':
        
        
        otp = request.POST.get('otp')
        random_number = request.session['random_number']
        phone_number = request.session['phone_number']
        tempfile_id = request.session['temper']
                
                 
        print("file id:", tempfile_id)
        
        
        print("Random Number:", random_number)
        print("otp", otp)
        
        if int(otp) ==int(random_number):
            print("verified")
            file_name = request.session.get('file_name')
            cost = request.session.get('cost')
            message = request.session.get('message')
            phone_number = request.session.get('phone_number')
            allow_payment = request.session.get('radio')
            
            try:
                user = User.objects.get(phone_number=phone_number)
                username = user.username
                lancer= Lancer.objects.get(phone_number=phone_number)
                
                project = Projects.objects.create(
                        lancer=lancer,
                        title=file_name,
                        cost=cost,
                        message=message,
                        status='notpaid', 
                        allow_without_pay=allow_payment,# Assuming initial status is 'notpaid'
                         # You might generate a link or leave it empty for now
                    )
               
                project.save()
                
                
                if tempfile_id:
                    try:
                       
                        tempfile = TempFile.objects.get(id=tempfile_id)
                        
                       
                        project.files = tempfile.file
                        project.save()
                        
                    except tempfile.DoesNotExist:
                      
                        pass
                return redirect(reverse('preview', kwargs={'title': project.title}))
                    
                    
                
                
                
                      
            except User.DoesNotExist:
                print("before",allow_payment)
                counter = User.objects.count()  # Get the total number of users
                
                # Generate a unique username
                username = generate_username(counter)
                
                user = User.objects.create(
                    phone_number=phone_number,
                    username=username 
                    )
                
                lancer = Lancer.objects.create(
                        user=user,
                        phone_number=phone_number,
                        name=username,  
                        is_superuser=True 
                    )
                lancer.save()
                login(request,user)
                link_text = slugify(file_name)
                link_text = "http://127.0.0.1:8000/preview/"+link_text     
                
                # link_text_ = link_text+ "-" + generate_random_string()
                
                # unique_link="http://127.0.0.1:8000/preview/"+link_text_     
               
                # link=unique_link,
                
                
                
  
                   
                
               
                project = Projects.objects.create(
                        lancer=lancer,
                        title=file_name,
                        cost=cost,
                        message=message,
                        status='notpaid',  # Assuming initial status is 'notpaid'
                        link=link_text,  # You might generate a link or leave it empty for now
                    )
                project.save()
                
                
                if tempfile_id:
                    try:
                       
                        tempfile = TempFile.objects.get(id=tempfile_id)
                        
                       
                        project.files = tempfile.file
                        project.save()
                        
                    except tempfile.DoesNotExist:
                      
                        pass
                    
                    
                user = User.objects.get(phone_number=phone_number)
                
                
                
               
                            
                return redirect(reverse('preview', kwargs={'title': project.title}))
                

    return render(request, 'otp_ver.html')










from django.conf import settings
import razorpay
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import razorpay
import json

def preview(request,title):
    
   
    project= get_object_or_404(Projects, title=title,)
    cost = project.cost
    yes_no =project.allow_without_pay
    print(yes_no)
    
    
    print(cost)
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    payment= client.order.create({'amount': cost,'currency': 'INR', 'payment_capture': 1})
    
    project.razor_pay_order_id = payment['id']
    project.save()
    
    
   
    # context = {}
    
    # context = {'client_':client_,}
    # print(payment.amount)
    print(payment['amount'])
    
    context = {
        'project': project,
        'payment ': payment,
        'payment_amount': payment['amount'],
        'payment_id': payment['id'],
        'file_name': title
        
    }
    return render(request, 'preview.html', context)





from django.http import HttpResponse

def download(request,title):
   
    project = get_object_or_404(Projects, title=title,)
    
    order_id = request.GET.get('order_id') 
    if order_id:
        try:
            project=Projects.objects.get(razor_pay_order_id=order_id)
            project.status = 'paid'
            project.save()
            context = {'project': project}
            return render(request, 'download.html', context)
        except project.DoesNotExist:
            # Handle the case where the OneTimeClient with the provided order_id doesn't exist
            pass
     # Handle other cases, such as invalid order_id or missing order_id
    return HttpResponse("Invalid order_id or missing parameter")

    
    # order_id = request.GET.get('order_id')
    # client_=OneTimeClient.objects.get(razor_pay_order_id=order_id)
    # client_.status ='paid'
    # client_.save()
    
    
    
    # context = {'client_':client_,}
    # return render(request, 'success.html',context)



  

def prof_login(request):
    if request.method == 'POST':
        
        phone_number = request.POST.get('phone_number')
        profile = Lancer.objects.filter(phone_number=phone_number).first()
        
        if not profile:
            return redirect('/')

        phone = '+91' + phone_number
        random_number = random.randint(1000, 9999)
        request.session['random_number'] = random_number
        request.session['phone_number'] = phone_number

        print(f'Variable1: {random_number}')

        # You can add code to send the OTP via SMS here if needed.

        return redirect('/prof_otp')
    
    return render (request ,'prof_login.html')


def prof_otp(request):
    if request.method == 'POST':
        
        
        otp = request.POST.get('otp')
        random_number = request.session['random_number']
        
        phone_number = request.session['phone_number'] 
        
        
        
        print("Random Number:", random_number)
        print("otp", otp)
        
        
        if int(otp) ==int(random_number):
            print("verified")
            
            try:
                user = User.objects.get(phone_number=phone_number)
                username = user.username       
            except User.DoesNotExist:
                return redirect('/')
                
            login(request,user)
            
            return redirect(reverse('prof_dash', kwargs={'username': user.username}))
        
            print("verified")
            
            try:
                user = User.objects.get(phone_number=phone_number)
                username = user.username 
                
            
                
            except User.DoesNotExist:
                
                username = request.session['username'] 
                # pfp
                random.seed(2)

                ran_ = random.randint(1,10)
                profile_pic = f'profile_pics/pfp_{ran_}.jpg'
                
                print(f'profile_pics/pfp_{{ran_}}.jpg')
                
                # pfp ends
                
                user = User.objects.create(username=username, phone_number=phone_number,)
                
                
               
                profile = Profile.objects.create(user=user, phone_number=phone_number,pfp=profile_pic)
            login(request,user)
            

            return redirect(reverse('client', kwargs={'username': user.username}))
    return render (request ,'prof_otp.html')



def prof_dash(request,username):
    
    # profile = get_object_or_404(Lancer, user__username=username,)
    
    # user_username = profile.user.username
    # phone_number = profile.phone_number
    
    
    # projects = Projects.objects.filter(lancer=profile)
    # context = {'username':user_username, 
               
    #            'phone_number':phone_number , 'projects': projects,           
    #      }

    # return render (request ,'prof_dash.html',context)


    profile = get_object_or_404(Lancer, user__username=username)
    user_username = profile.user.username
    phone_number = profile.phone_number

    projects = Projects.objects.filter(lancer=profile)

    context = {
        'username': user_username,
        'phone_number': phone_number,
        'projects': projects,
        'lancer_name': profile.name,  # Assuming 'name' is the field in Lancer model for name
    }

    return render(request, 'prof_dash.html', context)