<script>
  let username = '';
  let password = '';

  $: isFormValid = username && password;

  function handleSubmit(event) {
    event.preventDefault();
    console.log('Login attempt:', { username, password });
    // Here you would typically send this data to your server
  }
</script>

<div class="login-container">
  <h2>Login</h2>
  
  <form on:submit|preventDefault={handleSubmit}>
    <label for="username">Username:</label>
    <input type="text" id="username" bind:value={username} required>

    <div class="password-input">
      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} required>
      <button class="toggle-password" on:click={() => password = password === '' ? '•' * password.length : ''}>Show Password</button>
    </div>

    <button type="submit">Login</button>
    
    {#if isFormValid}
      <p class="success-message">Please wait while we log you in...</p>
    {:else if username === '' || password === ''}
      <p class="error-message">Please fill out all fields.</p>
    {:else}
      <p class="error-message">Invalid username or password.</p>
    {/if}
  </form>
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
    width: 350px; /* Increased width */
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

  .success-message {
    color: #28a745;
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

  .toggle-password {
    background-color: #f8f9fa;
    border: none;
    cursor: pointer;
    padding: 10px;
    font-size: 14px;
    color: #007bff;
    transition: color 0.3s ease;
  }

  .toggle-password:hover {
    color: #0056b3;
  }
</style>
