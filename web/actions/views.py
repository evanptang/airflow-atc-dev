from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)

from django.contrib.auth.models import User
from .forms import ActionForm

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Action

class ActionListView(LoginRequiredMixin, ListView):
    model = Action
    template_name = 'action/action_list.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = Action.objects.filter(active=True)
        return queryset.order_by('-datetime')


class ActionPendingConfirmationListView(LoginRequiredMixin, ListView):
    model = Action
    template_name = 'action/action_pending_approval.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = Action.objects.filter(pending_confirmation=True).exclude(user_added=self.request.user)
        return queryset.order_by('-datetime')


class ActionDetailView(LoginRequiredMixin, DetailView):
    model = Action
    template_name = 'action/action_detail.html'


class ActionUpdateView(LoginRequiredMixin, UpdateView):
    model = Action
    form_class = ActionForm
    template_name = 'action/action_edit.html'
    success_url = reverse_lazy('action_list')

    def form_valid(self, form): # new
        form.instance.user_added = self.request.user
        return super().form_valid(form)

class ActionDeleteView(LoginRequiredMixin, DeleteView):
    model = Action
    template_name = 'action/action_delete.html'
    success_url = reverse_lazy('action_list')

class ActionCreateView(LoginRequiredMixin, CreateView):
    form_class = ActionForm
    model = Action
    template_name = 'action/action_new.html'
    success_url = reverse_lazy('action_list')
    
    def form_valid(self, form):
        form.instance.user_added = self.request.user
        return super().form_valid(form)
