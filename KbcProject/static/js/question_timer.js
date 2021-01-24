document.addEventListener('DOMContentLoaded', function(){

    // we wait for this seconds to skip the question
    var time=30;
    var timer_variable = setInterval( function(){

       if (time <= 0){
         clearInterval( timer_variable );
         document.getElementById('skip_button_id').click() 
       }

       document.getElementById('timer_count').innerHTML=time
       time -= 1

    },1000 );
  },false
)







