from django.shortcuts import render
from django.shortcuts import render ,redirect,get_object_or_404

from .model.student import Student
from .model.branch import Branch

def student_list(request):
    students=Student.objects.all()
    
    return render(request,'vast_app/list.html',{'student':students})


def student_create(request):
    if request.method == 'POST':
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        branch_id=request.POST.get('branch')
        contact =request.POST.get('contact')
        
        branch=get_object_or_404(Branch,id=branch_id)
        
        students=Student(
            name=name,
            email=email,
            branch=branch,
            contact=contact,
        )
        students.save()
        return redirect('list')
    branches=Branch.objects.all()
    return render(request, 'vast_app/create_list.html',{'branch':branches})
