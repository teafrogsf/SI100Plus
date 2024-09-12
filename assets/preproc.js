

module.exports = (markdown, options) => {
  return new Promise((resolve, reject) => {
    return resolve(
      (options.makeTitle ? `
<div style="display: flex; justify-content: center; align-items: center; height: 700px;">
  <div style="text-align: center; padding: 40px; background-color: white; border: 2px solid rgb(0, 63, 163); border-radius: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 20px; color: #333;">${options.makeTitle.lecture || "请设置 makeTitle.lecture"}</h1>
    <p style="font-size: 24px; color: #666;">${options.makeTitle.title || "请设置 makeTitle.title"}</p>
    <p style="font-size: 16px; color: #999; margin-top: 20px;">${options.makeTitle.detail || "请设置 makeTitle.detail"}</p>
  </div>
</div>\n\n<!--s-->\n\n` : "") +
      markdown
        .split('\n')
        .map((line, index) => {
          if (!options.autoFragment) return line;
          if (!/^\s*[-*] /.test(line) || index === 0) return line;
          return line.replace(/^(\s*)[-*] (.*)/, "$1- <span> $2 </span>") + ' <!-- .element: class="fragment" -->';
        })
        .map((line, index) => {
          if (!options.autoTitlePage) return line;
          if (!line.startsWith('# ')) return line;
          return '<div class="middle center"><div style="width: 100%">\n\n' + line + '\n\n</div></div>';
        })
        .join('\n')
    );
  });
};