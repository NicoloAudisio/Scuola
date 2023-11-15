const somma = async()=>{
    await fetch('https://v2.jokeapi.dev/joke/Programming?type=single')
    .then(res => res.json())
    .then(json => console.log(json.joke))
}

somma().then(console.log("ANDREA GIORDANO"))