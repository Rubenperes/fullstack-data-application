<script>
  let inputValue = '';
  let imageUrl = ''; // Ajoutez cette ligne
  let apiUrl = 'https://api.example.com/search';
  let apiKey = 'YOUR_API_KEY_HERE';

  async function handleSubmit(event) {
    event.preventDefault();
    
    try {
      // Placeholder pour l'appel à l'API
      // const response = await fetch(`${apiUrl}?query=${encodeURIComponent(inputValue)}&key=${apiKey}`);
      
      // Placeholder pour le traitement de la réponse API
      // const data = await response.json();
      
      // Placeholder pour la récupération de l'image
      // imageUrl = data.results[0]?.urls?.regular || '';
      
      alert(`Image trouvée : ${imageUrl}`); // Placeholder pour afficher un message d'alerte
    } catch (error) {
      console.error('Erreur lors du chargement de l\'image:', error);
      alert('Une erreur s\'est produite lors du chargement de l\'image.');
    }
  }

  function handleImageChange(event) {
    imageUrl = event.target.value;
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <label for="input-field">Entrez votre texte :</label>
  <input type="text" id="input-field" bind:value={inputValue} />
  <br />
  <button type="submit">Chercher une image</button>
</form>

<p>Votre texte entré : {inputValue}</p>

<div class="image-container">
  <img src={imageUrl ? imageUrl : ''} alt="Image affichée" placeholder="N" />
</div>
