const toDoList = [];

const form = document.querySelector('form');
const input = document.querySelector('.insert');
const taskList = document.querySelector('ul');
const taskNumber = document.querySelector('h1 span');
// pobieram wszystkie elementy o klasie task
const taskItems = document.getElementsByClassName("task");

const searcher = document.querySelector(".searcher")

const mainList = document.getElementsByClassName("task");

const addTask = (event) => {
    // blokowanie odświeżania
    event.preventDefault();

    // wpisywanie do inputBoxa
    const inputTask = input.value;

    // blokowanie pustej wartości
    if (inputTask === '') return;

    console.log(inputTask);
    // czyszczenie inputa
    input.value = "";

    // tworzenie li z przyciskiem
    const task = document.createElement('li');
    // dodawanie klasy task do li, tylko do nich
    task.className = "task";
    task.innerHTML = inputTask + "<button>Usuń</button>"

    // wrzucanie tasków na listę
    toDoList.push(task);
    renderList();

    // wyświetlanie dodanych zadań
    taskList.appendChild(task);
    mainList.app
    // aktualizowanie liczby zadań
    taskNumber.textContent = taskItems.length;
    task.querySelector('button').addEventListener("click", removeTask);
};

// usuwanie z listy
const removeTask = (e) => {
    searcher.value = "";

    // zdarzenie.target.parentNode.remove();
    const index = e.target.parentNode.dataset.key;
    toDoList.splice(index, 1);
    taskNumber.textContent = toDoList.length;
    // aktualizowanie liczby zadań

    renderList();

};

// odświeżanie listy
const renderList = () => {
    // czyszczenie tekstu ul
    taskList.textContent = '';
    // z toDoList pobierany jest każdy element i jego index
    toDoList.forEach((toDoElement, key) => {
        // dla każdego elementu przypisz dataset o wartości indexu tego elementu
        toDoElement.dataset.key = key;
        // i dodaj te elementy do ul'a
        taskList.appendChild(toDoElement)
    });
};

// wyszukiwarka
const searchItem = () => {
    const searchText = searcher.value.toLowerCase();
    // jeżeli searchBox jest pusty to ma wyświetlać całą listę
    if (searchText === '') {
        renderList();
        // w inym przypadku ma wyszukiwać
    } else {

        let items = [...taskItems];

        items = items.filter(item => item.textContent.toLowerCase().includes(searchText));
        taskList.textContent = "";
        items.forEach(item => taskList.appendChild(item));
    };
};

form.addEventListener('submit', addTask);
searcher.addEventListener("input", searchItem)







    // // wrzucam li z przyciskiem (task) do tablicy
    // toDoList.push(task);
    // taskList.appendChild(task);
    // removeTask();