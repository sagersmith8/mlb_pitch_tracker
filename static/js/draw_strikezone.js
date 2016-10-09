function draw_strikezone(id, pitches) {
    var c = document.getElementById(id);
    var ctx = c.getContext("2d");
    h=parseInt(c.getAttribute("height"));
    mh = parseInt(h/2);
    w=parseInt(c.getAttribute("width"));
    mw = parseInt(w/2);
    ctx.beginPath();
    ctx.strokeStyle= 'red';
    ctx.lineWidth = 2;
    ctx.fillStyle = 'rgba(0, 0, 0, .8)';
    ctx.fillRect(w*.25, h*.25, w-w*.5, h-h*.5);//w*.25, h*25, w-w*.25, h-h*.25);
    for (var i = 0; i < pitches.length; i++){
        var x = parseFloat(pitches[i]['px'])-1;
        var y = parseFloat(pitches[i]['pz'])-1;
        if(pitches[i]["pitch_call"]=="strike"){
            ctx.fillStyle = 'rgba(255, 0, 0, 1)';
        } else{
            ctx.fillStyle = 'rgba(0, 255, 0, 1)';
        }
        ctx.beginPath();
        ctx.arc(mw, mh, 10, 0, 2 * Math.PI);
        ctx.fill();

    }
    //ctx.font="20px Georgia";
    //ctx.fillText("Hi", 0, 0);
}
