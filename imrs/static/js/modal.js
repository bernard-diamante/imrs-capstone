// function toggleButtons(){
//   var x = document.getElementById("buttons");
//   if (x.className === "hidden") {
//     x.className = "flex";
//   } else {
//     x.className = "hidden";
//   }
// }

var closeModal = document.querySelectorAll('.modal-toggle')

for (var i = 0; i < closeModal.length; i++) {
  closeModal[i].addEventListener('click', toggleModal)
}

function toggleModal () {
  const body = document.querySelector('body')
  const modal = document.querySelector('.modal')
  modal.classList.toggle('opacity-0')
  modal.classList.toggle('pointer-events-none')
  body.classList.toggle('modal-active')
}

