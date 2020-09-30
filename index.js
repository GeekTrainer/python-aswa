main();

async function main() {
    const response = await fetch('/api/tasks');
    const json = await response.json();

    for (let task of json.tasks) {
        const item = document.createElement('li');
        item.className = 'list-group-item';
        item.innerText = task;

        document.getElementById('task-list').appendChild(item);
    }
}