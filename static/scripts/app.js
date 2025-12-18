
hljs.highlightAll();

function openAddModal() {
    document.getElementById("addModal").style.display = "flex";
}

function closeAddModal() {
    document.getElementById("addModal").style.display = "none";
}

function saveSnippet() {
    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            code: document.getElementById("newCode").value,
            language: document.getElementById("language").value
        })
    }).then(() => location.reload());
}

function closeSnippetModal() {
    document.getElementById("snippetModal").style.display = "none";
}

function deleteSnippet(event, id) {
    event.stopPropagation();
    fetch(`/delete/${id}`, { method: "POST" }).then(() => location.reload());
}
