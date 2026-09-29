function handleSearch(event) {
    if (event.key === "Enter") searchJob();
}

function normalizeSearchText(value) {
    return String(value || "")
        .toLowerCase()
        .normalize("NFKD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9\s&-]/g, " ")
        .replace(/\s+/g, " ")
        .trim();
}

function escapeHtml(value) {
    return String(value || "").replace(/[&<>\"]/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;"
    }[char]));
}

function highlightText(text, keyword) {
    const safe = escapeHtml(text);
    const words = normalizeSearchText(keyword).split(" ").filter(Boolean).slice(0, 8);
    if (!words.length) return safe;
    const pattern = words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|");
    return safe.replace(new RegExp(`(${pattern})`, "gi"), "<mark>$1</mark>");
}

function scoreSearchResult(item, terms) {
    const title = normalizeSearchText(item.title);
    const desc = normalizeSearchText(item.description);
    const text = normalizeSearchText(item.text);
    let score = 0;
    terms.forEach(term => {
        if (title === term) score += 100;
        if (title.includes(term)) score += 50;
        if (desc.includes(term)) score += 20;
        if (text.includes(term)) score += 5;
    });
    return score;
}

function searchJob() {
    const input = document.getElementById("searchBox");
    const resultBox = document.getElementById("results");
    if (!input || !resultBox) return;

    const keyword = input.value.trim();
    const normalized = normalizeSearchText(keyword);
    if (!normalized) {
        resultBox.innerHTML = "<h3>Please enter a keyword</h3><p>Try a job, scholarship, internship, state, district, passport, visa, or career topic.</p>";
        return;
    }

    const index = Array.isArray(window.CAREERLIX_SEARCH_INDEX) ? window.CAREERLIX_SEARCH_INDEX : [];
    const terms = normalized.split(" ").filter(Boolean);
    const found = index
        .map(item => ({ item, score: scoreSearchResult(item, terms) }))
        .filter(result => result.score > 0)
        .sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title))
        .slice(0, 30)
        .map(result => result.item);

    if (!found.length) {
        resultBox.innerHTML = `<h3>No matching result found</h3><p>Try keywords such as <b>government jobs</b>, <b>internship</b>, <b>scholarship</b>, <b>Delhi</b>, <b>passport</b>, <b>visa</b>, or <b>career tips</b>.</p>`;
        return;
    }

    resultBox.innerHTML = `<p class="search-count"><b>${found.length}</b> result${found.length === 1 ? "" : "s"} found</p>` +
        found.map(item => {
            const label = item.category.replace(/[-_]/g, " ").replace(/\b\w/g, c => c.toUpperCase());
            const description = item.description || item.text.slice(0, 180);
            return `<div class="job-card">
                <p class="search-category">${escapeHtml(label)}</p>
                <h3>${highlightText(item.title, keyword)}</h3>
                <p>${highlightText(description, keyword)}</p>
                <a class="details-btn" href="${encodeURI(item.url)}">View Page</a>
            </div>`;
        }).join("");
}

function searchState() {
    const stateSearch = document.getElementById("stateSearch");
    if (!stateSearch) return;
    const input = stateSearch.value.toLowerCase();
    document.querySelectorAll(".job-item").forEach(item => { item.style.display = item.textContent.toLowerCase().includes(input) ? "block" : "none"; });
}

function initSiteSearch() {
    const input = document.getElementById("searchBox");
    if (!input) return;
    input.addEventListener("input", () => {
        const resultBox = document.getElementById("results");
        if (!resultBox) return;
        if (!input.value.trim()) resultBox.innerHTML = "";
    });
}

document.addEventListener("DOMContentLoaded", initSiteSearch);
