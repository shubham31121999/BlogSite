// static/js/base.js

document.addEventListener('DOMContentLoaded', function () {
    const postButton = document.getElementById('post-button');
    const hoverCard = document.getElementById('hover-card');
    const closeCard = document.getElementById('close-card');
    const postForm = document.getElementById('create-post-form');

    // Show the hover card when the "Create Post" button is clicked
    postButton.addEventListener('click', function () {
        hoverCard.classList.add('active');
    });

    // Hide the hover card when "Cancel" is clicked
    closeCard.addEventListener('click', function () {
        hoverCard.classList.remove('active');
    });

    // Handle form submission
    postForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(postForm);

        fetch(postForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // CSRF token for security
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            console.log('Success:', data);
            // Handle success (e.g., show a message, close the card, etc.)
            hoverCard.classList.remove('active');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Function to get the CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});