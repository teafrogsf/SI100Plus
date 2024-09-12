document.addEventListener('DOMContentLoaded', function () {

    console.log('Hello from inject.js');
    // 获取所有的 <img> 元素
    const images = document.querySelectorAll('img');
    console.log(images);

    // 遍历所有的 <img> 元素并收集它们的 alt 属性值
    const altTexts = Array.from(images).map(img => img.getAttribute('alt') || '');

    const widths = altTexts.map(text => text.split('|').pop());
    console.log(widths);

    // 将 widths 分别添加到每个元素的 width 中
    Array.from(images).forEach((img, i) => img.setAttribute('width', widths[i] || ""));
});