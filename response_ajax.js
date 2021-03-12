function onloadd(){
    var area = document.getElementById("text");
    var space = "";
    var lst_line = ""
    area.addEventListener("keyup", function(event) {
        var snip = document.getElementById("text").value.split("\n")
        var lenth = snip.length
        if (event.key == ":") {
            space = space + "\t";
            console.log(lst_line);
        }

        if (event.keyCode === 13) {
            // lst_line = snip[lenth-2];
            // tabs = lst_line.split("\t").length - 1;
            // console.log(tabs,space.length-1);
            // if (tabs != space.length-1){
            //     space = "\t".repeat(space.length-tabs);
            // }
            var txt = document.getElementById("text");
            //txt.value += space;
        }
        if (event.keyCode == 9) {
            event.preventDefault();
        }
    });
}


function runit(){
    code = document.getElementById("text").value;
    var xhttp = new XMLHttpRequest();
    console.log(code);
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText
        }
    }
    xhttp.open("GET","run?code="+encodeURIComponent(code),true);
    xhttp.send();
    }
