from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/python")
def hello():
    return """<!Doctype HTML>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        .basic {
            text-align: center;
        }

        .g {
            color : rgb(0,10,255);
        }

        img {
            width : 2%;
            height : 5%;
        }

        .mytext {
            height : 70%;
            width : 70%;
            resize : none;
            background-color: rgb(65, 65, 65);
        }

        .margin {
            margin : 3%;
        }

        body{
            background-color: rgb(34, 32, 32);
        }

        .code{
            background-color: rgb(56, 56, 56);
        }

        .keyword{
            color: rgb(0, 255, 200);
            font-family: 'Courier New', Courier, monospace;
            position: absolute;
            font-size: 13.3px;
            top: 12.6%;
            left: 25.27%;
            z-index: 2;
        }

        textarea{
            color: rgb(220,220,220);
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            border-radius: 0;
            background-color: transparent;
        }

        p{
            color: rgb(220,220,220);
            text-align: center;
            font-family: 'Courier New', Courier, monospace;
        }

        .inp{
            z-index: 1;
        }

        h1{
            color: rgb(140, 150, 150);
        }
    </style>

    <script>
        function onloadd(){
            var area = document.getElementById("text");
            var space = "";
            var lst_line = ""
            area.addEventListener("keyup", function(event) {
                var snip = document.getElementById("text").value.split("\\n")
                var lenth = snip.length
                if (event.key == ":") {
                    space = space + "\\t";
                    console.log(lst_line);
                }

                if (event.keyCode === 13) {
                    // lst_line = snip[lenth-2];
                    // tabs = lst_line.split("\\t").length - 1;
                    // console.log(tabs,space.length-1);
                    // if (tabs != space.length-1){
                    //     space = "\\t".repeat(space.length-tabs);
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
    </script>
</head>


<body onload="onloadd()">
    <div class="basic">
        <h1>Type code</h1>
        <!-- <div class="keyword">
            print
        </div> -->
        <div class="inp">
            <textarea class="mytext" id="text" rows="25">print("Hello! World.")</textarea><br>
            <button onclick="runit()">RUN</button>
        </div>
    </div>

    <div class="basic">
        <div class="margin">
            <textarea class="mytext" id="demo" rows="5">Hello! World.</textarea>
        </div>
    </div>

    <!-- <code contenteditable="true">
        <div class="basic">
            <span style="color: blue">var</span> foo = <span style="color: green">"bar"</span>;
        </div>
    </code> -->
    <p>Created by Ankit Raj Mahapatra</p>
</body>"""





@app.route("/run",methods=["GET"])
def execute():
    code = str(request.args.get("code"))
    #code = code.replace("\n","\\n").replace("\t","\\t").replace("\r","\\r")
    file = open("agent.py","w",encoding="utf-8")
    file.write(code)
    file.close()
    os.system("python executor.py > output.txt")
    data = open("output.txt",encoding="utf-8").read()
    print(data)
    if data != "":
        return data if len(data) <= 4090 else "Output too big, returning first 4000 characters\n"+data[:4000]
    else:
        return "No output statement provided"



