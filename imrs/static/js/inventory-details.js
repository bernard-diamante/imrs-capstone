$(document).ready(function () {
    $(".tableRow").click(function () {
      window.location = $(this).data("href");
      return false
    });
  });

  // function Search() {
  //   // Declare variables
  //   var input, filter, table, tr, td, i, txtValue;
  //   input = document.getElementById("myInput");
  //   filter = input.value.toUpperCase();
  //   table = document.getElementById("inventory-list");
  //   tr = table.getElementsByClassName("tableRow");

  //   var match = false;

  //   var noResults = document.getElementById("no-results");
  
  //   // Loop through all table rows, and hide those who don't match the search query

  //   if (input.innerHTML.length === 0) {
  //     match = false;
  //     noResults.style.display= "none";
  //   }

  //   for (i = 0; i < tr.length; i++) {
  //     td = tr[i].getElementsByTagName("td")[0];
  //     if (td) {
  //       txtValue = td.textContent || td.innerText;
  //       if (txtValue.toUpperCase().indexOf(filter) > -1) {
  //         tr[i].style.display = "";
  //         match = true;
  //       } else {
  //         tr[i].style.display = "none";
  //       }
  //     }
  //   }

  //   if (match===false) {
  //     noResults.style.display= "table-row"
  //   }
  // }

  var table = $('#table').DataTable({
    responsive: true,
    "language": {
      "zeroRecords": "No matching results found.",
      "emptyTable": "No available records."
    }
  });
 
// #myInput is a <input type="text"> element
    $('#myInput').on( 'keyup', function () {
        table.search( this.value ).draw();
    } );


  // Pagination

//   $(document).ready(function(){
//     var rowsShown = 2;
//     var rowsTotal = $('#inventory-list tbody tr').length;
//     var numPages = rowsTotal/rowsShown;
//     for(i = 0;i < numPages;i++) {
//         var pageNum = i + 1;
//         $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
//     }
//     $('#inventory-list tbody tr').hide();
//     $('#inventory-list tbody tr').slice(0, rowsShown).show();

//     $('#nav a').addClass('text-black bg-gray-200 px-4 py-2 rounded-lg outline-none hover:bg-gray-300 ease-in duration-100');
//     $('#nav a:first').removeClass('hover:bg-gray-300').addClass('scdc-green hover:scdc-green text-white');
//     $('#nav a').bind('click', function(){

//         $('#nav a').removeClass('scdc-green text-white').addClass('text-black bg-gray-200 hover:bg-gray-300');
//         $(this).removeClass('text-black bg-gray-200 hover:bg-gray-300').addClass('scdc-green hover:scdc-green text-white');
//         var currPage = $(this).attr('rel');
//         var startItem = currPage * rowsShown;
//         var endItem = startItem + rowsShown;
//         $('#inventory-list tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
//         css('display','table-row').animate({opacity:250}, 300);
//     });
// });