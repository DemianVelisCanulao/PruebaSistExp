
//Funcion de confirmacion de eliminacion de elementos Bodega o Producto
(function(){
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e) =>{
            const confirmacion = confirm('Seguro de eliminar el elemento?')
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    
})();



