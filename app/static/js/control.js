document.addEventListener('DOMContentLoaded', function() {
    const commandForm = document.getElementById('command-form');
    const commandInput = document.getElementById('command');
    const commandStatus = document.getElementById('command-status');

    // Pre-submit validation could go here
    commandForm.addEventListener('submit', function(event) {
        const command = commandInput.value.trim();

        // Simple validation example
        if (!command) {
            event.preventDefault(); // Prevent form submission
            updateStatus('Please enter a command.', 'error');
            return false;
        }

        // Clear status
        updateStatus('', '');
    });

    // Function to update command status with message
    function updateStatus(message, status) {
        commandStatus.textContent = message;
        commandStatus.className = ''; // Clear previous status classes
        if (status === 'error') {
            commandStatus.classList.add('error-status');
        } else if (status === 'success') {
            commandStatus.classList.add('success-status');
        }
    }

    // Example HTMX event listener for handling after request
    document.body.addEventListener('htmx:afterRequest', function(event) {
        if (event.detail.path === '/send-command') {
            commandInput.value = ''; // Clear input after successful submission
        }
    });

    // Example HTMX event listener for handling responses
    document.body.addEventListener('htmx:afterOnLoad', function(event) {
        let response = event.detail.xhr.response;
        try {
            let jsonResponse = JSON.parse(response);
            if (jsonResponse.status === 'Success') {
                updateStatus(jsonResponse.message, 'success');
            } else {
                updateStatus(jsonResponse.message, 'error');
            }
        } catch (e) {
            // In case the response is not JSON or another error occurs
            updateStatus('Error processing the response.', 'error');
        }
    });
});
