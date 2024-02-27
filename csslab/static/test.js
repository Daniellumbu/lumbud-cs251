document.addEventListener('DOMContentLoaded', function() {
    var textElement = document.getElementById('hello');
    textElement.addEventListener('click', function() {
        textElement.style.color = 'red';
    });
});
