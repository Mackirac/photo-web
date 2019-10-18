var inputReader = new FileReader();
var connection = new XMLHttpRequest();
var image = document.querySelector('#image');
var file_selector = document.querySelector('#file_selector');
var hidden_input = document.querySelector('#hidden_form input');

file_selector.value = null;

inputReader.onload = function() {
    image.src = this.result
};

file_selector.addEventListener('change', (ev) => {
    if (ev.target.value != undefined)
        inputReader.readAsDataURL(file_selector.files[0]);
});

function send_request (url) {
    let form = new FormData(document.querySelector('#hidden_form'));
    connection.open('POST', url, false);
    connection.send(form);
}

function getImageData () {
    hidden_input.value = image.src.split(',')[1];
}

function updateImage () {
    connection.onreadystatechange = function (event) {
        if (this.status == 200 && this.readyState == 4) {
            image.src = 'data:image/png;base64,' + this.response;
        }
    }
}

function negative () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/negative');
}

function log () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/log');
}

function pot () {
    let factor = prompt("Fator:");
    updateImage();
    getImageData();
    send_request('http://localhost:8000/pow/' + factor);
}

function parts () {
    let input = prompt("Entre os intervalos no formato 'Ii, If, Fi, Ff'");
    input = input.replace(/\s/g, '').split(',');
    updateImage();
    getImageData();
    send_request(
        `http://localhost:8000/parts/${input[0]}/${input[1]}/${input[2]}/${input[3]}`
    );
}

function hide () {
    console.log('hide')
}

function seek () {
    console.log('seek')
}

function get_hist () {
    console.log('get_hist')
}

function equalize () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/equalize');
}

function mean () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/mean');
}

function gauss () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/gaussian');
}

function median () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/median');
}

function conv () {
    console.log('conv')
}

function laplace1 () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/laplace1');
}

function laplace2 () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/laplace2');
}

function high_boost () {
    let factor = prompt("Factor:");
    updateImage();
    getImageData();
    send_request('http://localhost:8000/highboost/' + factor);
}

function grayscale () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/grayscale');
}

function weighted_grayscale () {
    let weights = prompt(
        "Pesos no formato 'p1, p2, p3' (a soma dos pesos DEVE ser igual a 1):"
    );
    weights = weights.replace(/\s/g, '').split(',');
    updateImage();
    getImageData();
    send_request(
        `http://localhost:8000/weighted_grayscale/${weights[0]}/${weights[1]}/${weights[2]}
    `);
}

function sepia () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/sepia');
}

function geo_mean () {
    console.log('geo_mean')
}

function harm_mean () {
    console.log('harm_mean')
}

function ch_mean () {
    console.log('ch_mean')
}

function sobel () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000/sobel');
}

function binarize () {
    let threshold = prompt("Limiar:");
    updateImage();
    getImageData();
    send_request('http://localhost:8000/binarize/' + threshold);
}
