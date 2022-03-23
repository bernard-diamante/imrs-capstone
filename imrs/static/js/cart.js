var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var itemID = this.dataset.item
		var action = this.dataset.action
		console.log('itemID:', itemID, 'Action:', action)
		console.log('USER:', user)
        if (user == 'anonymous') {
            console.log('User is not authenticated')
        }else{
            updateUserOrder(itemID, action)
        }

	})
}

function updateUserOrder(itemID, action){
    console.log('User is authenticated, sending data...')

	var url = 'cart/update_item/'
	fetch(url, {
		method: 'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
        body:JSON.stringify({'itemID':itemID, 'action':action})
	})
	.then((response)=>{
        return response.json()
    })

	.then((data)=>{
        console.log('data: ', data)
    })
}