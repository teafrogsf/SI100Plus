document.addEventListener('DOMContentLoaded', function () {
    console.log('Hello from inject.js');
    const images = document.querySelectorAll('img');
    // console.log(images);

    const altTexts = Array.from(images).map(img => img.getAttribute('alt') || '');

    const widths = altTexts.map(text => text.split('|').pop());
    console.log(widths);

    Array.from(images)
        .forEach((img, i) => {
            if(Number(widths[i])) img.setAttribute('width', widths[i]);
        });

    Array.from(document.querySelectorAll('a'))
        .forEach(a => a.setAttribute('target', '_blank'));
});

Reveal.addEventListener("ready", function addFragmentToLists() {
    for (const listItem of document.querySelectorAll(".fragmented-lists li")) {
      listItem.classList.add("fragment");
    }
  });