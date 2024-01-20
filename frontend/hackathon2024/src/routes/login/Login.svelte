<script>

</script>

<main>
    <div class="login-container">
        <div class="login-box">
            <form>
                <div class="form-group">
                    <label for="inputEmail">Email address</label>
                    <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <div class="form-group">
                    <label for="inputPassword">Password</label>
                    <input type="password" class="form-control" id="inputPassword" placeholder="Password">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
                <p class="forgot-password">
                    <a href="#">Forgot password?</a>
                </p>
                <p class="register">
                    Don’t have an account? <a href="#">Register</a>
                </p>
            </form>
        </div>
    </div>
</main>

    <style>
    body, html {
        height: 100%;
        margin: 0;
        font-family: 'Nunito', sans-serif;
        background: linear-gradient(to right, #6dd5ed, #2193b0); /* Fancy background */
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
        padding: 20px;
        background: rgba(255, 255, 255, 0.9); /* Slightly transparent white */
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
    }
    .form-group {
        margin-bottom: 1rem;
    }
    .form-control {
        border-radius: 5px;
        border: 1px solid #d1d3e2;
    }
    .btn-primary {
        background-color: #4e73df;
        border: none;
        border-radius: 5px;
        padding: 10px;
        color: #fff;
        font-size: 15px;
        line-height: 1.5;
        margin-top: 10px;
    }
    .btn-primary:hover {
        background-color: #2e59d9;
    }
    .forgot-password, .register {
        text-align: center;
        margin-top: 15px;
    }
</style>
</style>
