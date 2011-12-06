from django import forms
from cmsplugin_fancybox.models import FancyBoxPlugin
try:
    from tinymce.widgets import TinyMCE
    tinymce_available = True
except: 
    tinymce_available = False

class FancyBoxRichTextPluginForm(forms.ModelForm):
    if tinymce_available:
        popup_text = forms.CharField(widget=TinyMCE())
    class Meta:
        model = FancyBoxPlugin
        exclude = ('target_image', 'target_image_height', 'target_image_width', 'target_image_title',)
        
class FancyBoxImagePluginForm(forms.ModelForm):
    class Meta:
        model = FancyBoxPlugin
        exclude = ('popup_text',)
