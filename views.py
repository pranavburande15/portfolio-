from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'name':'Pranav Burande',
        'degree':'B.sc(ECS) 3rd Year(Computer Science)',
        'college':'Shriram Institute Of information Technology , Paniv tel.Malshiras',
        'skills':['Python','Django','HTML','CSS','SQL'],
        'certification':['Infosys Springboard-Python Programming Fundamentals(82.35%)'],
    }
    return render(request,'home.html',context)