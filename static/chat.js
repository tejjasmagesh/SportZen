    $(document).on('submit','#send__button',function(e)
                   {
      
      e.preventDefault();
      $.ajax({
        type:'POST',
        url:'/',
        data:{
          :$("#todo").val()
        },
        success:function()
        {
          alert('saved');
        }
      })
    });