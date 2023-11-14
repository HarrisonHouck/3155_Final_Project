let cartItems = [];
let total = 0;

// Show Thanksgiving sale popup after a delay
document.addEventListener("DOMContentLoaded", function() {
    // Show the fullscreen popup after a delay
    setTimeout(() => {
        const fullscreenPopup = document.getElementById('fullscreenPopup');
        fullscreenPopup.style.display = 'flex';
    }, 2000);
});

function closeFullscreenPopup() {
    const fullscreenPopup = document.getElementById('fullscreenPopup');
    fullscreenPopup.style.display = 'none';
}


function addToCart(dish, price) {
    cartItems.push({ dish, price });
    total += price;

    // Update cart display
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartItemsList = document.getElementById('cartItems');
    const totalDisplay = document.getElementById('total');

    // // Clear previous items
    // cartItemsList.innerHTML = '';

    // // Display current items
    // cartItems.forEach(item => {
    //     const li = document.createElement('li');
    //     li.textContent = `${item.dish} - $${item.price.toFixed(2)}`;
    //     cartItemsList.appendChild(li);
    // });

    // Display total
    totalDisplay.textContent = total.toFixed(2);
}

function openCheckout() {
    const checkoutModal = document.getElementById('checkoutModal');
    checkoutModal.style.display = 'block';
}

function closeCheckout() {
    const checkoutModal = document.getElementById('checkoutModal');
    checkoutModal.style.display = 'none';
}

function submitOrder() {
    const name = document.getElementById('name').value;
    const contactNumber = document.getElementById('contactNumber').value;
    const address = document.getElementById('address').value;

    // Simulate order submission (in a real application, this would involve sending a request to the server)
    alert(`Order Placed!\nName: ${name}\nContact Number: ${contactNumber}\nAddress: ${address}`);
    
    // Clear cart and close checkout modal
    cartItems = [];
    total = 0;
    updateCartDisplay();
    closeCheckout();
}

