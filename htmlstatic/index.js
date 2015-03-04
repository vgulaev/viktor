function make_out () {
    var el = document.getElementById( "Out" );
    el.innerHTML = "I'm work";
    
    bt = document.getElementById( "BtMain" );
    bt.innerHTML = "Pres me more";
    bt.style.position = "absolute";
    bt.style.top = bt.style.top + 40 + "px";
    bt.onmouseover = function() {
        //var bt = document.getElementById( "BtMain" );
        var y = parseInt( bt.style.top );
        if (y > 400) {
            bt.style.top = parseInt( bt.style.top ) - 40 + "px";
        }
        else {
            bt.style.top = parseInt( bt.style.top ) + 40 + "px";
        }
    }
}

