from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )

'''
class MyUserManager( BaseUserManager):
    def create_user( self, login, email, date_of_birth, name, password = None, role = None):
        if not email:
            raise ValueError('請提供電子郵件')
        if not email:
            raise ValueError('請提供中文名字')
        if not login:
            raise ValueError('請用y英文字打會員帳號')

        user = self.model(
                login = login,
                email = self.normalize_email(email),
                date_of_birth = date_of_birth,
                name = name,
                )
        
        user.set_password( password)
        user.save( using= self._db)
        return user



    def create_superuser( self, login, email, date_of_birth, name, password = None, role = None):
        if not email:
            raise ValueError('請提供電子郵件')
        if not email:
            raise ValueError('請提供中文名字')
        if not login:
            raise ValueError('請用英文字打會員帳號')

        user = self.model(
                login = login,
                email = self.normalize_email(email),
                date_of_birth = date_of_birth,
                name = name,
                password = password,
                )
        
        user.is_admin = True
        print( user )
        user.save( using= self._db)
        return user


class MyUser( AbstractBaseUser):
    login = models.CharField( 
            verbose_name = "User Login", max_length = 50,
            unique = True,
            ) 
    email = models.EmailField(
            verbose_name = 'User Email',
            max_length = 255,
            unique = True,
            )
    
    date_of_birth = models.DateField()
    registered    = models.DateField( auto_now_add = True )
    name = models.CharField(
            verbose_name ='User Name',
            max_length = 50,
            unique = True,
            )
    role_choices = (( None , 'None'),('Vet' , '獸醫') , ('Vet Assistant' ,  '助理' ))
    role = models.CharField(
            verbose_name = 'User Role',
            max_length = 20,
            choices = role_choices )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email','date_of_birth','name']


    def __str__(self):
        return self.login

    def has_perm(self, perm, obj = None):
        return True


    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin
'''
