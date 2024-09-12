options.plugins.push(RevealMenu)
options.menu = {
    loadIcons: false
}

document.addEventListener('DOMContentLoaded', function () {
    console.log('Hello from inject.js');
    const images = document.querySelectorAll('img');
    // console.log(images);

    const altTexts = Array.from(images).map(img => img.getAttribute('alt') || '');

    const widths = altTexts.map(text => text.split('|').pop());
    console.log(widths);

    Array.from(images)
        .forEach((img, i) => img.setAttribute('width', !isNaN(Number(widths[i])) ? widths[i] : img.getAttribute('width')));

    Array.from(document.querySelectorAll('a'))
        .forEach(a => a.setAttribute('target', '_blank'));
});