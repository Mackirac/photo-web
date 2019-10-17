var inputReader = new FileReader();
var imageReader = new FileReader();
var connection = new XMLHttpRequest();
var image = document.querySelector('#image');
var imageBytes = '';
var file = document.querySelector('#file_selector');

file.value = '';

inputReader.onload = function() {
    image.src = this.result
};

imageReader.onload = function() {
    imageBytes = this.result;
}

file.addEventListener('change', (ev) => {
    inputReader.readAsDataURL(file.files[0]);
});

function open_request (url) {
    connection.open('POST', url, false);
}

function dataURItoBlob (dataURI) {
    var byteString = atob(dataURI.split(',')[1]);
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0]
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    var blob = new Blob([ab], {type: mimeString});

    return blob;
}

function getImageBlob () {
    imageReader.readAsBinaryString(dataURItoBlob(image.src));
}

function negative () {
    console.log('negative')
}

function log () {
    console.log('log')
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
