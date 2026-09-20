const programmingButton =
    document.getElementById("programmingButton");

const persianButton =
    document.getElementById("persianButton");

const jokeContainer =
    document.getElementById("jokeContainer");


const RandomButton=
    document.getElementById("RandomButton")

async function getJoke(url) {

    try {
        jokeContainer.innerHTML=`<p>Take a moment...</p>`;
        const response = await fetch(url);
        

        if (!response.ok) {
            throw new Error("Failed to fetch joke");
        }

        const data = await response.json();

        jokeContainer.innerHTML = `
            <h2>${data.joke}</h2>
            <p>${data.answer}</p>
            <small>Category: ${data.category}</small>
        `;

    } catch (error) {

        jokeContainer.innerHTML = `
            <p>❌ Failed to get joke!</p>
        `;

        console.error(error);
    }
}


programmingButton.addEventListener("click", () => {

    getJoke("/joke_api_programming");

});


persianButton.addEventListener("click", () => {

    getJoke("/joke_api_persian");

});

RandomButton.addEventListener("click",()=>{
    getJoke("/joke_Random_api");
})