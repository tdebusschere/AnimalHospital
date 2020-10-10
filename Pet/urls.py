from django.urls import path

from . import views
from AnimalHospital import settings

urlpatterns = [
                #path('Petdetail/<id:Pet_id>', views.PetDetail.as_view(), name='Petdetail')
                path('petadd',               views.PetAdd.as_view()        , name = 'petadd'),
                path('petaddowner:<int:pk>', views.PetAddOwner.as_view()   , name = 'petaddowner'),
                path('petadded',             views.PetAdded.as_view()      , name = 'petadded' ),
                path('petedit:<int:pk>',     views.PetEdit.as_view()       , name = 'petedit' ),
                path('petedited',            views.PetEdited.as_view(  )   , name = 'petedited'),
                path('petunconfirmed',       views.PetUnconfirmed.as_view(), name = 'petunconfirmed'),
                path('petsearch',            views.PetSearch.as_view()     , name = 'petsearch'),   
              ]
