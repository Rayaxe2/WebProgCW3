function LogInUserHandler(event) {
     event.preventDefault(); 
     console.log($("[name = username_inp]").val().length == 0);
     
     if(($("[name = username_inp]").val().length == 0) || ($("[name = password_inp]").val().length == 0)){
         alert("Please complete the log in form without leaving any blank inputs.");
         return false;
     }
         
     PostData = $(this).serialize();
     console.log(PostData);
 
     $.ajax({
             type: "POST",
             url:  "Signin/", 
             dataType: "json",
             data: PostData,
             success: function(Response){

                //resume here!
                 console.log(Response);
                 
                 if (Response.Success == 'T'){
                     $('#LogInFormDiv').replaceWith(
                         "<h3 id='SuccessMessage'>Successfully Logged In!</h3>"
                     );
                     $('#SuccessMessage').fadeOut(5000, function(){
                         location.replace("/");
                     });
                 }
                 else {
                     if(Response.Issue == 'Non-Existant Username provided'){
                         $('#ErrorMessages').text("User Does Not Exist.");
                     }
                     else if(Response.Issue == 'Inccorect Password provided') {
                         $('#ErrorMessages').text("Password does not match with username.");
                     }
                     else{
                        $('#ErrorMessages').text("An error occured.");
                     }
                 }
             }
         });
}