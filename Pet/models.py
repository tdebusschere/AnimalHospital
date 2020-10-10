import datetime
from django.utils import timezone

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.a
from Owner.models import Owner


class Pet ( models.Model ):

    sex_choices = (( 'male','男' ), ('female','女'))
    neutered_choices = (('yes', 'yes'), ('no','no'), ('unknown','unknown'))

    pet_id                   =               models.AutoField( unique = True, primary_key = True )
    pet_name                 =               models.CharField( max_length = 100,null = True )
    species                  =               models.CharField( max_length = 30, null = False )
    breed                    =               models.CharField( max_length = 30, null = True, blank = True )
    birthday                 =               models.DateField( null = True )
    alive                    =               models.BooleanField( default = True )
    death_day                =               models.DateField( null = True, blank = True )
    sex                      =               MultiSelectField( choices = sex_choices, max_choices = 1 )
    neutered                 =               MultiSelectField( choices = neutered_choices, max_choices = 1 )
    weight                   =               models.DecimalField( max_digits = 6, decimal_places = 2 )
    blood_type               =               models.CharField( null = True, max_length = 2, blank = True ) 
    colour                   =               models.CharField( max_length = 100 )
    temper                   =               models.CharField( max_length = 500, blank = True, null = True )
    allergies                =               models.CharField( max_length = 500, blank = True, null = True )
    preconditions            =               models.CharField( max_length = 500, blank = True, null = True )
    other_pets               =               models.CharField( max_length = 100, blank = True, null = True )
    other_id                 =               models.CharField( max_length = 100, blank = True, null = True )
    hospital_id              =               models.CharField( max_length = 100, blank = True, null = True )
    first_visit              =               models.DateTimeField( null = True, blank = False)
    last_updated             =               models.DateTimeField( auto_now = True, blank = False )
    last_edited_by           =               models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True )
    pet_picture              =               models.FileField( upload_to = 'documents' ) 
    comment                  =               models.CharField( max_length = 500, blank = True, null = True )

    class Meta:
        db_table = 'pet'
        verbose_name_plural = 'pets'

    def __unicode__(self):
        return self.pet_name

    def get_absolute_url(self):
        return reverse('petdetail',args={self.owner_id})

    def clean(self):
        ##check cellphone 
        if self.first_visit is not None:
            if self.first_visit > timezone.now():
                raise ValidationError(_('第一次參與時間不合理'))
            if self.first_visit < timezone.now() - datetime.timedelta( days = 120 * 365):
                raise ValidationError(_('第一次參與時間不合理'))


class PetOwner( models.Model ):

   link_id               = models.AutoField( unique = True, primary_key = True )
   owner_id              = models.ForeignKey( Owner, on_delete = models.SET_NULL, null = True )
   pet_id                = models.ForeignKey( Pet,   on_delete = models.SET_NULL, null = True )
   last_updated          = models.DateTimeField( auto_now = True )
   active                = models.BooleanField( default = True )
   comment               = models.CharField( max_length = 500, blank = True, null = True )

   class Meta:
    db_table = 'pet_owner'
    verbose_name_plural = 'pet_owners'


