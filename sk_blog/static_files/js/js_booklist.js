$(document).ready(function(){
  $("#searchValue").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#book-table tbody tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("book-table");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if(n != 5)
        {
            if(n == 1){
                if (x.innerHTML.split(">")[2].toLowerCase() > y.innerHTML.split(">")[2].toLowerCase()) {
                  shouldSwitch= true;
                  break;
                }
            }
            else{
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                  shouldSwitch= true;
                  break;
                }
            }
        }
        else
        {
            if (getDate(x.innerHTML).getTime() > getDate(y.innerHTML).getTime()) {
                shouldSwitch = true;
                break;
            }
        }
      } else if (dir == "desc") {
        if(n != 5)
        {
            if(n == 1){
                if (x.innerHTML.split(">")[2].toLowerCase() < y.innerHTML.split(">")[2].toLowerCase()) {
                  shouldSwitch= true;
                  break;
                }
            }
            else{
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                  shouldSwitch= true;
                  break;
                }
            }
        }
        else
        {
            if (getDate(x.innerHTML).getTime() < getDate(y.innerHTML).getTime()) {
                shouldSwitch = true;
                break;
            }
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function getDate(date){
    return new Date(date);
}