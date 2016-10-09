function draw_strikezone(id, pitches) {
    var c = document.getElementById(id);
    var background_img = document.getElementById('home_plate')
    var ctx = c.getContext("2d");
    var w=c.width

    var mw = w/2;
    var box_width = w - mw;
    var rbox_width = 17/12;
    var wf = box_width / rbox_width;
    var rw = w / wf;
    var rmw = mw / wf;

    var h = c.height;
    var rbox_size = pitches[0]['sz_top'] - pitches[0]['sz_bot'];
    var box_size = rbox_size*wf;
    var bmh = h*.2;
    var tmh = h - box_size - bmh;
    var cr = (2.6/12)/2 * wf;
    ctx.beginPath();
    ctx.strokeStyle= 'black';
    ctx.lineWidth = 2;
    ctx.fillStyle = 'rgba(0, 0, 0, .6)';
    var fheight = parseInt(cr);
    ctx.font = fheight+"px Georgia";

    ctx.drawImage(background_img, 0, 0, w, h);
    ctx.fillRect(mw/2, tmh, w-mw, box_size);//w*.25, h*25, w-w*.25, h-h*.25);
    for (var i = 0; i < pitches.length; i++){
        var rx = rmw/2 + (17/12)/2 + parseFloat(pitches[i]['px']);
        var x = wf*rx;//mw+pitches[i]['px']*12*mw/17;
        var y = tmh + wf*(pitches[i]['sz_top'] - pitches[i]['pz']);

        if(pitches[i]["type"]=="B"){
            ctx.fillStyle = '#11a016';
        } else if(pitches[i]["type"]=="S") {
            ctx.fillStyle = '#ba2525';
        } else {
            ctx.fillStyle = '#252580';
	}
        ctx.beginPath();
        ctx.arc(x, y, cr, 0, 2 * Math.PI);
        ctx.fill();
        ctx.arc(x, y, cr, 0, 2 * Math.PI);
        ctx.stroke();

        ctx.fillStyle = "#000000";
        var fwidth = cr/2;
        ctx.fillText(""+(i+1), x - fwidth/2, y + fheight/4, fwidth);
    }
}
