"""Development Issues Views"""
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import DevelopmentForm, SudoDevelopmentForm
from .models import DevelopmentTasks

def model_form_upload(request):
    if request.method == 'POST':
        form = DevelopmentForm(request.POST, request.FILES)
        form.instance.request = request.user
        if form.is_valid():
            form.save()
            return redirect('development_list')
    else:
        form = DevelopmentForm()
    return render(request, 'development/model_form_upload.html', {
        'form': form
    })


@method_decorator(login_required, name='dispatch')
class DevelopmentDetailView(DetailView):
    model = DevelopmentTasks
    template_name = 'development/development_detail.html'
    context_object_name = 'dev'

@method_decorator(login_required, name='dispatch')
class DevelopmentListView(ListView):
    model = DevelopmentTasks
    template_name = 'development/development_list.html'
    context_object_name = 'dev_list'

@method_decorator(login_required, name='dispatch')
class DevelopmentUpdateView(UpdateView):
    model = DevelopmentTasks
    form_class = SudoDevelopmentForm
    template_name = 'action/action_edit.html'
    success_url = reverse_lazy('development_list')
