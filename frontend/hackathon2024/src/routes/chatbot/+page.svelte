<script>
  import { goto } from '$app/navigation';
  import {onMount } from 'svelte';
  const access_token = sessionStorage.getItem('access_token');
  if(!access_token){
    onMount(()=>goto('/login'));
  }
  let message = "";
  let chatMessages = "";

async function handleSend(){
  if(!message){
    return alert("Please enter a message");
  }
  const response = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({ message: message }),
      // @ts-ignore
      headers: { "Content-Type": "application/json; charset=UTF-8", "Authorization": `Bearer ${access_token}` }
    });
  const json = await response.json();
  chatMessages += json['msg'] + '\n';
}
      
</script>

<div class="chatbot-container">
  <div class="chat-messages" id="chat-messages">
    {chatMessages}
  </div>
  <div class="chat-input-container">
    <input
      bind:value={message}
      type="text"
      id="chat-input"
      class="form-control"
      placeholder="Type your message..."
    />
    <button id="send-button" on:click={handleSend}>Send</button>
  </div>
</div>
<div class="sidenav">
  <a class="nav-link" href="/">
    <img width="150" src="/logo.png" alt="logo" /></a
  >
  <a class="nav-link active" href="/flirts">Learn</a>
  <a class="nav-link" href="/chatbot">Chatbot</a><a
    class="nav-link"
    href="/preferences">Preferences</a
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
