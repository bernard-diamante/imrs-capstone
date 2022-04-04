$(document).ready(function () {
  $('#table').on("click", ".row-href", function () {
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

// Inventory Select dropdown
$(document).ready(function() {
  $('.search-select').select2({
    placeholder: "Select a site",
    language: {
      "noResults": function() {
        return "No results found."
      }
    }
  });
});

$(document).ready(function() {
  $('#table_length select').select2({
    minimumResultsForSearch: -1
  });
});