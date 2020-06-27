$(".delete").click(function (e) {
    var id = this.id;
    var href = this.href;
    console.log(href, id) // get href from link
    e.preventDefault(); // don't follow the link

    $.ajax({
      url: href,
      data: {},
    });

    $("#" + id).fadeOut(1000);

});
