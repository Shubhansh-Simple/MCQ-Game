from django.db                      import models
from PIL                            import Image as Img
from io                             import BytesIO 
from django.core.files.uploadedfile import InMemoryUploadedFile

class CustomResizeImage():
    '''Helper Class - To resize the image in memory with given ratio.'''

    def image_resize( self, image_read, dimensions, image_name ):
        '''Resizing image in memory using PIL then return the modified image'''

        if image_read:
            img            = Img.open( BytesIO( image_read ) )
            
            # png to jpg
            if img.mode in ( 'RGBA','P' ):
                img        = img.convert('RGB')

            img_resize     = img.resize( dimensions )
            modified_image = BytesIO() # image storage memory

            img_resize.save( modified_image , format='JPEG' )

            modified_image.seek(0)

            return InMemoryUploadedFile(
                    modified_image,
                    'ImageField',
                    "%s.jpg" %image_name,
                    'image/jpeg',
                    modified_image.getbuffer().nbytes,
                    None
                )        
        else:
            return None


class QuestionManager( models.Manager ):
    
    @property
    def total_questions( self ):
        return Question.objects.all().count()

    @property
    def passing_pushes( self ):
        '''Decides the passing marks'''

        return round( self.total_questions - self.total_questions/4 )



class Numbering( models.Model ):
    '''For re-arranging the question order in future'''

    question_number = models.PositiveIntegerField()
    
    def __str__( self ):
        return str( self.question_number )


class Question( models.Model,CustomResizeImage ):
    '''Kbc like question model - Question title and Option as images.'''

    ANSWER = ( 
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
        )

    question_number    = models.OneToOneField( Numbering ,
                                               on_delete=models.CASCADE ,
                                               help_text='Question number can\'t be repeated.'
                                             )

    question_image     = models.ImageField( upload_to='question_pic/',
                                            help_text='Image shows with question.',
                                            null=True,
                                            blank=True 
                                          )

    question_title     = models.CharField( max_length=200 ,help_text='Title of the question')

    option_one_image   = models.ImageField( upload_to='option_pics/', help_text='Option one image' )
    option_two_image   = models.ImageField( upload_to='option_pics/', help_text='Option two image' )
    option_three_image = models.ImageField( upload_to='option_pics/', help_text='Option three image' )
    option_four_image  = models.ImageField( upload_to='option_pics/', help_text='Option four image')
    
    answer             = models.CharField( max_length=1,
                                            choices=ANSWER,
                                            help_text='Enter right answer - A,B,C,D'
                                         )

    objects = QuestionManager()


    @property
    def total_questions_list( self ):
        '''Return a (counting list of total questions +1) starts with 0''' 

        return list( range( Question.objects.total_questions + 1 ) )


    def save( self,*args,**kwargs ):
        '''Resize image before saving.'''

        if not self.answer.isupper():
            self.answer = self.answer.upper()

        if self.question_image:

            '''Since it's optional'''

            self.question_image = self.image_resize( self.question_image.read(),
                                                     (200,200) ,
                                                     self.question_image.name 
                                                   )

        self.option_one_image   = self.image_resize( self.option_one_image.read(),
                                                     (100,100),
                                                     self.option_one_image.name 
                                                   )

        self.option_two_image   = self.image_resize( self.option_two_image.read(),
                                                     (100,100),
                                                     self.option_two_image.name 
                                                   )

        self.option_three_image = self.image_resize( self.option_three_image.read(),
                                                     (100,100),
                                                     self.option_three_image.name 
                                                   )
        self.option_four_image  = self.image_resize( self.option_four_image.read(),
                                                     (100,100),
                                                     self.option_four_image.name 
                                                   )
        
        super().save( *args,**kwargs )


    def __str__( self ):
        return str( self.question_number ) + '.) ' + str( self.question_title )


