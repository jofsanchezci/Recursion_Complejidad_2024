document.getElementById("start-button").addEventListener("click", () => {
    const searchType = document.getElementById("search-type").value;
    const target = parseInt(document.getElementById("target").value, 10);
    const numbers = Array.from({ length: 20 }, (_, i) => i + 1);

    visualizeSearch(numbers, target, searchType);
});

async function visualizeSearch(numbers, target, type) {
    const container = document.getElementById("visualization");
    container.innerHTML = ""; // Clear previous visualization

    // Create bars for visualization
    numbers.forEach(num => {
        const bar = document.createElement("div");
        bar.className = "bar";
        bar.style.height = `${num * 10}px`;
        bar.textContent = num;
        container.appendChild(bar);
    });

    const bars = document.querySelectorAll(".bar");

    if (type === "linear") {
        await linearSearchVisualization(numbers, target, bars);
    } else if (type === "binary") {
        await binarySearchVisualization(numbers, target, bars);
    }
}

async function linearSearchVisualization(numbers, target, bars) {
    for (let i = 0; i < numbers.length; i++) {
        bars[i].classList.add("active");
        await wait(500); // Pause for animation
        if (numbers[i] === target) {
            bars[i].classList.add("found");
            return;
        }
        bars[i].classList.remove("active");
    }
}

async function binarySearchVisualization(numbers, target, bars) {
    let left = 0;
    let right = numbers.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        // Highlight middle element
        bars[mid].classList.add("active");
        await wait(500);

        if (numbers[mid] === target) {
            bars[mid].classList.add("found");
            return;
        }

        bars[mid].classList.remove("active");

        if (numbers[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
}

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
