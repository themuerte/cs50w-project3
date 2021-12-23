# Project 3

# Pizza Web50x.ni
Es un sitio web donde se puede ordenar comidas con multiple opciones

## Instalacion
- comprobar si esta instalado el: `pipenv`
- colocarse dentro del directorio: `cs50w-project3/`
- ejecutar el comando: `pipenv install Pipfile`
- ejecutar el comando: `pipenv shell`

## Paginas
- La primera pagina que tendiramos que es la de generar una orden, en esta pagina tambien veremos una barra de navegacion tendremo la opcion del carrito de compra que nos redigira a las ordenes
- En la vista del carrito o del ordene tendremos como no las ordenes activas las cuales son las que estamos agregando items, las ordenes que esamos esperando que finalice y las ordenes que ya estan finalizadas. En las ordenes activas podremos eliminar, agragar y actulizar el item, tambien en la orden podras confirmar esta que pasara de acitva a espera
- Cuando creamos una nueva orden esta nos diregira a la pagina de menu y en esta pagina de orden desaparecera la orden hasta que esta este activa y hasta que se confirme y pase a epera se podra genrar nuevas ordenes
- El admin se podra agragar nuevos productos y tambien eliminar y actualizarlos. Para agragar nuevos productos se tiene que redirigir a la opcion de `MenuItem -> Añadir` una vez estando ahi la primera opcion que tnedremos es la categoria que queremos agragar que son las de `pizza, pasta, ensaldas, etc`, luego podemos agragar el nombre, despues tenemos lo que son los precios y hay dos `price_1 y price_2` que el primero se refiere al precio normal o en el caso de que tenga tamaño el plato, topping, etc es el pequeño y el price_2 hace referencia al tamaño largo.
- Otra venta es la de `Administracion de ordenes` que esta solo puede acceder los usuarios que son administradores, en esta se pude ver las ordenes pendientes las cuales se pueden finalizar ahi y las ordenes pasadas

## Mi toque personal
- Historial de ordenes 
- Eliminar ordenes activas
