from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from Pet.forms import PetForm, PetEditForm
from .models import Pet
from Owner.models import Owner

def get_user( request):
    return request.user.id 

class PetAdd( FormView ):
    template_name =  'Pet/add.html'
    form_class    =  PetForm
    success_url   =  'petadded'

    def form_valid(self, form):
        print( form)
        form.instance.last_updated_by = get_user( self.request )
        print( form )
        return super( PetEdit, self).form_valid( form )

class PetAddOwner ( FormView ):
    template_name =  'Pet/add.html'
    form_class    =  PetForm
    success_url   =  'petadded'
    
    def form_valid(self, form):
        print( form)
        form.instance.last_updated_by = get_user( self.request )
        print( form )
        return super( PetEdit, self).form_valid( form )


class PetAdded( TemplateView ):
    template_name = 'Pet/add_success.html'

class PetEdited( TemplateView):
    template_name = 'Pet/edit_success.html'

class PetEdit( FormView ):
    template_name =  'Pet/edit.html'
    form_class    =  PetEditForm
    success_url   =  'petedited'

    def form_valid(self, form):
        print( form)
        form.instance.last_updated_by = get_user( self.request )
        print( form )
        return super( PetEdit, self).form_valid( form )

class PetUnconfirmed( TemplateView ) :
    template_name = 'home.html'

class PetSearch( TemplateView ):
    template_name = 'home.html'

