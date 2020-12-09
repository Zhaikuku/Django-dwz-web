from django.shortcuts import redirect
# url 拦截器

try:

    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class LoginInterceptor(MiddlewareMixin):
    def _process_request(self, request):

        if request.path != '/login/':
            if request.session.exists(request.COOKIES.get('sessionid')):
                pass
            else:
                return redirect('_login_page')