let globalData = []

const loadingText = 'Reading....';
const PRODUCT_URL = 'https://dummyjson.com/products/search?q='

const categorySelect = document.getElementById('category-select');

// Modal Elements
const modal = document.getElementById('product-modal');
const modalTitle = document.getElementById('modal-title');
const modalImage = document.getElementById('modal-image');
const modalDescription = document.getElementById('modal-description');
const modalPrice = document.getElementById('modal-price');
const modalRating = document.getElementById('modal-rating');
const closeBtn = document.querySelector('.close-btn');

function filterAndDisplay(){
    const selectedCategory = categorySelect.value;
    const filtered = globalData.filter((product) => {
        const matchesCategory = selectedCategory === '' || product.category === selectedCategory;
        return matchesCategory;
    })

    displayData(filtered);
}

function fetchData(searchTerm='') {
    try {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<div class="loading">${loadingText}</div>`
        fetch( `${PRODUCT_URL}${searchTerm}`)
            .then((response) => response.json())
            .then((data) => {
                globalData = data.products;
                console.log(globalData);
                displayData(globalData);
            });
    } catch (error) {
        console.error('Error during fetching data: ',  error);
        document.getElementById('results').innerHTML = 
        '<div class="loading">Error occurred. Please try again.</div>'
    }
}

function displayData(products){
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    
    if (products.length === 0){
        resultsDiv.innerHTML = '<div class="loading">Product not found</div>';
        return;
    }

    products.forEach((product) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';
        itemDiv.innerHTML = `
            <img src="${product.thumbnail}" alt=${product.title}/>
            <h3>${product.title}</h3>
            <p>Price: $${product.price}</p>
            <p>Brand: ${product.brand}</p>
            <p>Category: ${product.category}</p>
            <p>Rating: ${product.rating}</p>
            <p>${product.description}</p>
        `;
        // add event listener
        itemDiv.addEventListener('click', () => showModal(product));
        resultsDiv.appendChild(itemDiv);
    })
}

function showModal(product){
    modalTitle.textContent = product.title;
    modalImage.src = product.thumbnail;
    modalDescription.textContent= product.description;
    modalPrice.textContent = product.price;
    modalRating.textContent = product.rating;
    modal.style.display = 'block';
}

const searchData = () => {
    const searchTerm = document.getElementById('searchInput').value;
    fetchData(searchTerm);
}

function debounce(func, timeout = 3000){
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => func.apply(this, args), timeout);
    }
}

const debouncedSearch = debounce(searchData);

document.getElementById('searchButton').addEventListener('click', searchData);
document.getElementById('searchInput').addEventListener('keyup', (e) => {
    if(e.key === 'Enter'){
        searchData();
    } else {
        debouncedSearch();
    }
})

categorySelect.addEventListener('change', filterAndDisplay);

closeBtn.addEventListener('click', () => modal.style.display = 'none');
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});


fetchData();