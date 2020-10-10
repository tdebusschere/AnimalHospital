from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User, Group

from .forms import OwnerForm, OwnerEditForm
from .models import Owner

import itertools

def get_user( request):
    uid = request.user.id 
    userobj = User.objects.get( id = uid )
    return userobj

class OwnerAdd( FormView ):
    template_name = 'Owner/add.html'
    form_class    = OwnerForm
    success_url   = 'owneradded'

    def get_success_url(self):
        return reverse('owneradded',kwargs = {'pk' : self.object.owner_id })

    def form_valid(self, form):
        n = form.save()
        n.last_updated_by = get_user( self.request )
        n.save()
        self.object = n
        return super( OwnerAdd, self).form_valid( form )

class OwnerAdded( TemplateView ):
    template_name = 'Owner/add_success.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data( **kwargs )
        ctx['object'] = Owner.objects.get( owner_id = self.kwargs['pk'] )
        return ctx

class OwnerEdited( TemplateView):
    template_name = 'Owner/edit_success.html'

class OwnerEdit( FormView ):
    template_name =  'Owner/edit.html'
    form_class    =  OwnerEditForm
    success_url   =  'owneredited'

    def get_initial(self ):
        """Handle GET requests: instantiate a blank version of the form."""
        initial = super( OwnerEdit, self).get_initial()
        identif =  self.kwargs['pk']
        owner   =  Owner.objects.get( owner_id = identif )
        fields  =  owner.get_fields
        for key in  fields:
           initial.update({ key['name']  : key['value']})
        return initial

    def form_valid(self, form):
        n = form.save( commit = False)
        ownerfile = Owner.objects.get(owner_id = self.kwargs['pk'] )
        n.owner_id = ownerfile.owner_id
        n.created_at = ownerfile.created_at
        n.last_updated_by = get_user( self.request)
        n.save()
        return super( OwnerEdit, self).form_valid( form )

class OwnerUnconfirmed( TemplateView ) :
    def get_context_data(self, *args, **kwargs):
            context = super(OwnerUnconfirmed, self).get_context_data(*args, **kwargs)
            users  = User.objects.filter(groups__name = 'AllUsers')
            ids =[  set(Owner.objects.filter(last_updated_by = key))  for key in users ]
            ids = ( set.union(*ids ))
            context['updates'] = ids
            return(context)
    template_name = 'Owner/unconfirmed.html'

class OwnerDetail( DetailView ):
    model = Owner
    template_name='Owner/view.html'
    

class OwnerSearch( TemplateView ):
    template_name = 'home.html'

