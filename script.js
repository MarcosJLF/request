document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const user = document.getElementById('loginUsername').value;
    const senha = document.getElementById('loginPassword').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user, senha })
        });

        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();

        if (data.success) {
            alert('Login realizado com sucesso!');
            window.location.href = '/pagina-principal'; // Altere conforme necessário
        } else {
            alert(`Erro no login: ${data.Erro || 'Credenciais inválidas'}`);
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao conectar ao servidor. Verifique sua conexão.');
    }
});

document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const user = document.getElementById('registerUsername').value;
    const senha = document.getElementById('registerPassword').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user, senha })
        });

        if (!response.ok) {
            throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();

        alert(data.Success || 'Cadastro realizado com sucesso!');
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao conectar ao servidor. Tente novamente.');
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
}