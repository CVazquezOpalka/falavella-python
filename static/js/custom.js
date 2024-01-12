$(document).ready(function () {
  $(".increment-btn").click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest(".product_data").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });
  $(".decrement-btn").click(function (e) {
    e.preventDefault();
    var dec_value = $(this).closest(".product_data").find(".qty-input").val();
    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });
  $(".addToCartBtn").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var prod_qty = $(this).closest(".product_data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        product_id: product_id,
        product_qty: prod_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
      },
    });
  });
  $(".changeQuantity").click(function (e) {
    e.preventDefault();
    console.log("estoy hacendo click");
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var product_qty = $(this).closest(".product_data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      type: "POST",
      url: "/update-cart",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });
  $(document).on("click", ".delete-cart-item", function (e) {
    e.preventDefault();
    var prod_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(prod_id, token);
    $.ajax({
      type: "POST",
      url: "/delete-cart-item",
      data: {
        product_id: prod_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        $(".cartdata").load(location.href + " .cartdata");
      },
    });
  });
  $(".addToWishList").click(function (e) {
    e.preventDefault();
    console.log("hice Click");
    var prod_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/add-to-wishlist",
      data: {
        product_id: prod_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        $(".cartdata").load(location.href + ".cartdata");
      },
    });
  });
  $(document).on("click", ".delete-wishlist", function (e) {
    e.preventDefault();
    console.log("hice click");
    var prod_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(prod_id, token);
    $.ajax({
      method: "POST",
      url: "/delete-to-wishlist",
      data: {
        product_id: prod_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        $(".wishdata").load(location.href + " .wishdata");
      },
    });
  });
});
