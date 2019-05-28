$( ".hll, .n, .c, .err, .s1, .ss, .bp, .vc, .vg, .vi, .il" ).parent( "pre" ).addClass("pre-style");
$( ".dataframe" ).parent( "div" ).css( "margin-bottom", "35px" );

if ($('.pre-style')[0]) {
} else {
  $('pre').addClass('pre-style');
}