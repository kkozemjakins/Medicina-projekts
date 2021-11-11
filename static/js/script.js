let vizites = []

window.addEventListener('load', () => {
    preces = JSON.parse(localStorage.getItem("vizites") || "[]");
    console.log(vizites)
    render();
});

document.getElementById("pievienotViziti").addEventListener('click', Poga)
function Poga(){
    if (datums.value === ""){
        alert("Jūs neievadijāt vizītes datumu.")
    };
    if (laiks.value === ""){
        alert("Jūs neievadijāt vizītes laiku.")
    } else {
        let vizite = {datums: datums.value, laiks: laiks.value};
        datums.value = "";
        laiks.value = "";
    
        vizites.push(vizite);

        render();
    }

}

function render() {
    let saraksts = document.getElementById('saraksts');
    saraksts.innerHTML = "";

    for(let i = 0; i < vizites.length; i++) {

        let vizite = `
    <li class="vizite">
        <h3>Vizīte: ${vizites[i].datums}</h3>⠀⠀⠀<h4>Laiks: ${vizites[i].laiks}</h4>⠀⠀⠀⠀
        <button class="del">Dzēst</button>
    </li>`;
    saraksts.innerHTML += vizite;
    }

    localStorage.setItem("vizites", JSON.stringify(vizites)) 
}

const list = document.querySelector('#saraksts')

list.addEventListener('click', (e) => {
    if(e.target.className == 'del'){
      const li = e.target.parentElement;
      li.parentNode.removeChild(li);
      vizites.splice(li, 1);
      localStorage.setItem('vizites',JSON.stringify(vizites));
    }
  });