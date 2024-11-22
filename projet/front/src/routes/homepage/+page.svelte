<script>
    import { onMount } from 'svelte';

    let inputValue = '';    
    let imageUrl = '';

    async function handleSubmit(event) {
        event.preventDefault();
        
        try {
            const response = await fetch('http://localhost:5000/gen-img/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt : inputValue})
            });

            const data = await response.text();

            console.log({data});

            imageUrl = data.replace(/"/g, '').trim();

            console.log({imageUrl});

        } catch (error) {
            console.error('Erreur lors du chargement de l\'image:', error);
            alert('Une erreur s\'est produite lors du chargement de l\'image.');
        }
    }

    function handleChange(event) {
        inputValue = event.target.value;
    }
</script>

<div class="img-generation">

  <h1> Générateur d'image </h1>

  <form on:submit|preventDefault={handleSubmit}>
      <label for="input-field">Entrez votre texte :</label>
      <input type="text" id="input-field" bind:value={inputValue} on:input={handleChange} />
      <br />
      <button type="submit">Générer une image</button>
  </form>

  <div class="button-container">
    <button type="submit" class="save-button">Enregistrer l'image</button>
    <button type="submit" class="view-button">Afficher mes images</button>
  </div>

</div>

{#if imageUrl}
    <div class="image-container">
        <img src={imageUrl} alt="Generated image" />
    </div>
{/if}

<style>

    .img-generation {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 40px;
        padding-top: 50px;
        width: 350px; /* Largeur augmentée */
        max-width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0 auto;
    }

    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        padding-top: 20px;
    }


    h1 {
      text-align: center;
      justify-content: center;
      padding-top: 5px;
      padding-bottom: 5px;
    }


    form {
        margin-bottom: 20px;
    }

    label {
        display: block;
        margin-bottom: 10px;
    }

    input[type="text"] {
        width: 100%;
        padding: 8px;
        border-radius: 4px;
        border: 1px solid #ccc;
        padding-bottom: 5px;
    }

    button {
        background-color: #007bff;
        color: white;
        padding: 8px 16px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }

    .button-container {
        display: flex;
        justify-content: space-between;
        width: 100%;
        margin-top: auto;
        padding-top: 20px;
    }

    .save-button {
        float: right;
    }

    .view-button {
        float: left;
    }

</style>

