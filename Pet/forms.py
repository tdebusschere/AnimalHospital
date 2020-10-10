from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Pet

from bootstrap_datepicker_plus import DatePickerInput

ofields = ['pet_name','species','breed', 'birthday','alive','sex','neutered', 'weight', \
           'blood_type','colour','temper','allergies','preconditions','other_pets', \
           'other_id', 'first_visit', 'pet_picture']

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


class PetForm(ModelForm):

    class Meta:
        model = Pet
        exclude =['comment']
        fields  = ofields 
        #labels  = olabels
        widgets = {'birthday' : DatePickerInput( format = '%Y-%m-%d' ), 
                   'first_visit' : DatePickerInput( format = '%Y-%m-%d' ), }

class PetEditForm( ModelForm):
    
    class Meta:
        model = Pet
        ofields.append('comment')
        fields = ofields
        
        #olabels['comment'] = _('備註欄')
        #labels = olabels
        widgets = {'birthday' : DatePickerInput( format='%Y-%m-%d' ),
                   'first_visit': DatePickerInput( format='%Y-%m-%d'), }
