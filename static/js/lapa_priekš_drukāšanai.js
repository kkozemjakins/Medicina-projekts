datums = localStorage.getItem('datums');
laiks = localStorage.getItem('laiks');

current_user_name = localStorage.getItem('Current User Name');


document.getElementById("Vizites_Laiks").innerHTML = datums + " " + laiks;

document.getElementById("Vards_Uzvards").innerHTML = current_user_name;
