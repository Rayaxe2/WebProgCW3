function NewUserHandler(event) {
    event.preventDefault(); 
    var SubmittedForm = $(this);
    PostData = SubmittedForm.serialize();

    console.log(PostData);

    $.ajax({
            type: "POST",
            url:  "signup/", 
            dataType: "json",
            data: PostData,
            success: function(Response){
                console.log(Response.Success);
                
                if (Response.Success == 'T'){
                    $('#SignUpForm').replacewith(
                        "<h3 id='SuccessMessage'>Successfully signed up!</h3>"
                    );
                    $('#SuccessMessage').fadeOut(2000, function(){
                        location.replace("/mainpage")
                    });
                }
                else {

                }
            }
        });
    }