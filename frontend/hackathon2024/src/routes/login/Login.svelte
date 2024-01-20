<script>

</script>

<main>
    <div class="login-container">
        <div class="login-box">
            <!-- Form with HTMX attributes -->
            <form id="loginForm" hx-post="/login-endpoint" hx-target="#responseTarget" hx-swap="outerHTML">
                <div class="form-group">
                    <label for="inputEmail">Email address: </label>
                    <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <div class="form-group">
                    <label for="inputPassword">Password: </label>
                    <input type="password" class="form-control" id="inputPassword" placeholder="Password">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
            <p class="forgot-password">
                <a href="#">Forgot password?</a>
            </p>
            <p class="register">
                Don't have an account? <a href="#">Register</a>
            </p>
        </div>
    </div>
    <!-- Placeholder where the server's response will be placed -->
    <div id="responseTarget"></div>
</main>

    <style>
    body, html {
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
        border-color: #80bdff; /* Highlight color when focused */
        box-shadow: 0 0 8px rgba(0, 123, 255, 0.25); /* Outer glow effect when focused */
    }

    .btn-primary {
        background-color: #fad8ff;
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
        background-color: #ffa1db;
    }
    .forgot-password, .register {
        text-align: center;
        margin-top: 15px;
    }
</style>
