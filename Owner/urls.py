from django.urls import path

from . import views
from AnimalHospital import settings

urlpatterns = [
                #path('ownerdetail/<id:owner_id>', views.OwnerDetail.as_view(), name='ownerdetail')
                path('owneradd',            views.OwnerAdd.as_view()        , name = 'owneradd'),
                path('owneradded:<int:pk>', views.OwnerAdded.as_view()      , name = 'owneradded' ),
                path('owneredit:<int:pk>',  views.OwnerEdit.as_view()       , name = 'owneredit' ),
                path('owneredited',         views.OwnerEdited.as_view(  )   , name = 'owneredited'),
                path('ownerunconfirmed',    views.OwnerUnconfirmed.as_view(), name = 'ownerunconfirmed'),
                path('ownersearch',         views.OwnerSearch.as_view()     , name = 'ownersearch'),  
                path('ownerdetail/<int:pk>',views.OwnerDetail.as_view()     , name = 'ownerdetail'),
              ]
