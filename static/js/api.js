function startResearch() {

    let startResearchButton = document.getElementById("startResearch");

    startResearchButton.addEventListener("click", function(event) {
            let color_data = localStorage.getItem("color_data");
            color_data = JSON.parse(color_data);
            if(color_data) {
            console.log(`Color data : ${color_data}`);
                console.log("data is valid");
                        axios.post('http://127.0.0.1:5000/research', color_data)
        .then(function (response) {
            // console.log(response);
        })
        .catch(function (error) {
            // console.log(error);
        });

    } else {
        alert("You didn't put colors and name please fill it");
        return;
    }


            });


}

startResearch();