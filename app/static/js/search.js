function apair(){
    us[i].style.display = "";
}
function myFunctionU() {
    var input, filter, table, tr, th, i, txtValue;
    input = document.getElementById("campoPesquisaU");
    filter = input.value.toUpperCase();
    table = document.getElementById("searcher");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    th = tr[i].getElementsByTagName("th")[0];
    if (th) {
        txtValue = th.textContent || th.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        } else {
        tr[i].style.display = "none";
        }
    }
    }
}
function myFunctionM() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("campoPesquisaM");
    filter = input.value.toUpperCase();
    table = document.getElementById("searcher");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        } else {
        tr[i].style.display = "none";
        }
    }
    }
}