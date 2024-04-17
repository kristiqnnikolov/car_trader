window.onload = function () {
    // "This function hides english error messages from Django"
    var liElements = document.querySelectorAll('li');
    for (var i = 0; i < liElements.length; i++) {
        var li = liElements[i];

        if (li.innerText.toLowerCase().indexOf('password') !== -1 || li.textContent.toLowerCase().indexOf('password') !== -1) {
            li.style.display = 'none';
        }
    }
};
