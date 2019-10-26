$(document).ready(function(){
    $('form1').submit(function(event){
      event.preventDefault()
      form = $("form1")
  
      $.ajax({
        'url':'/ajax/newsletter/',
        'type':'POST',
        'data':form1.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_your_name').val('')
      $("#id_email").val('')
    }) // End of submit event
  
  }) // End of document ready function