//  skrypt pozwalający pobrać dane z serwera

class PokemonTCGCatalog {
  //  zapisujemy dane w konstruktorze
  constructor() {
    //  ilośc pokemonów na stronie - z dokumentacji API
    this.pageSize = 4;
    //  aktualna strona - z dokumentacji API
    this.currentPage = 1;

    //  tablica na karty
    this.cards = [];
    this.newCards = [];
    //  tu będzie pobierany element z html zawierający [data-content]
    this.catalog = null;
    this.button = null;
    this.loader = null;
    this.search = null;
    this.card = null;
    this.info = null;



    //  tak jak jest w dokumentacji, rodzielamy adres
    this.API = "https://api.pokemontcg.io"
    this.API_VERSION = 'v1'
    this.API_RESOURCE = 'cards'

    //  takie adresy do których się odwołujemy po coś, które zawierają jakieś dane nazywamy endpointami
    this.API_ENDPOINT = `${this.API}/${this.API_VERSION}/${this.API_RESOURCE}`

    this.UiSelectors = {
      content: '[data-content]',
      button: '[data-button]',
      loader: '[data-loader]',
      search: 'search',
      card: '[data-card]',
      info: '[data-info]',
    }
  }

  //  funkcja inicjalizująca - odpalająca inne funkcje
  async initializeCatalog() {
    //  pobieranie z html elemntu z tym co jest w content czyli [data-content]
    this.catalog = document.querySelector(this.UiSelectors.content);
    this.button = document.querySelector(this.UiSelectors.button);
    this.loader = document.querySelector(this.UiSelectors.loader);
    this.search = document.getElementById(this.UiSelectors.search);
    this.info = document.querySelector(this.UiSelectors.info);
    this.pullCards();
    this.addEventListeners();
  }


  addEventListeners() {
    this.button.addEventListener('click', () => this.pullCards());
    this.search.addEventListener('keyup', () => this.filterCards());
  }


  //  funkcja zaciągająca karty
  async pullCards() {
    //  obsługa zamiany buttona na loader przez dodawanie i odejmowanie klasy hide
    // this.loader.classList.remove('hide')
    // this.button.classList.add('hide')
    this.toggleShowElement(this.loader, this.button)

    // const fetchedCards = await this.fetchData(this.API_ENDPOINT);
    //  destrukturyacja - mamy do razu karty, nie musimy się odwoływać po całej ścieżce
    const { cards } = await this.fetchData(`${this.API_ENDPOINT}?page=${this.currentPage}&pageSize=${this.pageSize}`);
    // this.loader.classList.add('hide')
    // this.button.classList.remove('hide')
    this.toggleShowElement(this.loader, this.button)

    //  do tablicy cards (pustej)  wrzucamy cards z destrukturyzacji za pomoca operatora spread
    this.cards = [...this.cards, ...cards]

    this.newCards = [...cards];

    //  wywołanie funkcji createCatalog z przekazaniem parametru
    this.createCatalog(this.newCards);
    this.currentPage++;
  }

  toggleShowElement(...elements) {
    elements.forEach(element => element.classList.toggle('hide'));
  }


  //  funkcja do pobierania danych
  async fetchData(url) {
    //  zapisujemy do zmiennej odpowiedź z API
    const response = await fetch(url);
    //  parsujemy, odpowiedź otrzymujemy w formacie json i musimy sparsować do obiketu natywnego JS
    const parsedResponse = await response.json();
    // zwracamy sparsowaną odpowiedź
    return parsedResponse;
  }

  //  funkcja wrzucająca karty do htmla, przyjmuje parametr
  createCatalog(cards) {
    //  join pozwala na połączenie elementów tablic nie za pomocą domyślnego przecinka tylko pustego stringa

    //  tu pojawia się problem bo za każdym razem pobiera od nowa wszystkie karty po naciśniściu load more zamiast pobierac tylko nowe
    // this.catalog.innerHTML += [cards.map((card) => this.createCard(card)).join('')];
    this.catalog.insertAdjacentHTML('beforeend', [cards.map((card) => this.createCard(card)).join(''),]);
  }

  //  funkcja tworząca kartę (strukturę)
  //  destrukturyzacja
  createCard({ name, number, imageUrl, supertype, subtype, rarity, id }) {
    return `
    <article class="card" id=${id} data-card>
     <header class="card__header">
      <h2 class="card__heading">${name}</h2>
      <p class="card__number">Nr: ${number}</p>
     </header>
     <img class="card__image "src="${imageUrl}" alt="${name}"/>
    <p class="card__description"><span class="bold">Supertype:</span> ${supertype}</p>
    <p class="card__description ${subtype ? '' : 'hide'}"><span class="bold">Subtype:</span> ${subtype}</p>
    <p class="card__description ${rarity ? '' : 'hide'}"><span class="bold">Rarity:</span> ${rarity}</p>
    </article>
    `
    //  jeżeli nie ma karta nic w rarity to nie wyświetlaj rarity
    // <p class="card__description ${rarity ? '' : 'hide'}"><span class="bold">Rarity:</span> ${rarity}</p>
  }

  //  filtrowanie kart
  filterCards() {
    //  przypisujemy tu wartość naszego inputa
    const searchQuerry = this.search.value.toLowerCase();

    //  jeżeli wpisujemy coś w wyszukiwarkę to przycisk load more ma byc ukryty
    // czyli jeżeli jest coś wpisane w input (cos inne niz nic daje true) to ukryj przycisk, w innym wypadku okdkryj
    searchQuerry.length ? this.button.classList.add('hide') : this.button.classList.remove('hide');

    //  usuwa klasę hide z każdego elementu kiedy input jest pusty
    document.querySelectorAll(this.UiSelectors.card).forEach((element) => element.classList.remove("hide"));

    //  filtorwanie kart, jeżeli nazwa się nie zgadza warunek jest prawdziwy i zwraca ten element przy czym przez metodę includes nie chodzi o całą nazwę a część albo ciąg znaków
    const filteredCards = this.cards.filter(({ name }) => !name.toLowerCase().includes(searchQuerry));

    //  jeśli długość tablicy wyfiltrowanych kart równa się długości tablicy wszystkich kart czyli żadna karta nie pasuje to zdejmij klasę hide z <P>There are no results</P>, a jak jest różna to dodaj klasę hide
    filteredCards.length === this.cards.length ? this.info.classList.remove('hide') : this.info.classList.add('hide');

    //  wszystkie karty których nazwa się nie zgadzała z wyszukiwaną dostają klasę hide, karty łapiemy po id.
    filteredCards.forEach(({ id }) => document.getElementById(id).classList.add('hide'))
  }
}