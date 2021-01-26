/*
  * Js file specially for question template
  * checks whether the user refresh / go to next question
  * refresh       - don't change the timer
  * next question - timer starts with initial state
  *
  *
*/
function removeKey(){
  // reset the localStorage's value
  //
  try{
    localStorage.setItem( 'question_id_key', current_question_id )
    localStorage.setItem( 'timer_value_key', 30 )
  } catch ( e ) {
    // do sometihng here if it's fail
    // redirect to the error page.
  }
}


document.addEventListener('DOMContentLoaded', function(){
  
  current_question_id = document.getElementById('question_number_id_html').innerText 
  
  if ( localStorage.getItem('question_id_key') 
       && 
       localStorage.getItem('timer_value_key')  ){
     // Storage exist then,

     if ( localStorage.getItem('question_id_key') !==  current_question_id ){
       // user redirect to another question
       // we are updating the localStorage value
       removeKey();
     }
  }
  else{
    // creating localStorage
    removeKey();
  }

  // we wait for this seconds to skip the question
  var time = localStorage.getItem('timer_value_key');

  var timer_variable = setInterval( function(){
     // in every 1000 milliseconds this section executes
     //
     if (time <= 0){
       clearInterval( timer_variable );
       removeKey();
       document.getElementById('skip_button_id').click();
     }

     document.getElementById('timer_count').innerHTML=time
     time -= 1
     localStorage.setItem( 'timer_value_key',time );

  },1000 );

 },false // function ends
)  // DOMContentLoaded ended





