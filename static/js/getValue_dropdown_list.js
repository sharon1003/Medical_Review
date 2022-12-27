function myFunction1() {
  var mylist = document.getElementById("num_Room");
  document.getElementById("num_Room_demo").value = mylist.options[mylist.selectedIndex].text;
}

function myFunction2() {
  var mylist = document.getElementById("Room_type");
  document.getElementById("Room_type_demo").value = mylist.options[mylist.selectedIndex].text;
}

function processFormData1() {
  var nameElement = document.getElementsByName('Arrival_date');
  var Arrival_date = nameElement[0].value;
  document.getElementsByName("Arrival_date_demo")[0].value = Arrival_date;
}

function processFormData2() {
  var nameElement = document.getElementsByName('Dep_date');
  var Dep_date = nameElement[0].value;
  document.getElementsByName("Dep_date_demo")[0].value = Dep_date;
}