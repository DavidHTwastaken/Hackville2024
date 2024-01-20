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
</style>
