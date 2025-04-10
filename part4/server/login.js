document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            // On récupère les valeurs du formulaire
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Vérification côté client (optionnel mais propre)
            if (!email || !password) {
                alert('Please enter both email and password.');
                return;
            }

            try {
                // On envoie la requête POST vers l'API de login
                const response = await fetch('http://localhost:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();

                if (response.ok) {
                    // ✅ Connexion réussie
                    document.cookie = 'isLoggedIn=true; path=/';

                    // Optionnel : tu peux stocker aussi l'ID de l'utilisateur pour t'en servir plus tard
                    document.cookie = `token=${data.access_token}; path=/`;

                    alert('Login successful!');
                    window.location.href = 'index.html'; // Redirection vers la page d'accueil ou autre
                } else {
                    // ❌ Erreur côté serveur (mauvais identifiants etc.)
                    alert(data.error || 'Login failed. Please check your credentials.');
                }

            } catch (error) {
                console.error('Error during login:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }
});
