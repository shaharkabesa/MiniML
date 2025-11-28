    let color_name = document.getElementById("color_name");
    let r = 0;
    let g = 0;
    let b = 0;
            
        let green_input = document.getElementById("color_stats_g");
        let red_input = document.getElementById("color_stats_r");
        let blue_input = document.getElementById("color_stats_b");


    let color_pick = document.getElementById("color_pick");

    color_pick.addEventListener("submit", (e) => {
        e.preventDefault()
    })
    
  function previewColors() {


        green_input.addEventListener("input", (e) => {
            g = e.target.value;
            console.log("red amount: " + g);
            changeColorBox(r,g,b); 
        })
        
        red_input.addEventListener("input", (e) => {
            r = e.target.value;
            console.log("red amount: " + g);
            changeColorBox(r,g,b); 
        })
        
        blue_input.addEventListener("input", (e) => {
            b = e.target.value;
            console.log("red amount: " + g);
            changeColorBox(r,g,b); 
        })

        
    }

    function createColorObject(r,g,b,color_name) {
        let color_data = {
            red_color: r,
            green_color: g,
            blue_color: b,
            color_name: color_name
        };

        color_data = JSON.stringify(color_data); 
        localStorage.setItem("color_data", color_data);
        console.log("Color uploaded to localstorage");

    }

    function changeColorBox(r,g,b) {

        if (color_box) {
            color_box.style.backgroundColor = (`rgb(${r},${g},${b})`);
        }
    }


function handleResearchButton() {

    color_name = color_name.value;
    if(color_name) {
        let researchbtn = document.getElementById("startResearch");
        researchbtn.addEventListener("click", (e) => {
        
        
     
        createColorObject(r,g,b, color_name);
            

    });
    }
    
}

function clearData(){
        green_input.value = "";
        red_input.value = "";
        blue_input.value = "";
        color_name.value = "";
        
} 

clearData();
previewColors();
handleResearchButton();
