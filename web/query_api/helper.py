"""Helper Functions"""
import re
from datetime import datetime
import pytz

from django.contrib.auth.models import User


def frontend_str_to_time(input_str, time_float=False):
    try:
        if time_float:
            return datetime.strptime(input_str, '%Y-%m-%dT%H:%M:%S.%f%z')
        return datetime.strptime(input_str, '%Y-%m-%dT%H:%M:%S%z')
    except:
        key_regex = re.compile(r'(.*)(\.)(.*)')
        input_time = key_regex.search(input_str).group(1)
        return pytz.utc.localize(datetime.strptime(input_time, '%Y-%m-%dT%H:%M:%S'))


def get_user(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None

def get_username(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
