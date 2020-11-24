function EmptySignUpFormChecker() {
    $('#SignUpForm').filter(':input').each(
        function(){
            if (! $('#SignUpForm').val()){
                alert("Please complete the sign in form without leaving any blank inputs.");
                return false;
            }
        }
    );
}