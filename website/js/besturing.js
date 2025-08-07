function stuurActie(command) {
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ move: command })
    })
    .then(response => response.text())
    .then(data => {
        console.log('Server antwoord:', data);
    });
}


function zoekVoorstellen() {
    const input = document.getElementById("zoekveld").value;
    
    fetch(`/zoek_suggesties?q=${input}`)
        .then(response => response.json())
        .then(data => {
            const lijst = document.getElementById("suggesties");
            lijst.innerHTML = ""; // leegmaken
            data.suggesties.forEach(s => {
                const item = document.createElement("li");
                item.innerText = s;
                item.onclick = () => stuurCommand(s);  // 👈 klikactie
                lijst.appendChild(item);
            });
        });
}

function stuurCommand(waarde) {
    fetch("/verwerk_zoekopdracht", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ item: waarde })
    })
    .then(response => response.text())
    .then(data => {
        console.log("Server antwoord:", data);
        alert(`Commando verstuurd: ${waarde}`);
    });
}   


