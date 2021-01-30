# Custom Mixin To Make Code Clean

from django.shortcuts import redirect

class CustomQuizCompleteMixin:
    '''Redirect if the quiz not complete'''

    def dispatch( self, request, *args, **kwargs ):
        if not request.user.is_complete_quiz:
            return redirect( 'terms_condition' )
        return super().dispatch( request, *args, **kwargs )


