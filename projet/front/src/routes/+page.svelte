<script>
  import { writable } from 'svelte/store';
  import { goto } from '$app/navigation';

  const username = writable('');
  const password = writable('');
  const confirmPassword = writable('');

  $username = '';
  $password = '';
  $confirmPassword = '';

  let isRegistering = false;

  $: isFormValid = username && password && confirmPassword && password === confirmPassword;

  async function handleSubmit(event) {
    event.preventDefault();
    console.log('Attempt:', isRegistering ? 'Registration' : 'Login', $username, $password);
    
    if (isRegistering) {
      if ($password !== $confirmPassword) {
        alert("Les mots de passe ne correspondent pas");
        return;
      }
      try {
      const response = await fetch('http://localhost:5000/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: $username, password: $password })
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }

      const result = await response.json();
      console.log('User registered successfully:', result);
      
      $username = '';
      $password = '';
      $confirmPassword = '';
      isRegistering = false;
    } catch (error) {
      console.error('Error:', error);
      alert(error.message || 'An unexpected error occurred');
    }
    } else {
      try {
      const response = await fetch('http://localhost:5000/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: $username, password: $password })
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const result = await response.json();
      console.log('User logged successfully:', result);
      
      $username = '';
      $password = '';

      //navigate to /homepage
      goto('/homepage');

    } catch (error) {
      console.error('Error:', error);
      alert(error.message || 'An unexpected error occurred');
    }
    }
  }

  function toggleForm() {
    isRegistering = !isRegistering;
  }
</script>

<div class="login-container">
  <h2>{isRegistering ? 'Enregistrer' : 'Connexion'}</h2>
  
  {#if isRegistering}
    <form on:submit|preventDefault={handleSubmit}>
      <label for="username">Nom d'utilisateur :</label>
      <input type="text" id="username" bind:value={$username} required>

      <div class="password-input">
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" bind:value={$password} required>
      </div>

      <div class="password-input">
        <label for="confirmPassword">Confirmer le mot de passe :</label>
        <input type="password" id="confirmPassword" bind:value={$confirmPassword} required>
      </div>

      <button type="submit">{isRegistering ? 'Enregistrer' : 'Basculer'}</button>
      
      <p class="error-message">Veuillez remplir tous les champs.</p>
    </form>
  {:else}
    <form on:submit|preventDefault={handleSubmit}>
      <label for="username">Nom d'utilisateur :</label>
      <input type="text" id="username" bind:value={$username} required>

      <div class="password-input">
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" bind:value={$password} required>
      </div>

      <button type="submit">Connexion</button>
      
      <p class="error-message">Nom d'utilisateur ou mot de passe invalide.</p>
    </form>
  {/if}

  <button class="toggle-form" on:click={toggleForm}>{isRegistering ? 'Déjà enregistré? Connectez-vous' : 'Pas encore enregistré? Enregistrez-vous'}</button>
</div>


<style>
  :global(body) {
    background-color: #f5f7fa;
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    color: #333;
  }

  .login-container {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 40px;
    width: 350px; /* Largeur augmentée */
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  h2 {
    font-size: 24px;
    margin-bottom: 20px;
    color: #333;
  }

  form {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  label {
    margin-bottom: 8px;
    font-weight: bold;
    color: #666;
  }

  input {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
    transition: border-color 0.3s ease;
  }

  input:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
  }

  button {
    background-color: #007bff;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 20px;
    width: 100%;
  }

  button:hover {
    background-color: #0056b3;
  }

  .error-message {
    color: #dc3545;
    font-size: 14px;
    margin-top: 5px;
    display: none;
  }

  .password-input {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }

  .toggle-form {
    margin-top: 15px;
    padding: 10px;
    background-color: #f8f9fa;
    border: none;
    cursor: pointer;
    font-size: 14px;
    color: #007bff;
    transition: color 0.3s ease;
  }

  .toggle-form:hover {
    color: #0056b3;
  }
</style>