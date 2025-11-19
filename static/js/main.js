
let r = 0;

function grabColors() {

    
    let red_input = document.getElementById("color_stats_r");
    let green_input = document.getElementById("color_stats_g");
    let blue_input = document.getElementById("color_stats_b");

    
    let color_picker_form = document.getElementById("color_pick");
    
    let g = 0;
    let b = 0;

    
    if (color_picker_form != null) {
        console.log("Loaded form");
        color_picker_form = document.getElementById("color_pick").addEventListener('submit', (e) => {
        e.preventDefault()
        console.log(red_input.value);
    }) 
    };

    
    if (red_input) {
        console.log(red_input);
    }
  
}
console.log("Script loaded");
function grabRedColor() {
    let red_input = document.getElementById("color_stats_r");

    red_input.addEventListener("change", (e) => {
        r = e.target.value;
        console.log("red amount: " + r); 
    })
};

function grabGreenColor() {
    let red_input = document.getElementById("color_stats_g");

    red_input.addEventListener("change", (e) => {
        r = e.target.value;
        console.log("red amount: " + r); 
    })
};


function grabRedColor() {
    let red_input = document.getElementById("color_stats_r");

    red_input.addEventListener("change", (e) => {
        r = e.target.value;
        console.log("red amount: " + r); 
    })
};


function grabBlueColor() {
    let red_input = document.getElementById("color_stats_b");

    red_input.addEventListener("change", (e) => {
        b = e.target.value;
        console.log("red amount: " + r); 
    })
};



grabGreenColor();
grabRedColor()
grabBlueColor();
grabColors();

