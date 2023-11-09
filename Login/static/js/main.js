$(document).ready(function() {
    // $("#pj").hide()
    // $("#pf, #pj").hide()
    $("#form_cad_cliente").hide()
});


$('#selecionado').change(function () {
    var selectedValue = $(this).val();
    if(selectedValue == "1")
    {
        $("#form_cad_cliente").show()

        $("#razaosocial").hide()
        $("#cnpj").hide()
        $("#inscestadual").hide()

        $("#nome").show()
        $("#cpf").show()

        $("input[name=tipo]").val('1');

    }else if( selectedValue == "2")
    {
        $("#form_cad_cliente").show()

        $("#nome").hide()
        $("#cpf").hide()

        $("#razaosocial").show()
        $("#cnpj").show()
        $("#inscestadual").show()

        $("input[name=tipo]").val('2');


        //reseta todos os campos do form
        // $('#pf input').each(function(){
        //     $(this).val('');
        // });
    }
    console.log(selectedValue);
});

$('#btn_cep').click(function(){

    var cep  = $("input[name=cep]").val().replace(/[^0-9]/g, '');

    console.log($("input[name=cep]").val())
    var url = 'https://viacep.com.br/ws/'+cep+'/json/';
            $.ajax({
                    url: url,
                    dataType: 'jsonp',
                    crossDomain: true,
                    contentType: "application/json",
                    success : function(json){
                        console.log(json.logradouro)
                        console.log(json)
                        if(json.logradouro){
                            $("input[name=rua]").val(json.logradouro);
                            $("input[name=bairro]").val(json.bairro);
                            $("input[name=cidade]").val(json.localidade);
                            $("input[name=uf]").val(json.uf);
                        }
                    }
            });
    console.log(cep)
})

