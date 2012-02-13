from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
    
class FancyBoxPlugin(CMSPlugin):
    link_text = models.CharField(max_length=255, blank=True, null=True)
    
    link_image = FilerImageField(null=True, blank=True, default=None, related_name='fancyboxplugin_set_link_image')
    link_image_height = models.PositiveIntegerField(blank=True, null=True)
    link_image_width = models.PositiveIntegerField(blank=True, null=True)
    link_image_alignment = models.CharField(max_length=100, blank=True, null=True, choices=(('left', 'Left'), ('right', 'Right')))
    
    target_image = FilerImageField(null=True, related_name='fancyboxplugin_set_target_image')
    target_image_height = models.PositiveIntegerField(blank=True, null=True)
    target_image_width = models.PositiveIntegerField(blank=True, null=True)
    target_image_title = models.CharField(max_length=255, blank=True, null=True)
    
    popup_text = models.TextField(null=True)
    
    def get_target_image_dimensions(self):
        height = self.target_image_height or self.target_image.height
        width = self.target_image_width or self.target_image.width
        return '%sx%s' % (width, height)
    
    def get_link_image_dimensions(self):
        height = self.link_image_height or self.link_image.height
        width = self.link_image_width or self.link_image.width
        return '%sx%s' % (width, height)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or link_text are set
        if (not self.link_image and not self.link_text):
            raise ValidationError(_('Either an image or link text must be selected.'))

