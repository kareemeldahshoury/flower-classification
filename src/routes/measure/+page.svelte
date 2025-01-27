<script lang="ts">
  let sepal_length = '';
  let sepal_width = '';
  let pedal_length = '';
  let pedal_width = '';
  let prediction = '';
  let errorMessage = '';

  async function handleSubmit(event: Event): Promise<void> {
    event.preventDefault()

    const data = {
      inputs: [
      parseFloat(sepal_length),
      parseFloat(sepal_width),
      parseFloat(pedal_length),
      parseFloat(pedal_width)
    ]
  }
  try {
    //send the data to the flask server
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 
        'content-type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if(!response.ok){
      throw new Error("Failed to fetch data")
    }

    const result = await response.json();
    console.log('API Response:', result);
    prediction = result.prediction;
    sepal_length = '';
    sepal_width = '';
    pedal_length = '';
    pedal_width = '';

  } catch (error) {
    if (error instanceof Error) {
        errorMessage = error.message;
      } else {
        errorMessage = 'An unknown error occurred.';
      }
      console.error('Error:', errorMessage); // Debugging: Log errors
    }
    // let sepal_length = '';
    // let sepal_width = '';
    // let pedal_length = '';
    // let pedal_width = '';
}
</script>

<div class="h-screen flex flex-col items-center justify-center bg-custom-teal bg-gradient-to-b from-custom-brown to-custom-dark-brown">

  {#if prediction}
    <div class="text-6xl font-bold text-iris mt-10 mb-10">
      <h2>Prediction: {prediction}</h2>
      {#if prediction == 'Setosa'}
        <img src="/setosa_iris.jpg" class="w-52 h-48 mx-auto mt-4" alt="setosa iris">
      {:else if prediction == 'Virginica'}
        <img src="/virginica_iris.jpg" class="w-52 h-48 mx-auto mt-4" alt="setosa iris">
      {:else}
        <img src="/versicolor_iris.jpeg" class="w-52 h-48 mx-auto mt-4" alt="setosa iris">
      {/if}
    </div>
  {/if}

  <form on:submit={handleSubmit} class="flex flex-col justify-center items-center">
    <h1 class="text-2xl font-bold text-iris mb-10">Measurement Classification</h1>
    <input class="m-1" type="number" step="0.01" bind:value={sepal_length} placeholder=sepal_length/>
    <input class="m-1" type="number" step="0.01" bind:value={sepal_width} placeholder=sepal_width/>
    <input class="m-1" type="number" step="0.01" bind:value={pedal_length} placeholder="pedal_length"/>
    <input class="m-1" type="number" step="0.01" bind:value={pedal_width} placeholder="pedal_width"/>
    <button class="font-bold mt-10 text-iris">Enter</button>
  </form>
</div>


