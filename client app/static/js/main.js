var sendRadioButton = document.getElementById("sendRadio");
var messageIDField = document.getElementById("messageID");
var alertBox = document.getElementById("alertBox");
messageIDField.disabled = true;

var textAreaBox = document.getElementById("data")
var submitBtn = document.getElementById("submitBtn")
var form = document.getElementById("form")
var messageID = document.getElementById("messageID");

textAreaBox.addEventListener("input", function (event) {
if (/^[\u0000-\u007f]*$/.test(textAreaBox.value) == false) {
    textAreaBox.setCustomValidity("Only ASCII characters allowed!");
} else {
    textAreaBox.setCustomValidity("");
}
});


$(document).ready( function() { // Wait until document is fully parsed
    $("#form").on('submit', function(e){

        e.preventDefault();

        if (sendRadioButton.checked != true){

            $.get("http://localhost:8080/get", {data: messageID.value} , function(data2){
            // Display the returned data in browser
            textAreaBox.value = data2
            messageID.value = ""
            console.log(data2)
            });
            

        } else {

            var userData = document.getElementById("data").value;

            $.post("http://localhost:8080/post", {data: userData} , function(data2){

            alertBox.style.display = 'inline'

            textAreaBox.value = ""
            alertBox.innerHTML = '<div class="alert alert-success alert-dismissible"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Success!</strong> Message Sent!.</div>'
            
            $("#alertBox").delay(1000).slideUp(500, function() {
                $(this).alert('close');
            });
            // Display the returned data in browser
            console.log(data2)
            });

        }

    });
})


    function EnableDisableTextBox() {
                    
        if (sendRadioButton.checked != true){
            messageIDField.disabled = false;
            textAreaBox.disabled = true;
            textAreaBox.readOnly = true;
            textAreaBox.placeholder = "Your retrieved message will be shown here!!!"
            submitBtn.innerHTML = "Retrieve Data"

            textAreaBox.value = ""
            messageIDField.value = ""

            
        } else {
            messageIDField.disabled = true;
            textAreaBox.disabled = false;
            textAreaBox.readOnly = false;
            textAreaBox.placeholder = "Enter the message to send!!!"
            submitBtn.innerHTML = "Send Data"
            textAreaBox.value = ""
            messageIDField.value = ""

        }

        // messageIDField.disabled = sendRadioButton.checked ? true : false;
        if (!messageIDField.disabled) {
            messageIDField.focus();
        }
}

