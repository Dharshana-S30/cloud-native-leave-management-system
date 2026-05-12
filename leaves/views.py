from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from .models import LeaveRequest


@login_required
def employee_dashboard(request):
    leaves = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'employee/dashboard.html', {'leaves': leaves})

@login_required
def my_leaves(request):
    leaves = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'employee/my_leaves.html', {'leaves': leaves})

@login_required
def manager_dashboard(request):
    return render(request, 'manager/dashboard.html')


@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect('employee_dashboard')
    else:
        form = LeaveForm()

    return render(request, 'employee/apply_leave.html', {'form': form})

@login_required
def manager_leaves(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'manager/manage_leaves.html', {'leaves': leaves})


@login_required
def update_status(request, id, status):
    leave = LeaveRequest.objects.get(id=id)
    leave.status = status
    leave.save()
    return redirect('manager_leaves')