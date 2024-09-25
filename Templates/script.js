// script.js
document.getElementById('file-upload').addEventListener('change', function() {
    const fileStatus = document.getElementById('file-status');
    const fileName = this.files[0] ? this.files[0].name : 'No file chosen';
    fileStatus.textContent = fileName; // Update the status message
});
