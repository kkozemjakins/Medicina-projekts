let vizit = [];

window.addEventListener('load', () => {
    vizit = JSON.parse(localStorage.getItem("vizit") || "[]");
    console.log(vizit)
    render();
});

document.getElementById('pievienotViziti').addEventListener('click', () => {
    POP_UP.style.display = 'none';

    let spisokVizitov = {datums: datums.value, laiks: laiks.value};

    datums.value = "";
    laiks.value = "";

    vizit.push(spisokVizitov);

    render();
})

function render() {
    let biblioteka = document.getElementById('biblioteka');
    biblioteka.innerHTML = "";

    for(let i = 0; i < vizit.length; i++) {
        let spisokVizitov = `
        <div class="pisokVizitov">
            <h3>Datums: ${vizit[i].datums}</h3>
            <h4>Laiks: ${vizit[i].laiks}</h4>
            <button onclick='removeBook("${vizit[i].datums}")'>Dzēst</button>
        </div>`;

        biblioteka.innerHTML += spisokVizitov;
    }

    localStorage.setItem("vizit", JSON.stringify(vizit))
}


function removeBook(spisokVizitov){
    for(let i = 0; i < vizit.length; i++) {
        if( === vizit[i].virsraksts){
            delete vizit)[i];
            break;
        }
    }

    vizit = vizit.filter(function (e) {return e != null;});

    localStorage.setItem("vizit", JSON.stringify(vizit))
    render();
}