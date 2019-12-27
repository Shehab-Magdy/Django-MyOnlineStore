// console.log("Hello");

$(function() {
  $(".dislike").hide();

  function doDisLike() {
    // console.log("dislike clicked");
    prod_id = $(this).attr("data1");
    $("#" + prod_id + "_L").show();
    $("#" + prod_id + "_D").hide();
    $.ajax({
      url: "http://127.0.0.1:8000/product/dislike/ajax",
      crossDomain: true,
      type: "GET",
      data: {
        prodId: prod_id
      },
      success: function(response) {
        console.log(response);
        $("#" + prod_id).html(response);
      },
      error: function(error) {
        console.log("error");
      }
    });
  }

  $(".dislike").click(doDisLike);

  function doLike() {
    prod_id = $(this).attr("data1");
    // console.log("BTN clicked");
    $("#" + prod_id + "_D").show();
    $("#" + prod_id + "_L").hide();

    $.ajax({
      url: "http://127.0.0.1:8000/product/like/ajax",
      crossDomain: true,
      type: "GET",
      data: {
        prodId: prod_id
      },
      success: function(response) {
        console.log(response);
        $("#" + prod_id).html(response);
      },
      error: function(error) {
        console.log("error");
      }
    });
  }

  $(".like").click(doLike);
});
