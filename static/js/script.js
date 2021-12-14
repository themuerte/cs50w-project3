
function changeSelect(){
    var cant_toppings = document.querySelector("#cant_toppings")
    var toppings = document.querySelector("#toppings")
    toppings.innerHTML = "";

    for (let index = 0; index < cant_toppings.selectedIndex; index++) {
        toppings.innerHTML =  ` 
        <select class="form-select" aria-label="Default select example" id="cant_toppings" onChange="cant_toppings">
            <option selected>Open this select menu</option>
            {% for pro in product %}
                {% if pro.price_2 is null %}
                    <option>{{ pro.name }}</option>
                {% endif %}
            {% endfor %}
        </select>
        `
    }
}