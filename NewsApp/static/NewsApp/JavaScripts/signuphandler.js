function NewUserHandler(event) {
    //var csrf = "input[name=csrfmiddlewaretoken]";
    event.preventDefault(); 

    console.log($("[name = username_inp]").val().length == 0);
    
    if(($("[name = firstname_inp]").val().length == 0) || ($("[name = lastname_inp]").val().length == 0) || ($("[name = username_inp]").val().length == 0) || ($("[name = password_inp]").val().length == 0) || ($("[name = email_inp]").val().length == 0) || ($("[name = dob_inp]").val().length == 0)){
        alert("Please complete the sign in form without leaving any blank inputs.");
        return false;
    }
        

    PostData = $(this).serialize();
    console.log(PostData);

    $.ajax({
            type: "POST",
            url:  "register/", 
            dataType: "json",
            data: PostData,
            success: function(Response){
                console.log(Response);
                
                if (Response.Success == 'T'){
                    $('#SignUpFormDiv').replaceWith(
                        "<h3 id='SuccessMessage'>Successfully signed up!</h3>"
                    );
                    $('#SuccessMessage').fadeOut(5000, function(){
                        location.replace("/");
                    });
                }

                else {
                    if(Response.Issue == 'Username Taken'){
                        $('#ErrorMessages').text("The username that you selected is already in use. Please select a different username.");
                    }
                    else {
                        $('#ErrorMessages').text("Invalid Submission: The form is misisng infromation!");
                    }
                }
            }
        });
    }