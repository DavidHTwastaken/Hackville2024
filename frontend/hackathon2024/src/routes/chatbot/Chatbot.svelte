<script>
    /**
   * @param {string} message
   */
    async function post_message(message){
        return await fetch("/api/chat",{
            method: "POST",
            body: JSON.stringify({message: message}),
            headers: [{"Content-type": "application/json; charset=UTF-8"}]
        });
    }

    document.getElementById("send-button")?.addEventListener('click',(e)=>{
        const message = document.getElementById('chatInput')?.textContent;
        if(!message){
            return alert("Please enter a message");
        }
        post_message(message).then(async (res)=>{
            const json = await res.json();
            try{
            
}catch(e){
    console.log(e);
    alert("Message failed");
}        
}
);
    });
</script>

<div class="chatbot-container">
  <div class="chat-messages" id="chat-messages">
    <!-- Chat messages will be appended here -->
  </div>
  <div class="chat-input-container">
    <input
      type="text"
      id="chat-input"
      class="form-control"
      placeholder="Type your message..."
    />
    <button id="send-button">Send</button>
  </div>
</div>
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
  .chatbot-container {
    width: 100%;
    max-width: 350px;
    height: 500px;
    margin: 2rem auto;
    display: flex;
    flex-direction: column;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }

  .chat-messages {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    background: #fff;
    height: 400px;
  }

  .chat-input-container {
    padding: 10px;
    background: #f9f9f9;
  }

  .chat-message {
    padding: 10px;
    margin: 5px 0;
    border-radius: 25px;
    color: white;
    max-width: 80%;
  }

  .user-message {
    background-color: #667eea;
    margin-left: auto;
    margin-right: 0;
  }

  .bot-message {
    background-color: #764ba2;
    margin-left: 0;
    margin-right: auto;
  }

  #chat-input {
    width: calc(100% - 90px);
    padding: 10px;
    margin-right: 10px;
    border: none;
    border-radius: 25px;
  }

  #send-button {
    width: 70px;
    background-color: #667eea;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 15px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  #send-button:hover {
    background-color: #575fcf;
  }
</style>
