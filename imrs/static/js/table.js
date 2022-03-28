$(document).ready(function () {
  $(".row-href").click(function () {
    window.location = $(this).data("href");
    return false;
  });
});

var table = $("#table").DataTable({
  responsive: true,
  language: {
    zeroRecords: "No matching results found.",
    emptyTable: "No available records.",
  },
  lengthMenu: [10, 25, 50],
});

// #myInput is a <input type="text"> element
// $('#myInput').on( 'keyup', function () {
//     table.search( this.value ).draw();
// } );