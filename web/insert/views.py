"""Views from the Insert App"""
from datetime import datetime, timedelta
import pytz

from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models import AirMarshallResponse


@method_decorator(login_required, name='dispatch')
class ResponseSearchListView(LoginRequiredMixin, ListView):
    model = AirMarshallResponse
    template_name = 'insert/response_search.html'
    login_url = 'login'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        hour_filter = self.request.GET.get('hourfilter', None)
        utcnow = pytz.utc.localize(datetime.utcnow())
        resp =  AirMarshallResponse.objects.order_by('-etl_ingestion_time'
            ).filter(username=self.request.user
            ).filter(acknowledged=True
            )
        if hour_filter is not None:
            try:
                hour_filter = int(hour_filter)
                datetime_hours_ago = utcnow - timedelta(hours=hour_filter)
                resp = resp.filter(
                    etl_ingestion_time__range=(datetime_hours_ago, utcnow)        
                )
            except:
                pass
        if query is not None:
            resp = resp.filter(
                Q(dag_id__icontains=query) | 
                Q(task_id__icontains=query) | 
                Q(partner_id__icontains=query)
            )
        return resp


@method_decorator(login_required, name='dispatch')
class IgnoreSearchListView(LoginRequiredMixin, ListView):
    model = AirMarshallResponse
    template_name = 'insert/response_ignored_issues.html'
    login_url = 'login'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        resp =  AirMarshallResponse.objects.order_by('-etl_ingestion_time'
            ).filter(acknowledged=False
            )
        if query is not None:
            resp = resp.filter(
                Q(dag_id__icontains=query) | 
                Q(task_id__icontains=query) | 
                Q(partner_id__icontains=query)
            )
        return resp
