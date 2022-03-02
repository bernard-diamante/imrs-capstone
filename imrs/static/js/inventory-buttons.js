function toggleButtons(){
  var x = document.getElementById("buttons");
  if (x.className === "hidden") {
    x.className = "flex";
  } else {
    x.className = "hidden";
  }
}