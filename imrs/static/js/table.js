$(document).ready(function () {
  $(".row-href").click(function () {
    window.location = $(this).data("href");
    return false;
  });
});

var table = $("#table").DataTable({
  initComplete: function() {
    $('#table_wrapper').prepend($('<div id="table-top" class="flex flex-row mb-5"></div'))
    $('#table_filter').appendTo($('#table-top'))
    $('#table_length').appendTo($('#table-top'))
    $('#table_filter').addClass('flex flex-row justify-start')
    $('#page-button').appendTo($('#table-top'))
    
  },
  responsive: true,
  language: {
    zeroRecords: "No matching results found.",
    emptyTable: "No available records.",
    search: "",
    searchPlaceholder: "Search",
    lengthMenu: "No. Entries: _MENU_"
  },
  lengthMenu: [10, 25, 50],
});



// #myInput is a <input type="text"> element
// $('#myInput').on( 'keyup', function () {
//     table.search( this.value ).draw();
// } );