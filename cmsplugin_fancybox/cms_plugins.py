from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse
from cmsplugin_fancybox.models import FancyBoxPlugin
from cmsplugin_fancybox.forms import FancyBoxImagePluginForm, FancyBoxRichTextPluginForm, FancyBoxSnippetPluginForm


class CMSFancyBoxImagePlugin(CMSPluginBase):
    model = FancyBoxPlugin
    form = FancyBoxImagePluginForm
    name = _("Fancybox Image Popup")
    render_template = "cmsplugin_fancybox/cmsplugin_fancybox_image.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        context.update({
            'placeholder': placeholder,
            'instance': instance,
        })
        return context
        

class CMSFancyBoxRichTextPlugin(CMSPluginBase):
    model = FancyBoxPlugin
    form = FancyBoxRichTextPluginForm
    name = _("Fancybox Rich Text Popup")
    render_template = "cmsplugin_fancybox/cmsplugin_fancybox_richtext.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        context.update({
            'placeholder': placeholder,
            'instance': instance,
        })
        return context
        
        
class CMSFancyBoxSnippetPlugin(CMSPluginBase):
    model = FancyBoxPlugin
    form = FancyBoxSnippetPluginForm
    name = _("Fancybox Snippet Popup")
    render_template = "cmsplugin_fancybox/cmsplugin_fancybox_richtext.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'placeholder': placeholder,
            'instance': instance,
        })
        return context
        

plugin_pool.register_plugin(CMSFancyBoxImagePlugin)
plugin_pool.register_plugin(CMSFancyBoxRichTextPlugin)
plugin_pool.register_plugin(CMSFancyBoxSnippetPlugin)

