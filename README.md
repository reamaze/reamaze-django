# Reamaze

**The simplest way to add a fully integrated support experience to your web site or web app**

[Reamaze](https://www.reamaze.com) is a fully embeddable support system that you can add with a few lines of JavaScript. Reamaze can help you handle your traditional email support along with your in-app knowledge base, support widget and live chat.

This package provides a Django tag helper that makes the SSO integration even easier.

## Installation

* pip install reamaze
* in settings.py, add reamaze to `INSTALLED_APPS`
* in base.html (or whichever template acts as the layout), at the top, add `{% load reamaze_js_tags %}`
* For the most basic integration, add the following at the bottom of base.html:
  ```
    {% reamaze_js 'your_brand_subdomain' %}
  ```
* Alternatively, to automatically log your users into the system you can use SSO integration. You'll find your SSO Key available via Settings within your Reamaze account: 
  ```
    {% reamaze_js 'your_brand_subdomain' sso_key=sso_key user_id=user_id user_email=user_email %}
  ```


### Pre-requisites

* Django (Only tested on 1.4 & 1.5)


## Copyright

See LICENSE for details.
