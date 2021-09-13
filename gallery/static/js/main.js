
// Retrieve data for individual images in modal// url:"{% url 'getUsers' 7 %}",url:"load/",
function populateForm(id) 
  {

  $(document).ready(function()
  {
  n 
      var urls=`${window.location.origin}/load/${id}/`

        $.ajax({
          type:'GET',
          
          url:urls,
          success: function(response)
          {
           data=JSON.parse(response.users)
           $('#location').text(data.location);
              $('.name').text(data.image_name);
              $('.date').text(data.pub_date);
              $('.description').text(data.description);
              $("#image").attr("src",data.image);
         
              $('.myInput').val(data.image);
                     
          },

          error: function(response)
          {
            alert('No data Found')
          }

        });
      // },100000);
  })
  }
// SHow detailson hover
  // $(document).ready(function(){
  // $( "#imageDiv" ).mouseenter(function() 
  // {
  //     var closestImage = $(this).closest("#imageDiv");
  //     closestImage.next("#locationDiv").slideDown(100);
  //   })
  //   .mouseleave(function() {
  //     $("#locationDiv" ).hide();
  // });
  // });

// Copy Function
      function myFunction() 
      {
          var copyText = document.getElementsByClassName("myInput")[0];
          copyText.select();
          copyText.setSelectionRange(0, 99999); 
          navigator.clipboard.writeText(copyText.value);
          alert("Copied the text: " + copyText.value);
        }

  // picking Location 
  $(document).ready(function()
    {
      $("#g-btn").click(function(){
        $("#general").fadeIn();
        $("#Eldoret").fadeOut();
        $("#Mombasa").fadeOut();
        $("#Nairobi").fadeOut();
      });
    });

    $(document).ready(function()
    {
      $("#e-btn").click(function(){
        $("#general").fadeOut();
        $("#Eldoret").fadeIn();
        $("#Mombasa").fadeOut();
        $("#Nairobi").fadeOut();
      });
    });

    $(document).ready(function()
    {
      $("#n-btn").click(function(){
        $("#general").fadeOut();
        $("#Eldoret").fadeOut();
        $("#Mombasa").fadeOut();
        $("#Nairobi").fadeIn();
      });
    });
    
    $(document).ready(function()
    {
      $("#m-btn").click(function(){
        $("#general").fadeOut();
        $("#Eldoret").fadeOut();
        $("#Mombasa").fadeIn();
        $("#Nairobi").fadeOut();
      });
    });

