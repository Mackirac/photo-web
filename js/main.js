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

function rgb_to_hsv () {
    let rgb = prompt('Entre os componentes rgb separados por vírgula').trim().split(',');
    let r = Number(rgb[0]);
    let g = Number(rgb[1]);
    let b = Number(rgb[2]);
    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b)

    let h = 0;
    let s = 0;
    let v = 0;

    if (max == r && g >= b) {
        h = Math.round(60 * (g - b) / (max - min));
    }
    else if (max == r && g < b) {
        h = Math.round(360 + 60 * (g - b) / (max - min));
    }
    else if (max == g) {
        h = Math.round(120 + 60 * (b - r) / (max - min));
    }
    else if (max == b) {
        h = Math.round(240 + 60 * (r - g) / (max - min));
    }
    if (isNaN(h)) { h = 0; }

    s = 100 * (max - min) / max;
    if (isNaN(s)) { s = 0; }

    v = max * 100 / 255;

    alert(`H = ${h}, S = ${s}%, V = ${v}%`);
}

function hsv_to_rgb () {
    let hsv = prompt('Entre os valores hsv separados por vírgula').trim().split(',');
    let h = Number(hsv[0]);
    let s = Number(hsv[1]) / 100;
    let v = Number(hsv[2]) / 100;

    let r = 0;
    let g = 0;
    let b = 0;

    let hi = Math.floor(h / 60) % 6;
    let f = (h / 60) - hi;
    let p = v * (1 - s);
    let q = v * (1 - f*s);
    let t = v * (1 - (1 - f)*s);

    if (hi == 0) {
        r = v;
        g = t;
        b = p;
    }
    else if (hi == 1) {
        r = q;
        g = v;
        b = p;
    }
    else if (hi == 2) {
        r = p;
        g = v;
        b = t;
    }
    else if (hi == 3) {
        r = p;
        g = q;
        b = v;
    }
    else if (hi == 4) {
        r = t;
        g = p;
        b = v;
    }
    else if (hi == 5) {
        r = v;
        g = p;
        b = q;
    }

    r = Math.round(255 * r);
    g = Math.round(255 * g);
    b = Math.round(255 * b);

    alert(`R = ${r}, G = ${g}, B = ${b}`);
}

// function chromakey(event) {
//     if (event.target.value != undefined) {
//         event.target.form = hidden_input.parentElement;
//         // updateImage();
//         getImageData();
//         send_request('http://localhost:8000/chromakey');
//     }
// }

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
    let text = prompt("Texto a ser escondido:");
    updateImage();
    getImageData();
    send_request('http://localhost:8000/hide/' + text);
}

function seek () {
    getImageData();
    connection.onreadystatechange = function() {
        if (this.status == 200 && this.readyState == 4) {
            alert(this.responseText);
        }
    }
    send_request('http://localhost:8000/seek')
}

function get_hist () {
    getImageData();
    connection.onreadystatechange = function() {
        if (this.status == 200 && this.readyState == 4) {
            let im = new Image();
            im.src = 'data:image/png;base64,' + this.responseText;
            var w = window.open('');
            w.document.write(im.outerHTML);
        }
    }
    send_request('http://localhost:8000/hist');
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
    document.querySelector('#panel').style.display = 'none';
    let cells = document.querySelectorAll('.filter-cell');
    let filter = { dx: dx, dy: dy, values: [] };
    for (x = 0; x < cells.length - 1; x++) {
        filter.values.push(Number(cells[x].value));
    }
    filter.divisor = Number(cells[cells.length - 1].value);
    console.log(JSON.stringify(filter));
    updateImage();
    getImageData();
    send_request('http://localhost:8000/conv/' + JSON.stringify(filter));
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
    updateImage();
    getImageData();
    send_request('http://localhost:8000/harm_mean');
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
