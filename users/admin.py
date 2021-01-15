from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin

from .forms                     import CustomUserChangeForm , CustomUserCreationForm
from .models                    import CustomUser

class CustomUserAdmin( UserAdmin ):
    '''Show extra fields to the AdminSite.'''

    add_form      = CustomUserCreationForm
    form          = CustomUserChangeForm
    model         = CustomUser
    
    # For seeing extra fields.
    UserAdmin.fieldsets += ( 'Additional Info',
                             {'fields' :  ( 'profile_pic',
                                            'correct_answers',
                                            'winning_prize',
                                            'skip_question',
                                            'is_complete_quiz' 
                                          ), 
                             }
                           ),

admin.site.register( CustomUser,CustomUserAdmin )




















