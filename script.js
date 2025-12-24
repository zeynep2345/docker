async function fetchData() {
    const res = await fetch('http://localhost:5000/data');
    const data = await res.json();
    document.getElementById('bitcoin').innerText = `Bitcoin Price: $${data.bitcoin_usd}`;
    document.getElementById('joke').innerText = `Random Joke: ${data.joke}`;
}
