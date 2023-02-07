const cupcakeList = document.querySelector('#cupcake-list');
const getBtn = document.querySelector('#get-button');
const createBtn = document.querySelector('#create-btn');
const cupcakeForm = document.querySelector('#add-cupcake-form')

async function getCupcakes() {
    cupcakeList.innerHTML = '';

    let cupcakes = await axios.get('/api/cupcakes');
    console.log(cupcakes);

    for( cupcakes of cupcakes.data.cupcakes){
        let cupcake = document.createElement('li');
        cupcake.classList.add('list-group-item');
        cupcake.innerText = `Flavor: ${cupcakes.flavor} || Rating: ${cupcakes.rating} || Size:${cupcakes.size}`;
        cupcakeList.append(cupcake);
    }
};

cupcakeForm.addEventListener('submit', async (e) => {
    e.preventDefault()
    let flavor = document.getElementById('flavor-input').value;
    let size = document.getElementById('size-input').value;
    let rating = document.getElementById('rating-input').value;
    let image = document.getElementById('image-input').value;

    const addCupcake = await axios.post('/api/cupcakes', {
        flavor,
        rating,
        size,
        image
    });
    cupcakeForm.reset();
    getCupcakes();
})

getCupcakes()







