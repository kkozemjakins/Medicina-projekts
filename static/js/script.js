let vizites = []

window.addEventListener('load', () => {
    vizites = JSON.parse(localStorage.getItem("vizites") || "[]");
    console.log(vizites)
    render();
});

document.getElementById('pievienotVizite').addEventListener('click', () => {
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
        let vizite = `
        <div class="vizite">
            <h3>Datums: ${vizites[i].datums}</h3>
            <h3>Laiks: ${vizites[i].laiks}</h3>
            <button class="del" onclick='removeViziti("${vizites[i].datums}")'>Dzēst</button>
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