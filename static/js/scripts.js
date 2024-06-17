let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

// Gestion du scroll de la fenêtre
window.onscroll = () => {
    let scrollY = window.scrollY;

    sections.forEach(sec => {
        let secTop = sec.offsetTop - 150; // Position du haut de la section
        let secHeight = sec.offsetHeight; // Hauteur de la section
        let id = sec.getAttribute('id'); // ID de la section

        if (scrollY >= secTop && scrollY < secTop + secHeight) {
            // Supprimer la classe 'active' de tous les liens de navigation
            navLinks.forEach(link => {
                link.classList.remove('active');
            });

            // Ajouter la classe 'active' au lien de navigation correspondant à la section visible
            document.querySelector(`header nav a[href="#${id}"]`).classList.add('active');
        }
    });
};

// Gestion du clic sur l'icône de menu
menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x'); // Basculer la classe pour changer l'icône du menu
    navbar.classList.toggle('active'); // Afficher ou masquer la barre de navigation
};
