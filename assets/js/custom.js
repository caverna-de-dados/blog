// CONFIGURAÇÕES
var canonic = $("link[rel='canonical']");

if (canonic.length == 0) {
	$( "head" ).prepend( "<link href='https://cavernadedados.com/' rel='canonical'/>" );
}

$( "header" ).prepend( "<script>var disqus = 'YOUR_DISQUS_SHORTNAME';</script>" );

// AJUSTES DE LAYOUT E DESIGN DAS TAGS 'PRE', USADAS PARA CÓDIGOS
// $( ".hll, .n, .c, .err, .s1, .ss, .bp, .vc, .vg, .vi, .il" ).parent( "pre" ).addClass("pre-style");
// $( ".dataframe" ).parent( "div" ).css( "margin-bottom", "35px" );

// if ($('.pre-style')[0]) {
// } else {
//   $('pre').addClass('pre-style');
// }