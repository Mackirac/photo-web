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
    if (this.value != undefined)
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
    console.log('negative')
}

function log () {
    updateImage();
    getImageData();
    send_request('http://localhost:8000');
}

function pot () {
    console.log('pot')
}

function parts () {
    console.log('parts')
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
    console.log('equalize')
}

function mean () {
    console.log('mean')
}

function gauss () {
    console.log('gauss')
}

function median () {
    console.log('median')
}

function conv () {
    console.log('conv')
}

function laplace1 () {
    console.log('laplace1')
}

function laplace2 () {
    console.log('laplace2')
}

function high_boost () {
    console.log('high_boost')
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
    console.log('sobel')
}

function binarize () {
    console.log('binarize')
}
