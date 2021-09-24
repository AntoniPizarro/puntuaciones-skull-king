const ipList = [
    "192.168.1.36",
    "192.168.1.34",
    "192.168.43.110",
    "83.40.85.218"
]

// Cambiar segun las necesidades
const ipDirection = ipList[1]
const port = "5505"

const ip ="http://" + ipDirection + ":" + port;

function checkSesion() {
    if (window.sessionStorage) {
        username = document.getElementById('username').value;
        password = document.getElementById('user-pass').value;
        sessionStorage.setItem("username", username);
        sessionStorage.setItem("password", password);
        let user = {
            "username" : username,
            "password" : password
        }
        fetch(ip + '/users/add', {
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(user),
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(data => {
            console.log(data)
            alert(data["new_user"]);
        });
    }else {
        throw new Error('Tu Browser no soporta sessionStorage!');
    }
}

function openPage(url) {
    window.location.href = url;
}

function pruebas(data) {
    console.log(data);
}

function checkAccount() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('user-pass').value;
    let data = {
        "username": username,
        "password": password
    };
    let newUser;
    if (username != "" && password != "") {
        fetch(ip + '/users/add', {
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            state = data["state"];
            newUser = data["new"];
            if (state) { // Conexion a BD satisfactoria
                if (window.sessionStorage) {
                    sessionStorage.setItem("username", username);
                    sessionStorage.setItem("password", password);
                }else {
                    throw new Error('Tu Browser no soporta sessionStorage!');
                }
                if (!newUser) { // No es nuevo usuario
                    let logging = confirm(data["new_user"] + ". ¿Desea iniciar sesión?");
                    if (!logging) { // No desea iniciar sesion
                        return 0;
                    }
                }
                openPage("./maze.html");
            }else {
                alert(data["new_user"]);
            }
        });
    }else{
        alert("Debe rellenar los datos");
    }
}