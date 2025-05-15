function serch() {
    document.getElementById("search-btn").style.display='none'
    document.getElementById("search").style.display='block'
}

function coffee() {
    const orderForm = document.getElementById('coffee-form');
    const heroContent = document.getElementById('to-hidden');
    
    if (orderForm.style.display === 'block') {
        orderForm.style.display = 'none';
        heroContent.style.display = 'block';
        orderForm.classList.remove('active');
    } else {
        orderForm.style.display = 'block';
        heroContent.style.display = 'none';
        orderForm.classList.add('active');
    }
}

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#coffee-form form');
    
    form.addEventListener('submit', function(e) {
        const phoneNumber = document.querySelector('input[name="phone_number"]');
        const weight = document.querySelector('input[name="weight"]');
        
        // Phone number validation
        const phoneRegex = /^[0-9]{10,12}$/;
        if (!phoneRegex.test(phoneNumber.value)) {
            e.preventDefault();
            alert('Please enter a valid phone number (10-12 digits)');
            return;
        }
        
        // Weight validation
        const weightValue = parseInt(weight.value);
        if (isNaN(weightValue) || weightValue < 50 || weightValue > 1000) {
            e.preventDefault();
            alert('Please enter a valid weight between 50g and 1000g');
            return;
        }
    });
});