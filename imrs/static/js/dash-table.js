$(document).ready(function () {
  $(".req-table").on("click", ".row-href", function () {
    window.location = $(this).data("href");
    return false;
  });

  $(".inv-table").on("click", ".row-href", function () {
    window.location = $(this).data("href");
    return false;
  });

  var reqtable = $(".req-table").DataTable({
    responsive: true,
    dom: "trip",
    language: {
      zeroRecords: "No matching results found.",
      emptyTable: "No available records.",
      search: "",
      searchPlaceholder: "Search",
      lengthMenu: "No. Entries: _MENU_"
    },
    lengthMenu: [5],
    pagingType: "simple",
    columnDefs: [ { type: 'date', 'targets': [2] } ],
    order: [[ 2, 'asc' ]]
  });
  
  var invtable = $(".inv-table").DataTable({
    responsive: true,
    dom: "trip",
    language: {
      zeroRecords: "No matching results found.",
      emptyTable: "No available records.",
      search: "",
      searchPlaceholder: "Search",
      lengthMenu: "No. Entries: _MENU_",
    },
    lengthMenu: [5],
    pagingType: "simple",
    order: [[ 2, 'asc' ]]
  });
});



