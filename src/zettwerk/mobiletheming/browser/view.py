from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from urlparse import urlparse


class JavaScript(BrowserView):

    def __call__(self, request=None, response=None):
        """Returns configurations."""
        self.registry = getUtility(IRegistry)
        self.request.response.setHeader("Content-type", "text/javascript")

        return """\
            var mobile_domain = "%(hostname)s";
            var ipad = "%(ipad)s";
            var other_tablets = "%(tablets)s";
            document.write(unescape("%%3Cscript src='/++resource++zettwerk.mobiletheming.scripts/me.redirect.min.js' type='text/javascript'%%3E%%3C/script%%3E"));

            """ % {
                'hostname': self.hostname,
                'ipad': self.ipad,
                'tablets': self.tablets,
            }

    @property
    def hostname(self):
        registry = getUtility(IRegistry)
        hostnames = registry[
            'zettwerk.mobiletheming.interfaces.IMobileThemingSettings' \
                '.hostnames'
        ]
        url = hostnames[0] or 'mylocalhost'
        o = urlparse(url)
        return o.hostname

    @property
    def tablets(self):
        return self.registry[
            'zettwerk.mobiletheming.interfaces.IMobileThemingSettings' \
                '.tablets'
        ]

    @property
    def ipad(self):
        return self.registry[
            'zettwerk.mobiletheming.interfaces.IMobileThemingSettings' \
                '.ipad']
