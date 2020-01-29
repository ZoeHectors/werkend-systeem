function maak_afspraak() {

    let naam = document.getElementById('firstname').value + ' ' + document.getElementById('lastname').value;
    let datumtijd = document.getElementById('datumtijd').value;
    let email = document.getElementById('email').value;
    let behandeling = document.querySelector('input[name="behandeling"]:checked').value;

    let data = { 'naam': naam, 'email': email, 'tijdstip': datumtijd, 'behandeling': behandeling };

    fetch('http://127.0.0.1:5000/afspraak', {
            method: 'POST',
            headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then((response) => {
            return response.json();
        })
        .then((result) => {
            alert(result['succes']);
        });

}


fetch('http://127.0.0.1:5000/afspraken')
    .then((res) => { return res.json() })
    .then((data) => {
        let result = `<h2> Agenda </h2>`;
        data.forEach((user) => {
            const { name, email, behandeling, tijdstip } = user
            result +=
                `<div>
                 <ul class="w3-ul">
                     <li> User Full Name : ${name}</li>
                     <li> User Email : ${email} </li>
                     <li> User Behandeling : ${behandeling} </li>
                     <li> User Tijdstip : ${tijdstip} </li>
                 </ul>
              </div>`;
            document.getElementById('result').innerHTML = result;
        });
    })