// crating vapables for each consent i made in css
const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    modeSwtich = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");

    //this is for the menu extender
    toggle.addEventListener("click", () =>{
        sidebar.classList.toggle("close");
    });
    //this is to change the whole apracne of the website to dar or light mode
    modeSwtich.addEventListener("click", () =>{
        body.classList.toggle("dark");
   
        //this changes the text to the corrosponding mode colour next to the buttion to switch the colour.
        if(body.classList.contains("dark")){
            modeText.innerText = "Light Mode"
        }else{
            modeText.innerText = "Dark Mode"
        }
    });
    
