$(".like").click(function (e) {
    var id = this.id; //$(this).attr('id');
    var href = $('.like').find('a').attr('href');
    e.preventDefault(); // don't follow the link

    $.ajax({
        url: href,
        data: {
          'likeId': id
        },
        success: function(response){
          if(response.liked){
            $('#likebtn' + id).html("Liked");
          }
          else{
            $('#likebtn' + id).html("Like");
          }
        }
      })
});
