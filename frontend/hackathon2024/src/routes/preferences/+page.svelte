<script>
    import { onMount } from "svelte";

    let formData = "";
    let gender = "";
    let age = "";
    let confidenceLevel = "";
    let levelOfWarmness = "";
    let levelOfPlayfulness = "";
    let levelOfRudeness = "";
    let levelOfSpicyness = "";

    function handleFormSubmit() {
        let formData = {
            gender: `${gender}`,
            age: `${age}`,
            confidenceLevel: `${confidenceLevel}`,
            levelOfWarmness: `${levelOfWarmness}`,
            levelOfPlayfulness: `${levelOfPlayfulness}`,
            levelOfRudeness: `${levelOfRudeness}`,
            levelOfSpicyness: `${levelOfSpicyness}`,
        };

        console.log(formData);

        const saveFormData = async () => {
            try {
                const response = await fetch("", {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify(formData),
                });

                if (response.ok) {
                    console.log("Form data sent successfully");
                } else {
                    console.log("Error sending from data:", response.statusText);
                }
            } catch (error) {
                console.error("Error sending from data: ", error);
            }
        };
    }

    onMount(() => {
        console.log("Component is mounted!");
    });

    console.log(formData);
</script>

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

    <input
            type="button"
            class="pref-btn"
            value="Save"
            on:click={handleFormSubmit}
    />
</main>

<link
        rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        crossorigin="anonymous"
/>

<style>
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
