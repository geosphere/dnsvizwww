from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

_encoded_slash = r'S'
_dns_label_first_char = r'[_a-z0-9]'
_dns_label_middle_char = r'[_a-z0-9-]|(%s)' % _encoded_slash
_dns_label_last_char = _dns_label_first_char
_dns_label = r'((%s)(%s)*(%s))|(%s)' % \
        (_dns_label_first_char, _dns_label_middle_char, _dns_label_last_char,
            _dns_label_first_char)
dns_name = r'(%s)(\.(%s))*' % (_dns_label, _dns_label)

timestamp = r'[a-zA-Z0-9-_]{6}'

ip_chars = r'[0-9a-fA-F:\.]{,39}'

urlpatterns = patterns('dnsvizwww.views',
        url(r'^d/(?P<name>%s)/(?P<url_subdir>(dnssec|responses|servers)/)?$' % dns_name, 'domain_view'),
        url(r'^d/(?P<name>%s)/(?P<url_subdir>dnssec)/(?P<url_file>auth_graph)\.(?P<format>png|jpg|svg|dot|js)$' % dns_name, 'dnssec_info'),
        url(r'^d/(?P<name>%s)/(?P<url_subdir>dnssec)/(?P<url_file>notices)\.(?P<format>xml|json)$' % dns_name, 'dnssec_info'),
        url(r'^d/(?P<name>%s)/info\.(?P<format>xml|json)$' % dns_name, 'info_view'),

        url(r'^d/(?P<name>%s)/(?P<url_subdir>cache/)$' % dns_name, 'analyze_cache'),
        url(r'^d/(?P<name>%s)/(?P<url_subdir>analyze/)$' % dns_name, 'analyze'),

        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>(dnssec|responses|servers)/)?$' % (dns_name, timestamp), 'domain_view'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>dnssec/)(?P<url_file>auth_graph)\.(?P<format>png|jpg|svg|dot|js)$' % (dns_name, timestamp), 'dnssec_info'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>dnssec/)(?P<url_file>notices)\.(?P<format>xml|json)$' % (dns_name, timestamp), 'dnssec_info'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/info\.(?P<format>xml|json)$' % (dns_name, timestamp), 'info_view'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/responses/(?P<qname>%s)/(?P<rdtype>[0-9]{1,5})/(?P<server>%s)/(?P<rd>t|f)(?P<do>t|f)(?P<cd>t|f)/(?P<client>%s)/$' % (dns_name, timestamp, dns_name, ip_chars, ip_chars), 'response_by_name_view'),

        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>cache/)(?P<server>%s)/(?P<cache_timestamp>%s)/dnssec/$' % (dns_name, timestamp, ip_chars, timestamp), 'domain_view'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>cache/)(?P<server>%s)/(?P<cache_timestamp>%s)/dnssec/(?P<url_file>auth_graph)\.(?P<format>png|jpg|svg|dot|js)$' % (dns_name, timestamp, ip_chars, timestamp), 'dnssec_info'),
        url(r'^d/(?P<name>%s)/(?P<timestamp>%s)/(?P<url_subdir>cache/)(?P<server>%s)/(?P<cache_timestamp>%s)/dnssec/(?P<url_file>notices)\.(?P<format>xml|json)$' % (dns_name, timestamp, ip_chars, timestamp), 'dnssec_info'),

        url(r'^r/(?P<qname>%s)/(?P<rdtype>[0-9]{1,5})/(?P<server>%s)/(?P<rd>t|f)(?P<do>t|f)(?P<cd>t|f)/(?P<client>%s)/(?P<timestamp>%s)/$' % (dns_name, ip_chars, ip_chars, timestamp), 'response_view'),

        url(r'^contact/$', 'contact'),
        url(r'^search/$', 'domain_search'),
)
urlpatterns += patterns('django.views.generic.simple',
        url(r'^$', 'direct_to_template', { 'template': 'main.html' } ),
        url(r'^d/$', 'redirect_to', { 'url': '/'}),
        url(r'^doc/$', 'direct_to_template', { 'template': 'doc.html' } ),
        url(r'^doc/faq/$', 'direct_to_template', { 'template': 'faq.html' } ),
        url(r'^doc/dnssec/$', 'direct_to_template', { 'template': 'dnssec_legend.html' } ),
        url(r'^message_submitted/$', 'direct_to_template', { 'template': 'message_submitted.html' } ),
)

urlpatterns += staticfiles_urlpatterns()