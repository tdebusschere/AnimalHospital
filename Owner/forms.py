from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Owner

ofields = ['owner_name','owner_name_english','gender','birthday',\
           'phone_home','phone_work','cellphone1','cellphone2',\
           'address','line','facebook','preferred_way_contacting',\
           'preferred_office']

olabels = {
           'owner_name' : _('姓名'),
           'owner_name_english' : _('英文名'),
           'phone_home':_('電話(宅)'),
           'phone_work':_('電話(公)'),
           'cellphone1':_('行動電話1'),
           'cellphone2':_('行動電話2'),
           'address':_('住址'),
           'line':_('Line'),
           'facebook':_('Facebook'),
           'preferred_way_contacting':_('偏好聯絡方式'),
           'preferred_office':_('偏好診療位置'),
           'gender':_('性別'),
           'birthday':_('生日'),
          }


class OwnerForm(ModelForm):

    class Meta:
        model = Owner
        exclude =['comment']
        fields  = ofields 
        labels  = olabels


class OwnerEditForm( ModelForm):
    
    class Meta:
        model = Owner
        ofields.append('comment')
        fields = ofields
        
        olabels['comment'] = _('備註欄')
        labels = olabels

