document.addEventListener('DOMContentLoaded', (event) => {
    const texte = document.getElementById('texte');
    const contenuInitial = texte.innerHTML;
    
    document.querySelectorAll('input[name="choix"]').forEach((elem) => {
        elem.addEventListener("change", function(event) {
            switch (event.target.value) {
                case '0':
                    texte.innerHTML = contenuInitial;
                    break;
                case '1':
                    texte.innerHTML = "<h2>Débutant</h2> \
                    <p>Dans cette variante, le joueur qui a donné la combinaison place les pions blancs et noirs à la place exacte \
                    qu'ils occupent dans la combinaison</p>";
                    break;
                case '2':
                    texte.innerHTML = "<h2>Paramétrable</h2> \
                    <p>Dans cette variante, on peut paramétrer le nombre de couleurs que peut prendre la combinaison, \
                    ainsi que le nombre de pions qui constituent la combinaison</p>";
                    break;
            }
        });
    });
});

document.getElementById('secretForm').addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();

    var secretCode = document.getElementById('secretCode').value;

    if (secretCode === 'mastercheat') {
        window.location.href = 'page_secrete.html';
    } else {
        alert('Code secret incorrect');
    }
});

document.addEventListener('DOMContentLoaded', (event) => {
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
});
