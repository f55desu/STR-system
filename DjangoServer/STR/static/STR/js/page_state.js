function getTabs() {
    return Array.from(document.querySelectorAll('.tabcontent'));
}

function saveState(){
    const tabs = getTabs();
    tabs.forEach(tab => {
        localStorage.setItem(tab.id, tab.style.display);
    });
};

function loadState(){
    const tabs = getTabs();
    tabs.forEach(tab => {
        const style = localStorage.getItem(tab.id);
        tab.style.display = style;
    });
};

$(document).ready(loadState);