StorageUser = window.localStorage;

let user_data = [];

const login = document.getElementById('buttonLOGIN');

const reg = document.getElementById('buttonREG');

window.addEventListener('load', () => {
    user_data = JSON.parse(localStorage.getItem("user_data") || "[]");
    console.log(user_data)
    render();
});

document.getElementById('buttonREG').addEventListener('click', () => {

    login.style.display = 'none';
    reg.style.display = 'none';

    let vards = document.getElementById("login_div").innerHTML = ` 
    <p><input id="username" class="input" type="text"  maxlength="30" placeholder="Vārds Uzvārds" required></p>
    <p><input id="password" class="input" type="text" maxlength="30" placeholder="Parole" required></p>
    <p><input id="passwordADD" class="input" type="text" maxlength="30" placeholder="Apstipriniet paroli" required></p>
    <p><button class="button" id="Registracija" onclick="registracija()" style="font-size: 40px;margin-top: 20%;height: 73px;width: 500px;">Reģistrācija</button></p>`;

})

document.getElementById('buttonLOGIN').addEventListener('click', () => {

    login.style.display = 'none';
    reg.style.display = 'none';

    let vards = document.getElementById("login_div").innerHTML = `      
    <p><input id="username" class="input" type="text"  maxlength="30" placeholder="Vārds Uzvārds" required></p>
    <p><input id="password" class="input" type="text" maxlength="30" placeholder="Parole" required></p>
    <p><button class="button" id="Login" onclick="Login()" style="font-size: 40px;margin-top: 20%;height: 73px;width: 500px;">Login</button></p>`;

})

function Login(){
    
    for(let i = 0; i < user_data.length; i++) {
        login_name = document.getElementById('username').value;

        login_pass = document.getElementById('password').value;

        console.log(login_name)
        console.log(login_pass)
        

        if(login_name === user_data[i].username && login_pass == user_data[i].password){

            window.location = "/guest_main";
            let current_user_name = localStorage.setItem("Current User Name", login_name)
        }

        if(login_name === "admin" && login_pass == "admin"){

            window.location = "/admin_main";
        }


    }

    username.value = "";
    password.value = "";

}

function registracija(){
    let data = {username: username.value, password: password.value};

    if(password.value === passwordADD.value && password.value != ""){
        user_data.push(data);

        render();

        window.location = "/";
    }

    username.value = "";
    password.value = "";
    passwordADD.value = "";



}

function render() {

    localStorage.setItem("user_data", JSON.stringify(user_data))
}