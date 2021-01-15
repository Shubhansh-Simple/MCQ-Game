from django.contrib.auth.models import AbstractUser
from django.db                  import models
from question_app.models        import Question


class CustomUser( AbstractUser ):
    '''Add some extra fields to the user model.'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'

    profile_pic      = models.ImageField( upload_to='profile_pic/',
                                          null=True,
                                          blank=True,
                                          help_text='Upload your profile picture' 
                                        )

    correct_answers  = models.PositiveSmallIntegerField( default=0 )
    skip_question    = models.ManyToManyField( Question, blank=True )
    winning_prize    = models.PositiveSmallIntegerField( default=0 )
    is_complete_quiz = models.BooleanField( default=False )

    
    @property
    def total_skip_question( self ):
        return self.skip_question.all().count()

    
    @property
    def increase_correct_answers( self ):
        self.correct_answers += 1

    
    @property
    def increase_winning_prize( self ):
        self.winning_prize += 10

    
    @property
    def is_pregnant( self ):
        '''Check whether whiskey pregnant or not.'''

        if self.correct_answers >= Question.objects.passing_pushes:
            return True
        return False


    def __str__( self ):
        return str( self.username ).capitalize()


