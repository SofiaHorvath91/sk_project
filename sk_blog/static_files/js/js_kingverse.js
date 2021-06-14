var kingverseImg = document.getElementById('kingverse-img');
var kingverseRefsImg = document.getElementById('kingverse-refs-img');
var startMicroscopeBtn = document.getElementById('start-microscope-btn');
var endMicroscopeBtn = document.getElementById('end-microscope-btn');

function magnify(img, zoom){
    var glass, w, h, bw;

    glass = document.createElement("DIV");
    glass.setAttribute("class", "img-magnifier-glass");

    img.parentElement.insertBefore(glass, img);

    glass.style.backgroundImage = "url('" + img.src + "')";
    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;

    glass.addEventListener("mousemove", moveMagnifier);
    img.addEventListener("mousemove", moveMagnifier);

    glass.addEventListener("touchmove", moveMagnifier);
    img.addEventListener("touchmove", moveMagnifier);

    function moveMagnifier(e) {
        var pos, x, y;

        e.preventDefault();

        pos = getCursorPos(e);
        x = pos.x;
        y = pos.y;

        if (x > img.width - (w / zoom)){
            x = img.width - (w / zoom);
        }
        if (x < w / zoom){
            x = w / zoom;
        }
        if (y > img.height - (h / zoom)){
            y = img.height - (h / zoom);
        }
        if (y < h / zoom){
            y = h / zoom;
        }

        glass.style.left = (x - w) + "px";
        glass.style.top = (y - h) + "px";

        glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
    }

    function getCursorPos(e) {
        var a, x = 0, y = 0;
        e = e || window.event;

        a = img.getBoundingClientRect();

        x = e.pageX - a.left;
        y = e.pageY - a.top;

        x = x - window.pageXOffset;
        y = y - window.pageYOffset;
        return {x : x, y : y};
    }
}

function switchImage(state){
    if(state == 0){
        kingverseImg.classList.add('hidden');
        kingverseRefsImg.classList.remove('hidden');
    }
    else{
        kingverseImg.classList.remove('hidden');
        kingverseRefsImg.classList.add('hidden');
    }
}

kingverseImg.addEventListener('click', () => {
    switchImage(0);
    startMicroscopeBtn.disabled = true;
});

kingverseRefsImg.addEventListener('click', () => {
    switchImage(1);
    startMicroscopeBtn.disabled = false;
});

startMicroscopeBtn.addEventListener('click', () => {
    magnify(kingverseImg, 3);
    startMicroscopeBtn.classList.add('hidden');
    endMicroscopeBtn.classList.remove('hidden');
    kingverseImg.removeEventListener('click', switchImage);
    kingverseRefsImg.removeEventListener('click', switchImage);
});

endMicroscopeBtn.addEventListener('click', () => {
    location.reload()
});