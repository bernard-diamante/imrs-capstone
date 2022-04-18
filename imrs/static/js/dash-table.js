$(document).ready(function () {
  $(".table").each(function () {
    $(this).on("click", ".row-href", function () {
      window.location = $(this).data("href");
      return false;
    });

    var table = $(this).DataTable({
      // initComplete: function() {
      //   $('#table_wrapper').prepend($('<div id="table-top" class="flex flex-row mb-5"></div'))
      //   $('#table_filter').appendTo($('#table-top'))
      //   $('#table_length').appendTo($('#table-top'))
      //   $('#table_filter').addClass('flex flex-row justify-start')
      //   $('#page-button').appendTo($('#table-top'))

      // },
      dom: "rtip",
      responsive: true,
      language: {
        zeroRecords: "No matching results found.",
        emptyTable: "No available records.",
        search: "",
        searchPlaceholder: "Search",
        lengthMenu: "No. Entries: _MENU_",
      },
      lengthMenu: [10, 25, 50],
    });
  });
});
