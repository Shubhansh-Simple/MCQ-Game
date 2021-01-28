from django.contrib.auth.models import AbstractUser
from django.db                  import models
from question_app.models        import Question,CustomResizeImage


class CustomUser( AbstractUser,CustomResizeImage ):
    '''Add some extra fields to the user model.'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'

    profile_pic      = models.ImageField( upload_to='profile_pic/',
                                          null=True,
                                          blank=True,
                                          help_text='Upload your profile pic in (png/jpg format only)' 
                                        )

    correct_answers  = models.PositiveSmallIntegerField( default=0 )
    winning_prize    = models.PositiveSmallIntegerField( default=0 )
    is_complete_quiz = models.BooleanField( default=False )


    @staticmethod
    def hide_special_user():
        '''Returns is_staff and endswith _demo'''

        return CustomUser.objects.filter( is_staff=False ).exclude( username__endswith='_demo' )

    @staticmethod
    def whose_quiz_complete():
        '''All non-special user whose quiz complete for plotting'''
        
        # how to use staticmethod into another within class
        return __class__.hide_special_user().filter( is_complete_quiz=True )


    @property
    def increase_correct_answers( self ):
        '''Increase correct_answers by 1'''
        self.correct_answers += 1

    
    @property
    def increase_winning_prize( self ):
        '''Increase winning_prize by 10'''
        self.winning_prize += 10

    
    @property
    def is_pregnant( self ):
        '''Check whether whiskey pregnant or not.'''

        if self.correct_answers >= Question.objects.passing_pushes:
            return True
        return False

   
    def save( self,*args,**kwargs ):
        '''Resize profile_pic before saving.'''

        if self.profile_pic:
            '''Since it's optional'''

            self.profile_pic = self.image_resize( self.profile_pic.read(),
                                                     (200,200) ,
                                                     'profile_picture.jpg' 
                                                )
        super().save( *args,**kwargs )


    def __str__( self ):
        return str( self.username ).capitalize()


class Contributor( models.Model ):
    '''Who contributes this project'''

    first_name  = models.CharField( max_length=50 )
    last_name   = models.CharField( max_length=50 )
    talent      = models.CharField( max_length=50 )
    about       = models.CharField( max_length=200,\
                                    help_text ='How it\'s contribute to this project')
    email       = models.EmailField()

    profile_pic = models.ImageField( upload_to='profile_pic/',
                                          null=True,
                                          blank=True,
                                          help_text='Upload your profile pic\
                                                     in (png/jpg format only)' 
                                   )

    def __str__( self ):
        return self.first_name + ' ' + self.last_name










