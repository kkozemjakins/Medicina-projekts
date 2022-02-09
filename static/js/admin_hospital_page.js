let slimnicas = []

window.addEventListener('load', () => {
    slimnicas = JSON.parse(localStorage.getItem("slimnicas") || "[]");
    console.log(slimnicas)
    render();
});

document.getElementById("pievienotSlimnici").addEventListener('click', Poga)
function Poga(){
    if (nosaukums.value === ""){
        alert("Jūs neievadijāt slimnīcas nosaukumu.")
    };
    if (adrese.value === ""){
        alert("Jūs neievadijāt slimnīcas adresi.")
    } else {
        let slimnica = {nosaukums: nosaukums.value, adrese: adrese.value};
        nosaukums.value = "";
        adrese.value = "";
    
        slimnicas.push(slimnica);

        render();
    }

}

function render() {
    let saraksts = document.getElementById('saraksts');
    saraksts.innerHTML = "";

    for(let i = 0; i < slimnicas.length; i++) {

        let slimnica = `
    <li class="slimnica">
        <h3>Slimnīca: ${slimnicas[i].nosaukums}</h3>⠀⠀⠀<h4>Adrese: ${slimnicas[i].adrese}</h4>⠀⠀⠀⠀
        <button class="del">Dzēst</button>
    </li>`;
    saraksts.innerHTML += slimnica;
    }

    if(!localStorage.getItem('slimnicas')){
      localStorage.setItem('slimnicas', JSON.stringify($scope.slimnicas));
    } 
}

const list = document.querySelector('#saraksts')

list.addEventListener('click', (e) => {
    if(e.target.className == 'del'){
      const li = e.target.parentElement;
      li.parentNode.removeChild(li);
      slimnicas.splice(li, 1);
      if(!localStorage.getItem('slimnicas')){
        localStorage.setItem('slimnicas', JSON.stringify($scope.slimnicas));
      }
    }
  });
