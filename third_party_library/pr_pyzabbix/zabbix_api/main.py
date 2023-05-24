from zabbix_api.api_mediatype import mediatype_get, mediatype_delete, mediatype_create
from zabbix_api.api_user import user_get, user_delete, user_create
from zabbix_api.api_action import action_get, action_delete, action_create

action_ids = action_get()
if action_ids:
    action_delete(action_ids)

mediatype_ids = mediatype_get()
if mediatype_ids:
    mediatype_delete(mediatype_ids)

user_ids = user_get()
if user_ids:
    user_delete(user_ids)

mediatype_create()
user_create()
action_create()
