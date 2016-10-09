function draw_strikezone(id, pitches) {
    var c = document.getElementById(id);
    var ctx = c.getContext("2d");
    w=parseInt(c.getAttribute("width"));
    mw = parseInt(w/2);
    h=12*mw*(pitches[0]['sz_top']-pitches[0]['sz_bot'])/17;
    mh = parseInt(h/2);
    c.height = h;
    ctx.beginPath();
    ctx.strokeStyle= 'black';
    ctx.lineWidth = 2;
    ctx.fillStyle = 'rgba(0, 0, 0, .8)';
    ctx.fillRect(w*.25, 0, w*.5, h);//w*.25, h*25, w-w*.25, h-h*.25);
    for (var i = 0; i < pitches.length; i++){
        var x = mw+pitches[i]['px']*12*mw/17;//mw+pitches[i]['px']*12*mw/17;
        var y = 1.2*12*mw/17;//pitches[i]['pz']*12*mw/17;
        if(pitches[i]["des"]=="Ball"){
            ctx.fillStyle = 'rgba(0, 255, 0, 1)';
        } else{
            ctx.fillStyle = 'rgba(255, 0, 0, 1)';
        }
        ctx.beginPath();
        ctx.arc(x, y, 2*250/17, 0, 2 * Math.PI);
        ctx.fill();
        ctx.arc(x, y, 2*258/17, 0, 2 * Math.PI);
        ctx.stroke();
    }
}
