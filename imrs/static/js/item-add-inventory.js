function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addItem(itemID) {
    var csrftoken = getCookie('csrftoken');
    let data_to_backend = new FormData()
    if (itemID !== '') {
        data_to_backend.append('itemID', itemID)
    } else return
    
    const request = new Request("./", 
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: data_to_backend
    })
    fetch(request, {
        method: 'POST',
        mode: 'same-origin'
    }).then(
        function(response) {
            if (response.status === 200) {
                let rowButton = document.getElementById(`item-${ itemID }`)
                rowButton.innerHTML = "✓"
            } else {
                alert("Error")
                console.log(response)
                for (var val of data_to_backend.values()){
                    console.log(val);
                }
            }
        }
    )
}
