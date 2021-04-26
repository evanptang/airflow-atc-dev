"""GET views"""
import re
import json
from datetime import datetime, timezone
import pytz

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core import serializers
from django.http import HttpResponse
from django.db.models import Count

from django.contrib.auth.models import User
from actions.models import Action
from insert.models import AirMarshallResponse
from issue.models import AirMarshallLogsWithIssueId, AirMarshallLogsWithNotes

from .aws_get_file import query_aws_last_modifed
from .helper import (
    frontend_str_to_time,
    get_user,
    get_username
)

# Create your views here.
@api_view(['GET'])
def query_action(request):
    """
    query action of air marshall response
    """
    issue_id = request.query_params["id"]
    filter_issue_id = re.compile(r'(action_error_|reason_)(.*)')
    issue_id = filter_issue_id.search(issue_id).group(2)
    obj = AirMarshallResponse.objects.filter(issue_id=issue_id).values('action')
    act = Action.objects.filter(id=obj[0]['action']).values()[0]['value']

    return Response(
        {
            "option": act,
        },
    )

@api_view(['GET'])
def query_notes_by_issue_id(request):
    """
    query action of air marshall response
    """
    issue_id = request.query_params["id"]
    filter_issue_id = re.compile(r'(notes_)(.*)')
    issue_id = filter_issue_id.search(issue_id).group(2)
    obj = AirMarshallResponse.objects.filter(issue_id=issue_id).values('support_notes')
    support_notes = obj[0]['support_notes']

    return Response(
        {
            "notes": support_notes,
        },
    )

@api_view(['GET'])
def log_issue(request):
    status = request.query_params["status"]
    airflow_id = request.query_params["id"]
    option = request.query_params["option"]
    username = get_user(request.query_params["username"])
    issue_id = request.query_params["issue"]
    task_id = request.query_params["task"]
    dag_id = request.query_params["dag"]
    dag_start_datetime = request.query_params["datetime"]
    dag_start_datetime = pytz.utc.localize(datetime.strptime(dag_start_datetime, '%Y-%m-%dT%H:%M:%S.%f'))
    act = Action.objects.get(value=option)
    if status == 'acknowledge':
        ack_bool = True
    else:
        ack_bool = False
    AirMarshallResponse.objects.create(
        acknowledged=ack_bool,
        airflow_id=int(airflow_id),
        action=act,
        username=username,
        issue_id=issue_id,
        dag_id=dag_id,
        task_id=task_id,
        dag_start_datetime=dag_start_datetime
    )
    return Response({
        "message": "success",
    })

@api_view(['GET'])
def update_action(request):
    """
    update action of air marshall response
    """
    issue_id = request.query_params["id"]
    action = request.query_params["action"]
    act = Action.objects.get(value=action)

    AirMarshallResponse.objects.filter(
        issue_id=issue_id).update(action=act)
    

    return Response(
        {
            "status": "success",
        },
    )


@api_view(['GET'])
def convert_airflow_id_to_relevant_metadata(request):
    issue_id = request.query_params["issueid"]
    airflow_id = request.query_params["airflowid"]

    try: 
        airflow_id = int(airflow_id)
    except ValueError:
        airflow_id = int(airflow_id[:-1])

    obj = AirMarshallLogsWithIssueId.objects.filter(
        issue_id=issue_id,
        id=airflow_id,
    )
    qs_json = serializers.serialize('json', obj)
    return HttpResponse(qs_json, content_type='application/json')

@api_view(['GET'])
def group_by_issue_id(request):
    issue_id = request.query_params["id"]
    issue_regex = re.compile(r'(popover_)(.*)')
    issue_id = issue_regex.search(issue_id).group(2)
    obj = AirMarshallLogsWithIssueId.objects.all().values(
        'issue_id').annotate(total=Count('issue_id')).order_by('total')
    obj = obj.filter(issue_id=issue_id)
    return Response({
        "status": "success",
        "count": str(obj[0]['total'])
    })
   

@api_view(['GET'])
def calculate_time_difference(request):
    time = request.query_params["time"]
    converted_time = frontend_str_to_time(time, time_float=True)
    utc_now = datetime.now(timezone.utc)
    datetime_difference = utc_now - converted_time
    return Response({
        "status": "success",
        "time_difference": str(datetime_difference)[:20]
    })


@api_view(['GET'])
def query_notes_for_response(request):
    html_id = request.query_params["id"]
    filter_regex = re.compile(r'^(form_assignee_)([\-a-zA-Z0-9]+)(\/*)')
    issue_id = filter_regex.search(html_id).group(2)
    obj = AirMarshallLogsWithNotes.objects.filter(issue_id=issue_id).only('response_by')
    if not obj:
        return Response({
            "response_by": None
        })
    else:
        queryset = serializers.serialize('json', obj)
        obj_dict = json.loads(queryset)
        username = get_username(obj_dict[0]['fields']['response_by'])
        return Response({
            "response_by": str(username),
        })

@api_view(['GET'])
def query_users(request):
    try:
        staff = request.query_params["staff"]
        if staff.lower() == 'true':
            staff = True
        else:
            staff = False
    except:
        staff=False

    obj = User.objects.filter(is_staff=staff)
    queryset = serializers.serialize('json', obj)
    queryset = json.loads(queryset)
    return_obj = list()
    for i in queryset:
        return_dict = dict()
        return_dict['username'] =i['fields']['username']
        return_dict['first_name'] = i['fields']['first_name']
        return_obj.append(return_dict)
    return Response({
        "response_by": return_obj
    })


@api_view(['GET'])
def query_aws(request):
    """
    Update Support Notes in the model AirMarshallResponse
    """
    try:
        bucket = request.query_params["bucket"]
        prefix = request.query_params["prefix"]
        response = query_aws_last_modifed(bucket, prefix)
        return Response(
            {
                "status":"query successful",
                "bucket":bucket,
                "prefix":prefix,
                "aws_response":response
            }
        )

    except:
        return Response(
            {
                "message": "this endpoint is designed to return the " +
                "last modified time from AWS given the keys bucket and prefix" +
                ". Please pass those two as query parameters. Limits results at 1000 records",
            }
        )


@api_view(['GET'])
def query_actions_table(request):
    """
    query action of air marshall response
    """
    acknowledge = request.query_params["acknowledge"]
    if acknowledge.lower() == 'true':
        acknowledge = True
    else:
        acknowledge = False

    obj = Action.objects.filter(active=True).filter(for_acknowledged=acknowledge)
    qs_json = serializers.serialize('json', obj)

    return Response(
        json.loads(qs_json)
    )


@api_view(['GET'])
def query_pending_action(request):
    """
    query action of air marshall response
    """
    user = request.query_params["user"]
    user = get_user(user)
    obj = Action.objects.filter(pending_confirmation=True).exclude(user_added_id=user)
    own_obj = Action.objects.filter(pending_confirmation=True)
    if obj is None or len(obj) == 0:
        if own_obj is None:
            return Response(
                {
                    'pending_action': None,
                    'own_action': False
                }
            )
        return Response(
            {
                'pending_action': None,
                'own_action': True
            }
        )
    else:
        return Response(
            {
                'pending_action': len(obj),
                'own_action': False

            }
        )
