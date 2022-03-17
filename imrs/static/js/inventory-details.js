$(document).ready(function () {
    $(".tableRow").click(function () {
      window.location = $(this).data("href");
      return false
    });
  });

  function Search() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("inventory-list");
    tr = table.getElementsByClassName("tableRow");

    var match = false;

    var noResults = document.getElementById("no-results");
  
    // Loop through all table rows, and hide those who don't match the search query

    if (input.innerHTML.length === 0) {
      match = false;
      noResults.style.display= "none";
    }

    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          match = true;
        } else {
          tr[i].style.display = "none";
        }
      }
    }

    if (match===false) {
      noResults.style.display= "table-row"
    }
  }