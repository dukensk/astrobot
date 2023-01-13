from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


@require_GET
def robots_txt(request):
    current_site = get_current_site(request)
    if settings.SITE_NO_INDEX:
        lines = [
            'User-agent: *',
            'Disallow: /',
        ]
    else:
        lines = [
            'User-Agent: *',
            'Host: {0}'.format(current_site.domain),
            # 'Sitemap: {0}'.format(request.build_absolute_uri(reverse('django.contrib.sitemaps.views.sitemap'))),
        ]
    return HttpResponse('\n'.join(lines), content_type="text/plain")
