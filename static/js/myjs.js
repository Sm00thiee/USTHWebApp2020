function deletePic(){
    var i;
    for (i = 0; i<9; i++){
        var picSrc = document.getElementsByTagName("button")[i].innerHTML;
        if (picSrc == ""){
            var edge = document.getElementsByClassName("col-md-4")[i];
            edge.remove();
            i = i-1;
        }
    }
}