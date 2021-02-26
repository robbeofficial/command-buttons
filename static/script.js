async function stream(url, target) {
    const response = await fetch(url);
    const reader = response.body
        .pipeThrough(new TextDecoderStream())
        .getReader();
    const out = document.getElementById('out');

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        target.appendChild(document.createTextNode(value));
    }

    target.appendChild(document.createTextNode('$'));
}

async function run(name, command) {
    var target = document.getElementById('out');

    while (target.firstChild) {
        target.removeChild(target.firstChild);
    }

    target.appendChild(document.createTextNode('$ ' + command + '\n'));

    stream('/run/' + name, target);
}