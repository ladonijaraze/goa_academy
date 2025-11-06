document.getElementById('registrationForm').addEventListener('submit', function(event) {


    if (username && email && password) {
        message.textContent = "რეგისტრაცია წარმატებით დასრულდა!";
        message.style.color = "green";
        
    } else {
        message.textContent = "გთხოვთ შეავსოთ ყველა უჯრა!";
        message.color ="red"
    }
});


