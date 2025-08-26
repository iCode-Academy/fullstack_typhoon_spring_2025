from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'todos/task_list.html', {'tasks': tasks})

class TaskCreateView(LoginRequiredMixin, View):
    def post(self, request):
        title = request.POST.get('title')
        if title:
            Task.objects.create(user=request.user, title=title)
        return redirect('task_list')

class TaskUpdateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')

class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user = request.user)
        task.delete()
        return redirect('task_list')