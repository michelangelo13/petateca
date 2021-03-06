from django.conf.urls.defaults import *
from django.conf import settings

from haystack.views import SearchView, search_view_factory
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet

from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

from registration.forms import RegistrationFormTermsOfService
from invitation.views import register 
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    (r'^$', 'views.index'),
    # estadistcas
    (r'^stats/$', 'views.statistics'),

    (r'^sentry/', include('sentry.urls')),

    (r'^serie/', include('serie.urls.obj')),
    (r'^series/', include('serie.urls.entity')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^api/$', redirect_to, { 'url': '/api/v1' }, name='api'),
    (r'^api/v1/', include('api.urls')),

    (r'^search/lookup/$', 'search.views.search_lookup'),

    (r'^search/$', search_view_factory(
        view_class=SearchView,
        searchqueryset=SearchQuerySet(),
        form_class=ModelSearchForm
    )),

    (r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^faq/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'faq.html'},
        name="faq"
       ),
    url(r'^aviso-legal/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'aviso-legal.html'},
        name="aviso-legal"
       ),
    url(r'^politica-privacidad/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'politica-privacidad.html'},
        name="politica-privacidad"
       ),

    # Usuarios, invitaciones, registros, avatar, etc
    (r'^accounts/', include('invitation.urls')),
    (r'^accounts/profile/$', 'userdata.views.view_profile'),
    url(r'^accounts/register/$',
        register,
        {
            'form_class': RegistrationFormTermsOfService,
            'backend': 'invitation.backends.InvitationBackend',
        },
        name='registration_register'),
    url(r'^accounts/signin/$',
        auth_views.login,
        {
            'template_name': 'invitation/signin.html', 
        },
        name='auth_login'),
    (r'^accounts/', include('registration.urls')),
    url(r'^user/(?P<user_name>[-\w]+)$', 'userdata.views.get_user_public_profile', name='get_user_public_profile'),
    (r'^accounts/avatar/', include('avatar.urls')),
    url(r'^accounts/invitation/request/$', 'userdata.views.request_invitation', name='request_invitation'),
    url(r'^accounts/invitation/thanks/$', 'django.views.generic.simple.direct_to_template', {'template': 'invitation/thanks.html'},),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^rosetta/', include('rosetta.urls')),
    )
