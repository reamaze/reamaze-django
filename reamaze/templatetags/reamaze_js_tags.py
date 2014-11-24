from django import template
from django.conf import settings
import hmac
import hashlib

register = template.Library()

def reamaze_js(brand_subdomain='', sso_key='', user_id=None, user_email=None):
    context = {
        'brand_subdomain': brand_subdomain
    }

    if user_id and user_email:
        hmac_message = unicode("%s:%s" % (str(user_id), str(user_email)))
        hmac_key = str(sso_key)
        context['user_id'] = user_id
        context['user_email'] = user_email
        context['authkey'] = hmac.new(hmac_key, hmac_message, hashlib.sha256).hexdigest()

    return context

register.inclusion_tag('reamaze/reamaze_js.html')(reamaze_js)
