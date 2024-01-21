<script>
  let gender = "male";
  let age = 18; // Default age value
  let confidenceLevel = 3;
  let levelOfWarmness = 1;
  let levelOfPlayfulness = 2;
  let levelOfRudeness = 5;
  let levelOfSpicyness = 5;
</script>

<div class="sidenav">
  <a class="nav-link" href="/src/routes/+page.svelte">
    <img width="150" src="/logo.png" alt="logo" /></a
  >
  <a class="nav-link active" href="/src/routes/flirts/flirts.svelte">Learn</a>
  <a class="nav-link" href="/src/routes/chatbot/chatbot.svelte">Chatbot</a><a
    class="nav-link"
    href="/src/routes/preferences/preferences.svelte">Preferences</a
  >
  <!-- Add more links as needed -->
</div>

<main>
  <h1>Choose your preferences:</h1>
  <label>
    Gender:
    <select bind:value={gender}>
      <option value="male">Male</option>
      <option value="female">Female</option>
      <option value="other">Other</option>
    </select>
  </label>

  <label>
    Age:
    <input type="text" min="18" max="50" bind:value={age} />
    <!-- <span class="output">{age}</span> -->
  </label>

  <label>
    Confidence Level:
    <input
      type="range"
      class="slider"
      min="1"
      max="5"
      bind:value={confidenceLevel}
    />
    <span class="output">{confidenceLevel}</span>
  </label>

  <label>
    Cold to Warm:
    <input
      type="range"
      class="slider"
      min="1"
      max="5"
      bind:value={levelOfWarmness}
    />
    <span class="output">{levelOfWarmness}</span>
  </label>

  <label>
    Playfulness Level:
    <input
      type="range"
      class="slider"
      min="1"
      max="5"
      bind:value={levelOfPlayfulness}
    />
    <span class="output">{levelOfPlayfulness}</span>
  </label>

  <label>
    Rude or polite:
    <input
      type="range"
      class="slider"
      min="1"
      max="5"
      bind:value={levelOfRudeness}
    />
    <span class="output">{levelOfRudeness}</span>
  </label>

  <label>
    Spicyness:
    <input
      type="range"
      class="slider"
      min="1"
      max="5"
      bind:value={levelOfSpicyness}
    />
    <span class="output">{levelOfSpicyness}</span>
  </label><br />

  <input type="button" class="pref-btn" value="Save" />
</main>

<link
  rel="stylesheet"
  href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
  integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
  crossorigin="anonymous"
/>

<style>
  .sidenav {
    height: 100%;
    width: 200px;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #f4f4f4; /* Background color of the sidebar */
    border-right: 2px solid #ddd; /* Outline color */
    padding-top: 20px;
  }

  .sidenav a {
    padding: 8px 16px;
    text-decoration: none;
    font-size: 18px;
    color: #333; /* Text color */
    display: block;
  }

  .sidenav a:hover {
    background-color: #ddd; /* Hover color */
  }

  h1 {
    text-align: center;
    padding-bottom: 20px;
  }

  main {
    padding: 300px;
    padding-top: 0px;
  }

  label {
    display: block;
    margin-bottom: 15px;
  }

  input,
  select,
  span.output {
    display: block;
    margin-top: 5px;
  }

  input[type="text"],
  input[type="range"],
  select {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
  }

  span.output {
    font-weight: bold;
    color: rgb(34, 31, 31);
  }

  .pref-btn {
    background-color: #ffc1d4;
    color: #000000;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
    text-align: center;
  }

  .pref-btn:hover {
    background-color: #0056b3;
  }
</style>
