"""API Post Views"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from insert.models import AirMarshallResponse
from issue.models import AirMarshallLogsWithNotes
from actions.models import Action
from query_api.helper import(
    frontend_str_to_time,
    get_user
)

@api_view(['GET', 'POST'])
def modify_support_notes(request):
    """
    Update Support Notes in the model AirMarshallResponse
    """
    if request.method == 'GET':
        return Response(
            {
                "message": "this endpoint is designed to modify" +
                " the support notes field of the model AirMarshallResponse",
            }
        )

    elif request.method == 'POST':
        request_data = request.data
        try:
            issue_id = request_data["issue_id"]
            message = request_data["message"]
        except:
            return Response(
                {"errors": "missing the fields issue_id or message"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        obj = AirMarshallResponse.objects.filter(issue_id=issue_id)
        if not obj:
            return Response(
                {"errors": "invalid issue_id"},
                status=status.HTTP_400_BAD_REQUEST
            )
        obj.update(support_notes=message)
        return Response(
            {
                "status":"update successful",
                "issue_id":issue_id,
                "message":message,
            },
            status=status.HTTP_201_CREATED
        )


@api_view(['POST'])
def remove_response(request):
    """
    remove_response
    """
    request_data = request.data
    try:
        issue_id = request_data["issue_id"]
    except KeyError:
        return Response(
            {"errors": "invalid issue_id"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    AirMarshallResponse.objects.filter(
        issue_id=issue_id).delete()

    return Response(
        {
            "status": "success",
        },
    )


@api_view(['GET', 'POST'])
def upsert_into_notes(request):
    """
    Upsert into Database for Notes
    """
    if request.method == 'GET':
        return Response(
            {
                "message": "this endpoint is designed to upsert" +
                " into the model Air Marshall Logs with Notes",
            }
        )

    elif request.method == 'POST':
        request_data = request.data
        try:
            issue_id = request_data["issue_id"]
            assignee = request_data["assignee"]
            dag = request_data["dag"]
            execution = frontend_str_to_time(request_data["execution"])
            etl = frontend_str_to_time(request_data["etl"], time_float=True)
            task = request_data["task"]
            user = request_data["user"]
        except:
            return Response(
                {"errors": "missing the fields"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        note_row, created = AirMarshallLogsWithNotes.objects.update_or_create(
            issue_id=issue_id,
            defaults={
                'dag_id': dag,
                'execution_datetime': execution,
                'first_failed_task': task,
                'response_by': get_user(assignee),
                'reporter': get_user(user),
                'etl_ingestion_time': etl,
                'investigator_resolved': False,
                'assignee_resolved': False,
            }
        )

        if not note_row:
            return Response(
                {"errors": "Object Not Created"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "status":"success",
                "created": created
            }, 
            status=status.HTTP_201_CREATED
        )

@api_view(['GET', 'POST'])
def create_note_if_none(request):
    """
    Create Note if does not exist
    """
    if request.method == 'GET':
        return Response(
            {
                "message": "this endpoint is designed to create a note if it does not exist" +
                " into the model Air Marshall Logs with Notes",
            }
        )

    elif request.method == 'POST':
        request_data = request.data
        try:
            issue_id = request_data["issue_id"]
            dag = request_data["dag"]
            execution = frontend_str_to_time(request_data["execution"])
            etl = frontend_str_to_time(request_data["etl"], time_float=True)
            task = request_data["task"]
            user = request_data["user"]
        except:
            return Response(
                {"errors": "missing the fields"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        obj = AirMarshallLogsWithNotes.objects.filter(issue_id=issue_id)
        if not obj:
            note_row = AirMarshallLogsWithNotes.objects.create(
                issue_id=issue_id,
                dag_id=dag,
                execution_datetime=execution,
                first_failed_task=task,
                reporter=get_user(user),
                etl_ingestion_time=etl,
                assignee_resolved=False,
                investigator_resolved=False,
            )

            if not note_row:
                return Response(
                    {"errors": "Object Not Created"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {
                "status":"success",
            }, 
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'POST'])
def approve_action(request):
    """
    Approve Action
    """
    if request.method == 'GET':
        return Response(
            {
                "message": "this endpoint is designed to approve and incoming action",
            }
        )

    elif request.method == 'POST':
        request_data = request.data
        try:
            action_id = request_data["id"]
        except:
            return Response(
                {"errors": "missing the fields"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        action = Action.objects.get(id=action_id)
        action.active = True
        action.pending_confirmation = False
        action.save()
        return Response(
            {"status": "success"}, 
        )