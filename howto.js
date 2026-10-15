function init_pagination() {
  var pagescount = 8, i, txt = "", able = " pagdisabled";
  var prevPage = "default.asp";
  var nextPage = "default_page2.asp";
  
  for (i = 1; i <= pagescount; i++) {
    var defPage = (i === 1) ? "default.asp" : ("default_page" + i + ".asp");
    if (i === 1) {
      txt += "<a class='howtopag_item" + able + "' href='" + prevPage + "'>&#10094;</a>";
    }
    var activeClass = (i === 1) ? " pagactive" : "";
    txt += "<a class='howtopag_item" + activeClass + "' href='" + defPage + "'>" + i + "</a>";
    if (i === pagescount) {
      txt += "<a class='howtopag_item' href='" + nextPage + "'>&#10095;</a>";
    }
  }
  var x = document.getElementsByClassName("howtopag");
  for (i = 0; i < x.length; i++) {
    x[i].innerHTML = txt;
  }
}
