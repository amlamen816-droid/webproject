function requestCar(car) {
    document.getElementById("carName").value = car;
    document.getElementById("requestForm").style.display = "block";
    document.getElementById("confirmation").style.display = "none";
}

function confirmRequest() {
    let name = document.getElementById("name").value.trim();
    let phone = document.getElementById("phone").value.trim();

    if(name === "" || phone === "") {
        alert("⚠️ يرجى إدخال الاسم ورقم الهاتف");
        return;
    }

    document.getElementById("requestForm").style.display = "none";
    document.getElementById("confirmation").style.display = "block";
}


        