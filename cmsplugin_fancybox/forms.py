from django import forms
from cmsplugin_fancybox.models import FancyBoxPlugin
from tinymce.widgets import TinyMCE

class FancyBoxRichTextPluginForm(forms.ModelForm):
    popup_text = forms.CharField(widget=TinyMCE())
    class Meta:
        model = FancyBoxPlugin
        exclude = ('target_image', 'target_image_height', 'target_image_width', 'target_image_title',)
        
class FancyBoxImagePluginForm(forms.ModelForm):
    class Meta:
        model = FancyBoxPlugin
        exclude = ('popup_text',)
        
class FancyBoxSnippetPluginForm(forms.ModelForm):
    popup_text = forms.CharField(label="HTML Snippet", widget=forms.Textarea)
    class Meta:
        model = FancyBoxPlugin
        exclude = ('target_image', 'target_image_height', 'target_image_width', 'target_image_title',)

