$(document).ready(function(){
    $('#userSelector').change(function(){
        $(".usersType").hide(); 
        $('#' + $(this).val()).show();
    });  
    
 // Submit post on submit
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")   
        var fname = $("#nombre").val();
        var lname = $("#apellido").val();
        var uname = $("#usuario").val();
        var tuser = $("#userSelector").val();
        
        console.log("Nombre: "+fname);
        console.log("Apellido: "+lname);
        console.log("Usuario: "+uname);
        console.log("Tipo de usuario: "+tuser);
        
        if( fname != "" && lname != "" ){
	        $.ajax({
	        	url:'registro/',
	        	type:'GET',
	        	data:{nombre:fname,apellido:lname,usuario:uname,tipousuario:tuser},
	        	success:function(response){
	        		if(response == " "){
	        			alert("Vacio!!");
	        		}else{
	        			fullName = response;
	        			alert(fullName);
	        			window.location = 'mensaje/?fname='+fullName;
	        		}
	        	}
	        });
        }else{
        	alert("Nombre y Apellido Obligatorios!!");
        }
    });
});  