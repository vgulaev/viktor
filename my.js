function doPress( ) {
    alert( "I'm interactiv work" )
    $.ajax(
        {
            url: "/ws/getfilters",
            type: "POST",
            dataType: "json",
            data: {
                "filter" : $( "#param" ).val()
            }
        })
    .done(function ( data ) {
        alert("Some body alive");
        });

}