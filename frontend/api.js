let urlHolder = document.getElementById("urls")
let user = document.getElementById("user")
const BASE_URL = "http://127.0.0.1:8000"

fetch(BASE_URL + "/api/")
.then(res => res.json())
.then(data => {
    data.urls.forEach(element => {
        user.innerText = element.creator
        console.log(element)
        let link = BASE_URL + "/short/" + element.id
        urlHolder.innerHTML += `<a href="${link}">${element.title}</a>`
    })
})
