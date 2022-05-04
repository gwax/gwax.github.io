function fancydates(fanciness) {
    if (fanciness === 0) {
        return;
    }

    var dates = document.querySelectorAll('.dt-published, .dt-updated, .listdate');

    var l = dates.length;

    for (var i = 0; i < l; i++) {
        var d = new Date(dates[i].attributes.datetime.value);
        var o;
        if (fanciness === 1) {
            o = d.toLocaleString();
        } else {
            o = d.toISOString();
        }
        dates[i].innerHTML = o;
    }
}
