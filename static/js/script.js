let vizites = []

current_user_name = localStorage.getItem('Current User Name');

document.getElementById("username_lapā").innerHTML = current_user_name;


window.addEventListener('load', () => {
    vizites = JSON.parse(localStorage.getItem("vizites") || "[]");
    console.log(vizites)
    render();
});

document.getElementById('pievienotViziti').addEventListener('click', () => {
    let vizite = {datums: datums.value, laiks: laiks.value};

    datums.value = "";
    laiks.value = "";

    vizites.push(vizite);

    render();
})

function render() {
    let saraksts = document.getElementById('saraksts');
    saraksts.innerHTML = "";

    for(let i = 0; i < vizites.length; i++) {
        let datums = vizites[i].datums
        let laiks = vizites[i].laiks
        let vizite = `
        <div class="vizite">
            <h3>Datums: ${datums}</h3>
            <h3>Laiks: ${laiks}</h3>
            <button class="del" onclick='removeViziti("${datums}")'>Dzēst</button>
            <a href="/lapa_priekš_drukāšanai"><button class="dru" onclick='drukat("${datums}","${laiks}")'>Drūkat</button></a>
        </div>`;

        saraksts.innerHTML += vizite;
    }

    localStorage.setItem("vizites", JSON.stringify(vizites))
}


function removeViziti(vizite){
    for(let i = 0; i < vizites.length; i++) {
        if(vizite === vizites[i].datums){
            delete vizites[i];
            break;
        }
    }

    vizites = vizites.filter(function (e) {return e != null;});

    localStorage.setItem("vizites", JSON.stringify(vizites))
    render();

    
}



function drukat(datums, laiks){
    StorageDatums = window.localStorage;

    localStorage.setItem("datums", datums);
        
    localStorage.setItem("laiks", laiks);
    
}
