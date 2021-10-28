var data_transmit_enable = 1;
function transmitToServer(data){
  if(data_transmit_enable == 1){
    data_transmit_enable = 0;
    $.ajax({
      method: 'POST',
      url: '/add_score/',
      data: data,
      success: function(){
        data_transmit_enable = 1;
      },
      error: function(xhr, status, err){
        console.log("Error " + xhr.status);
        data_transmit_enable = 1;
      }
    });
  }
}