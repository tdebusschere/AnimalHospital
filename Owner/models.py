import datetime
from django.utils import timezone

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.a

class Owner( models.Model ):

    sex_choices = (( 'male','男' ), ('female','女'), ('other','無'))
    offices     = (('changhua','彰化市'),('yuanlin','員林市'))

    owner_id                 =               models.AutoField(unique= True,  primary_key = True )
    owner_name               =               models.CharField(max_length = 20 )
    owner_name_english       =               models.CharField(max_length = 50, blank = True, null = True )
    phone_home               =               PhoneNumberField( blank = True, null = True,  unique = False )
    phone_work               =               PhoneNumberField( blank = True, null = True,  unique = False )
    cellphone1               =               PhoneNumberField( blank = True, null = True,  unique = False )
    cellphone2               =               PhoneNumberField( blank = True, null = True,  unique = False )
    address                  =               models.CharField( max_length = 100, null = False )
    line                     =               models.CharField( max_length = 30, null = True, blank = True )
    facebook                 =               models.CharField( max_length = 60, null = True, blank = True )
    preferred_way_contacting =               models.CharField( max_length = 20, null = True, blank = True )
    birthday                 =               models.DateField( blank = True, null = True)
    gender                   =               MultiSelectField( choices = sex_choices, max_choices = 1, null = True, blank = False )
    preferred_office         =               MultiSelectField( choices = offices, max_choices = 1, null = True, blank = True )
    last_updated_by          =               models.ForeignKey( settings.AUTH_USER_MODEL  , on_delete = models.SET_NULL, null = True )
    updated_at               =               models.DateTimeField( auto_now = True ) 
    created_at               =               models.DateTimeField( auto_now_add = True )
    comment                  =               models.CharField( max_length = 500, blank = True, null = True )

    class Meta:
        db_table = 'owner'
        verbose_name_plural = 'owners'

    def __unicode__(self):
        return self.owner_name

    def get_absolute_url(self):
        return reverse('ownerdetail',args={self.owner_id})

    def clean(self):
        ##check cellphone 
        if self.phone_home is None and  self.phone_work is None and self.cellphone1 is None and self.cellphone2 is None: 
            raise ValidationError(_('需要提供至少一張手機號'))

        if self.birthday is not None:
            if self.birthday > timezone.now():
                raise ValidationError(_('生日不合理') )

            if self.birthday <  timezone.now() - datetime.timedelta(days = 120 * 365) :
                raise ValidationError(_('生日不合理') )

        if not any( char.isalpha() for char in self.address ):
            raise ValidationError(_('地址不合理'))

        if not any( char.isalpha() for char in self.owner_name ):
            raise ValidationError(_('名稱有問題'))


    @property	
    def get_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:
            fname = f.name
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            cvalue = None
            if hasattr(self, get_choice):
                cvalue = getattr(self, get_choice)()
            try:
                value = getattr(self, fname)
            except AttributeError:
                value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :

                fields.append(
                  {
                   'label':f.verbose_name,
                   'name':f.name,
                   'value':value,
                   'cvalue':cvalue
                   }
	          )
        return fields
