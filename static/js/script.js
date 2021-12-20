

document.addEventListener("DOMContentLoaded", () =>{
    const cant_toppings = document.querySelector("#cant_toppings")
    const toppings = document.querySelector("#toppings")

    toppings.addEventListener("change", () => {
        if (toppings.length > cant_toppings.selectedIndex){
            alert("Cantidad de topinngs ")
        }
        console.log("si funciona")
    })
})