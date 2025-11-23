let startResearchButton = document.getElementById("startResearch");


startResearchButton.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("started research");
    startResearch();
})




function startResearch() { 
    const url = "http://127.0.0.1:5000/startResearch"
    const color_data = {
        red: 255,
        blue: 255,
        green : 255,
        color_name: "white"
    }

    try {
        
        const response = await fetch(url, {
            method : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(color_data);
        });
        if(!response.ok) {
            throw new Error("Response status:" + response.status);
        }
        const json = await response.json();
        console.log(json);
    } catch (e) {
        console.error(`Error: ${e}`)
    } 
}