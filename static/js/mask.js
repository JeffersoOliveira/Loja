$(function(){
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.mask-cep').mask('00000-000');
    $('.mask-fone').mask(SPMaskBehavior, spOptions);

    
})

var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };


 
  $('#selecBusca').change(function () {
    var valorSelecionado = $(this).val();
    console.log(valorSelecionado)
    if(valorSelecionado == "1"){
      $('#pesquisa')
        .val('')
        .attr({placeholder:"Insira um CPF",maxlength :"14"})
        .removeClass( "mask-cnpj" )
        .toggleClass( "mask-cpf" )
    }
    else if(valorSelecionado == "2"){
      $('#pesquisa')
      .val('')
      .attr({placeholder:"Insira um CNPJ",maxlength :"18"})
      .removeClass( "mask-cpf" )
      .toggleClass( "mask-cnpj" )
    }
    
    else if(valorSelecionado == "3"){
      $('#pesquisa')
      .val('')
      .attr({placeholder:"",maxlength :"18"})
      .removeClass( "mask-cpf" )
      .removeClass( "mask-cnpj" )
    }
 
  })