<script>
    /**
   * @param {string} email
   * @param {string} password
   */
    async function post_email_pass(email, password){
        return await fetch("/api/signup",{
            method: "POST",
            body: JSON.stringify({email: email, password: password}),
            headers: {"Content-Type": "application/json; charset=UTF-8"}
        });
    }

    document.getElementById("submit")?.addEventListener('click',(e)=>{
<<<<<<< HEAD
=======
        console.log("hello")
>>>>>>> parent of 2f006da (ad)
        const email = document.getElementById('inputEmail')?.textContent;
        const password = document.getElementById('inputPassword')?.textContent;
        if(!email || !password){
            return alert("Please enter an email and a password");
        }
        post_email_pass(email, password).then(async (res)=>{
            const json = await res.json();
            try{
            sessionStorage.setItem("access_token", json['access_token']);
}catch(e){
    console.log(e);
    alert("Login failed");
}        
}
).catch((e)=>console.log(e)
);
    });
</script>

<main>
    <div class="login-container">
        <div class="login-box">
            <!-- Form with HTMX attributes -->
            <form id="creatAccountForm">
                <div class="form-group">
                    <label for="inputEmail">Email address: </label>
                    <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <div class="form-group">
                    <label for="inputPassword">Password: </label>
                    <input type="password" class="form-control" id="inputPassword" placeholder="Password">
                </div>
                <button id="submit" type="button" class="btn btn-primary">Create Account</button>
            </form>
            <p class="forgot-password">
                <a href="Login.svelte">Login</a>
            </p>
        </div>
    </div>
    <!-- Placeholder where the server's response will be placed -->
    <div id="responseTarget"></div>
</main>

<style>
    main {
        height: 100%;
        margin: 0;
        font-family: Georgia, sans-serif;
        background-image: url("/background-image.png");
        background-size: cover;/* Fancy background */
    }
    .login-container {
        min-height: 100vh; /* Make it fit the full screen */
        display: flex;
        align-items: center; /* Align vertically */
        justify-content: center; /* Align horizontally */
    }
    .login-box {
        width: 100%;
        max-width: 350px;
        border-radius: 50px; /* Make edges round */
        padding: 40px; /* Increase padding */
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2), 0 0 0 20px rgba(255, 255, 255, 0.9); /* Cloud-like shadow */
        background: rgba(255, 255, 255, 0.95);
        opacity: .80;
    }
    .form-group {
        margin-bottom: 1rem;
    }
    .form-control {
        border-radius: 5px;
        border: 2px solid #d1d3e2;
        box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075); /* Subtle inner shadow */
        padding: 15px; /* Larger padding */
        font-size: 16px; /* Larger font size */
        transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; /* Smooth transition for interactions */
    }
    .form-control:focus {
        border-color: #9d5b6f; /* Highlight color when focused */
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.25); /* Outer glow effect when focused */
    }

    .btn-primary {
        background-color: #fbe9e3;
        border: none;
        border-radius: 5px;
        padding: 10px;
        color: #fff;
        font-size: 15px;
        line-height: 1.5;
        margin-top: 10px;
        width: 100%; /* Make the button fit the width of the box */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .btn-primary:hover {
        background-color: #f8aab0;
    }
    .forgot-password, .register {
        text-align: center;
        margin-top: 15px;
    }
</style>
