const grabButton = document.getElementById("grabButton");
grabButton.addEventListener("click", () => {
    chrome.tabs.query({active: true}, (tabs) => {
        var tab = tabs[0];
        if (tab) {
            execScript(tab);
        } else {
            alert("There are no active tabs")
        }
    })
})

function execScript(tab) {
    chrome.scripting.executeScript(
        {
            target:{tabId: tab.id, allFrames: true},
            func:grabImages
        },
        onResult
    )
}

function grabImages() {
    const images = document.querySelectorAll("img");
    return Array.from(images).map(image=>image.src)
}

function onResult(frames) {
    if (!frames || !frames.length) {
        alert("Could not get images");
        return;
    }

    const imageUrls = frames.map(frame=>frame.result)
                            .reduce((r1,r2) => r1.concat(r2));
    window.navigator.clipboard
        .writeText(imageUrls.join("\n"))
        .then(() => {
            window.close();
        })
}