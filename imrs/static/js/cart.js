var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var item = this.dataset.item
		var action = this.dataset.action
		console.log('item:', item, 'Action:', action)
		console.log('USER:', user)
        if (user == 'anonymous') {
            console.log('User is not authenticated')
        }else{
            updateUserOrder(item, action)
        }

	})
}

function updateUserOrder(item, action){
    console.log('User is authenticated, sending data...')

	var url = 'cart/add/'
	fetch(url, {
		method: 'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
        body:JSON.stringify({'item':item, 'action':action})
	})
	.then((response)=>{
        return response.json()
    })

	.then((data)=>{
        console.log('data: ', data)
    })
}

$(document).ready(function ()
    {
        ClickHand();
    });

    function setClickHandlers() {

        var cells = document.querySelectorAll('#switchboard-container td');

        Array.prototype.forEach.call(cells, function (td) {
            td.addEventListener('click', changeCell);
        });
    }

    function changeCell() {
        
        $(".switch").text("Off");
        this.textContent = "Up";

    }

$('.update-cart').click(function () {
    $(this).replaceWith("<p class='h-7 w-7 cursor-default justify-center text-sm font-bold flex ml-auto mr-2 text-white bg-green-500 border-0 py-1 px-1 focus:outline-none hover:bg-green-600 rounded-full'>✓</p>")
})