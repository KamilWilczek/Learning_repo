// import './style.scss';

//  stałe do łapania z html
const ADDITION_ID = 'js-addition';
const BACK_ID = 'js-back';
const CANCEL_ID = 'js-cancel';
const CLEAR_ID = 'js-clear';
const COMMA_ID = 'js-comma';
const DISPLAY_ID = 'js-display';
const DIVIDE_ID = 'js-divide';
const EQUAL_ID = 'js-equal';
const FRACTION_ID = 'js-fraction';
const INVERT_ID = 'js-invert';
const MEMORY_ADD_ID = 'js-M+';
const MEMORY_CLEAR_ID = 'js-MC';
const MEMORY_MINUS_ID = 'js-M-';
const MEMORY_READ_ID = 'js-MR';
const MEMORY_SET_ID = 'js-MS';
const MULTIPLY_ID = 'js-multiply';
const NUMBER_CLASS_SELECTOR = '.calculator__button--is-number';
const NUMBER_OF_NUMBERS_IN_KEYBOARD = 10;
const PERCENT_ID = 'js-percent';
const POWER_ID = 'js-power';
const SUBTRACTION_ID = 'js-subtraction';
const SQUARE_ID = 'js-square';



class Calculator {
  constructor() {
    //  przechowywanie wartości w pamięci, przyciski memory
    this.memoryValue = 0;
    //  potrzebujemy aktualną wartość
    this.displayValue = '0';
    //  potrzebujemy przechowywać poprzednią wartość
    this.previousValue = null;
    //  czy mamy jakąś wybraną operację i jaką, np ciągle dodajemu wybierając dodawanie i potem ciągle równa się
    this.selectedFunction = null;
    this.isFunctionDone = false;
    //  powtarzenie wartości np. 2+3=, = , =, = , cały czas dodaje 3.
    this.repeatedValue = 0;
    //  czy równa się było klikniete (dopsiujemy cyfrę czy wpisujey od nowa)
    this.wasEqualClicked = false;
    // czy została wciśnięta jakaś specjalna funkcja np. memory read
    this.wasSpecialFunctionClicked = false;

    //  podpinamy się pod wyświetlacz,
    this.bindToDisplay();
    // podpiamy się pod cyfry
    this.bindToNumbers();
    // podpinamy się pod klawisze funkcyjne
    this.bindToButtons();
  }




  bindToDisplay() {
    const display = document.getElementById(DISPLAY_ID);

    // obsługa błedu, jeżeli nie znajdzie wyświetlacza
    if (!display) {
      throw ("Nie znaleziono elementu dla wyświetlacza");
    }

    //  wyświetlanie w wyświetlaczu
    display.textContent = this.displayValue;
    this.display = display;
  }





  bindToNumbers() {
    //  do numbers pobieramy klawisze cyfry
    const numbers = document.querySelectorAll(NUMBER_CLASS_SELECTOR);

    //  obsługa błędu, gdyby ktoś w np htmu usunał cyfrę
    if (numbers.length !== NUMBER_OF_NUMBERS_IN_KEYBOARD) {
      console.warn("W klawiaturze brakuje cyfr")
    }
    //  do każdego przycisku z cyfrą z całej puli dodaj na click funkcję
    numbers.forEach(number => number.addEventListener("click", event => this.concatenateNumber(event)));
    return;
  }



  bindToButtons() {
    //  to się powtarza i bedzie powtarzać więc trzeba to zoptymalizować i wynieść do innej funkcji bindFunctionToButton
    // const memoryClearElement = document.getElementById(MEMORY_CLEAR_ID);
    // if (!memoryClearElement) {
    //   console.warn(`Nie znaleziono elementu o id ${MEMORY_CLEAR_ID}`);
    // } else {
    //   memoryClearElement.addEventListener("click", () => this.memoryClear());
    // }

    // const memoryReadElement = document.getElementById(MEMORY_READ_ID);
    // if (!memoryReadElement) {
    //   console.warn(`Nie znaleziono elementu o id ${MEMORY_READ_ID}`);
    // } else {
    //   memoryReadElement.addEventListener("click", () => this.memoryRead());
    // }

    //  jako parametr przekazujemy id i funkcję stzałkową wywołująca funkcję obsługującą przycisk. Strzałkową, żeby this nie staciło wiązania
    this.bindFunctionToButton(MEMORY_CLEAR_ID, () => this.memoryClear());
    this.bindFunctionToButton(MEMORY_READ_ID, () => this.memoryRead());
    this.bindFunctionToButton(MEMORY_ADD_ID, () => this.memoryAdd());
    this.bindFunctionToButton(MEMORY_MINUS_ID, () => this.memoryMinus());
    this.bindFunctionToButton(MEMORY_SET_ID, () => this.memorySet());
    this.bindFunctionToButton(CLEAR_ID, () => this.clear());
    this.bindFunctionToButton(CANCEL_ID, () => this.cancel());
    this.bindFunctionToButton(ADDITION_ID, () => this.addition());
    this.bindFunctionToButton(SUBTRACTION_ID, () => this.subtraction());
    this.bindFunctionToButton(MULTIPLY_ID, () => this.multiplication());
    this.bindFunctionToButton(DIVIDE_ID, () => this.divide());
    this.bindFunctionToButton(EQUAL_ID, () => this.equal());
    this.bindFunctionToButton(BACK_ID, () => this.back());
    this.bindFunctionToButton(INVERT_ID, () => this.inversion());
    this.bindFunctionToButton(COMMA_ID, () => this.addComma());
    this.bindFunctionToButton(PERCENT_ID, () => this.percent());
    this.bindFunctionToButton(SQUARE_ID, () => this.square());
    this.bindFunctionToButton(POWER_ID, () => this.power());
    this.bindFunctionToButton(FRACTION_ID, () => this.fraction());
    return;
  }




  //  przekazujemy tu id do łapanie elementów z htmla - id oraz callback - czyli funkcje która ma się wywoływać na tym id
  bindFunctionToButton(id, callback) {
    const element = document.getElementById(id);

    if (!element) {
      console.warn(`Nie znaleziono elementu o id ${id}`);
      return;
    }

    element.addEventListener("click", () => callback());
  }




  //  ta funkcja będzie robić string z cyfr. Np klikamy "2" i "3" to wyświetla się 23. Dokleja nam cyfry do już istniejących
  concatenateNumber(event) {
    // sprawdza czy obecna wartość wyświetlana jest nullem (null to w pamięci brak wartości ale wyswietlamy 0), czy jest 0, bo jak jest zero i naciśniemy 2 to chcemy mieć 2 a nie 02 oraz czy została wciśnięta jakaś specjalna funkcja
    this.displayValue = this.displayValue === null || this.displayValue === '0' || this.wasSpecialFunctionClicked ? event.target.textContent : this.displayValue + event.target.textContent;
    // Jeżeli warunek jest spełniony to podmień cyfrę na tą która została kliknięta,
    // this.displayValue = event.target.textContent

    //  a jak nie to doklej do tego co już jest
    // this.displayValue = this.displayValue + event.target.textContent


    // jeżeli przycisk równa się był kliknięty to ustawiamy poprzednią wartość na 0, powtarzalną wartośc na 0 i zmieniamy flagę, że przycisk nie był klikniety
    //  bo jak na kalkualtorze naciśniemy równa się i potem cyfrę to robimy nwowe działanie
    if (this.wasEqualClicked) {
      this.previousValue = null;
      this.repeatedValue = 0;
      this.wasEqualClicked = false;
    }
    //  zmiana flag specjalej funkcji i funkcji przycisków innych niż cyfry
    this.wasSpecialFunctionClicked = false;
    //  wyłącza wybramą operację
    this.isFunctionDone = false;
    //  wyśwetlanie - do elementu wyświetlacz wpisz wartość
    this.display.textContent = this.displayValue;
  }



  //  -----------------------wyczyść pamięć--------------------------
  //  funckja obsługująca przycisk MC
  memoryClear() {
    //  utaw że specjalny przycisk był kliknięty
    this.wasSpecialFunctionClicked = true;
    //  wyzeruj wartość w pamięci
    this.memoryValue = 0;
  }

  //  -----------------------odczytaj z pamięci--------------------------
  //  funkcja obsługująca przycisk MR
  memoryRead() {
    //  ustaw, że spacjalny przycisk został kliknięty
    this.wasSpecialFunctionClicked = true;
    //  wartość z pamięci ma być wpisana do wartości wyświetlacza
    // this.displayValue = this.memoryValue;
    // // console.log(this.displayValue)
    // //  do wyświetlacza wpiasna jest wartość z memory zamieniona na String
    // this.display.textContent = this.memoryValue.toString()
    this.changeDisplayValue(this.memoryValue);
  }

  //  -----------------------dodaj do pamięci--------------------------
  //  funkcja obsługująca przycisk M+
  memoryAdd() {
    //  ustaw, że spacjalny przycisk został kliknięty
    this.wasSpecialFunctionClicked = true;
    //  w pamięci zapisujemy wartość z pamięci i dodaną wartość z wyświetlacza
    //  do cyfry dodajemy string, trzeba wartośc przerobić na number
    this.memoryValue = this.memoryValue + Number(this.displayValue);
  }

  //  -----------------------odejmij z pamięci--------------------------
  //  funkcja obsługująca przycisk M-
  memoryMinus() {
    //  ustaw, że spacjalny przycisk został kliknięty
    this.wasSpecialFunctionClicked = true;
    //  w pamięci zapisujemy wartość z pamięci i odjętą wartość z wyświetlacza
    //  od cyfry odejmujemy string, trzeba wartośc przerobić na number
    this.memoryValue = this.memoryValue - Number(this.displayValue);
  }

  //  -----------------------zapamietaj--------------------------
  //  funkcja obsługująca przycisk MS
  memorySet() {
    //  ustaw, że spacjalny przycisk został kliknięty
    this.wasSpecialFunctionClicked = true;
    //  przekaż wartość ze zmiennej przechowującą wartość wyświetlacza do pamięci
    this.memoryValue = Number(this.displayValue);
  }

  //  -----------------------wyczyść--------------------------
  //  funkcja kasuje wartości i funkcje, nie kasuje pamięci
  clear() {
    this.previousValue = null;
    this.selectedFunction = null;
    this.changeDisplayValue(null);
  }

  //  -----------------------anuluj--------------------------
  //  funkcja kasuje wyświetlaną wartość
  cancel() {
    this.changeDisplayValue(null);
  }

  //  -----------------------dodawanie--------------------------
  addition(hasRepeatedValue) {
    // jeżeli wybrana operacja jest inna niż dodawanie i wybrana operacja ma jąkąkolwiek wartość (nie jest nullem)
    // if (this.selectedFunction !== this.addition && this.selectedFunction) {
    //   //  to wykonaj tę inną operację
    //   this.selectedFunction(hasRepeatedValue);
    // }
    //  wybrana operacja
    //  this.selectedFunction = this.addition;
    this.callPreviousFunctionAndAssignNew(this.addition, hasRepeatedValue);


    // sprawdzamy czy  jest kliknięte dwa razy na przycisk +
    // if (this.isFunctionDone) {
    //   //  jeżeli wciśnięto przycisk "+" dwa razy z rzedu to wartość jaka jest w wyświetlaczu wpisuje jako wartość do powtarzania sparsowana w number
    //   this.repeatedValue = Number(this.previousValue);
    //   this.displayValue = '0';
    //   this.wasEqualClicked = false;

    //   return;
    // }
    if (this.isFunctionDone) {
      this.setValuesForIsFunctionDone();
      return;
    }


    //  jeżeli to nie było ponowne wciśnięcie
    //  do nowej zmiennej która będzie przechowywać wartość z wyświetlacza przypisz obecnie wyświetlaną wartość
    // const displayValue = Number(this.display.textContent);
    //  jeżeli nie było wcześniej zmiennej do powtarzania to do tej nowej zmiennej przechwoującej poprzednią wartość wstaw poprzednią wartość jaka była wpisana. Jeżeli była podana wartość do powtarzanie to do zmiennej wstaw tę wartość do powtarzania
    // const previousValue = hasRepeatedValue ? this.repeatedValue : Number(this.previousValue);
    const [displayValue, previousValue] = this.getDisplayAndPreviousValue(hasRepeatedValue);

    // ----------Wyliczenie nowej wartości---------------
    //  do nowej zmiennej przechwoującej nową wartość wstaw sumę obecnej wartości i poprzedniej wartości
    const newValue = displayValue + previousValue;



    // //  zmień zmienną na zakończoną aktualną operację
    // this.isFunctionDone = true;
    // //  do zmienej przechowującej wartość do powtarzania
    // // jeżeli jest jakaś wartość do powtarzania to przypisz tę wartość
    // //  jeżeli nie ma to sprawdź czy wciśnięto "równa się"
    // //      jeżeli wciśnięto to przypisz zmienną przechowującą nową wartość (spowoduje to ze klikanie równa się będzie powtarzało jakąs operację na tej wartości)
    // //      jeżeli nie to przypisz wartość jaka jest obecnie wyświetlana(po sparsowaniu)
    // this.repeatedValue = hasRepeatedValue
    //   ? this.repeatedValue
    //   : this.wasEqualClicked
    //     ? newValue
    //     : Number(this.display.textContent);
    this.getRepeatedVaule(hasRepeatedValue, newValue)

    // this.isFunctionDone = true;
    // //  zmień flagę czy znak równości został kliknięty
    // this.wasEqualClicked = false;
    // //  do poprzedniej wartości wpisz nową wartość
    // this.previousValue = newValue;
    // //  do zmiennej przechowująca wartość z wyświetlacza wpisz null
    // this.displayValue = null;
    // //  do wyświetlacza wpisz nową wartość
    // this.display.textContent = newValue;
    this.setValuesAfterSettingNewValue(newValue);
  }

  //  ----------------------odejmowanie-------------------------------
  subtraction(hasRepeatedValue) {
    this.callPreviousFunctionAndAssignNew(this.subtraction, hasRepeatedValue);


    if (this.isFunctionDone) {
      this.setValuesForIsFunctionDone();
      return;
    }

    const [displayValue, previousValue] = this.getDisplayAndPreviousValue(hasRepeatedValue);
    let newValue;

    // ----------Wyliczenie nowej wartości---------------
    //  po włączeniu kalkulatora wyświetla się 0 ale jest null i nie mamy od czego odjąć, 0 musimy sobie kliknąć
    if (this.previousValue !== null) {
      //  do nowej zmiennej przechowującej wynik operacji jeżeli jest jakaś wartość do powtarzania
      newValue = hasRepeatedValue
        //  przypisz odejmowanie od zmiennej przechowującą cyfrę poprzednią odejmij cyfrę w zmiennej do powtarzania
        ? displayValue - this.repeatedValue
        //  jeżeli nie ma wartości do powtarzania to od poprzedno wpisanej cyfry odjemij ostatnio wpisaną
        : previousValue - displayValue;


      this.getRepeatedVaule(hasRepeatedValue, newValue)
    }
    this.setValuesAfterSettingNewValue(newValue);

  }

  //  -----------------------mnożenie--------------------------
  multiplication(hasRepeatedValue) {
    this.callPreviousFunctionAndAssignNew(this.multiplication, hasRepeatedValue);

    if (this.isFunctionDone) {
      this.setValuesForIsFunctionDone();
      return;
    }

    const [displayValue, previousValue] = this.getDisplayAndPreviousValue(hasRepeatedValue);

    // ----------Wyliczenie nowej wartości---------------
    const newValue = displayValue * previousValue;

    this.getRepeatedVaule(hasRepeatedValue, newValue)

    this.setValuesAfterSettingNewValue(newValue);
  }

  //  -----------------------dzielenie--------------------------
  divide(hasRepeatedValue) {
    this.callPreviousFunctionAndAssignNew(this.divide, hasRepeatedValue);

    if (this.isFunctionDone) {
      this.setValuesForIsFunctionDone();
      return;
    }

    const [displayValue, previousValue] = this.getDisplayAndPreviousValue(hasRepeatedValue);
    const newValue = hasRepeatedValue
      ? displayValue / this.repeatedValue
      : previousValue === 0
        ? displayValue
        : previousValue / displayValue;

    this.getRepeatedVaule(hasRepeatedValue, newValue)
    this.setValuesAfterSettingNewValue(newValue);

  }

  //  -----------------------znak równości--------------------------
  equal() {
    //  zmień flagę czy funkcja została wykonana
    this.isFunctionDone = false;

    //  jeżeli flaga "czy znak równa się był kliknięty" jest not true to (nie był kliknięty)...
    if (!this.wasEqualClicked) {
      //  przekaż do zmiennej że żadna operacja nie jest aktywna, has repeatted jest false, nie ma tej wartosci ktora ma byc dodawana
      this.selectedFunction(false);
    } else {
      //  jeżeli był kliknięty, ustaw, że operacja jest aktywna, mamy juz uzywac repeated value
      this.selectedFunction(true);
    }
    //  zmień flagę "czy równa się był kliknięty" na true
    this.wasEqualClicked = true;
  }

  //  -----------------------procent--------------------------
  percent() {
    //  watość w procentach, poprzednia wartość razy aktualna wartość przez 100
    // const newValue = this.previousValue * this.displayValue / 100;

    // this.wasSpecialFunctionClicked = true;
    // this.wasEqualClicked = false;
    // this.changeDisplayValue(newValue);
    this.callSpecialFunction(this.previousValue * this.displayValue / 100);
  }

  //  -----------------------pierwiastek--------------------------
  square() {
    //  Math.sqrt oblicza pierwiastek z aktualnej wartości i wysyła jako parametr do innej funkcji
    this.callSpecialFunction(Math.sqrt(this.displayValue));
  }

  //  -----------------------potęgowanie--------------------------
  power() {
    //  podnosi akualną wartość do potęgi i przekazuje jako parametr
    this.callSpecialFunction(this.displayValue ** 2);
  }

  //  -----------------------ułamek--------------------------
  fraction() {
    //  zamienia aktualną wartość w ułamek i przekazuje jako parametr do innej funkcji
    this.callSpecialFunction(1 / this.displayValue);
  }


  callSpecialFunction(value) {
    this.wasSpecialFunctionClicked = true;
    this.wasEqualClicked = false;
    this.changeDisplayValue(value);
  }
  //  -----------------------cofnij--------------------------
  back() {
    //  wywołuje funkcję odpowiedzialną za wyświetlanie i jeżeli  jest jakaś wartość w zmiennej która przechowuje wartość do wyświetlenia to przekaż nowy string który ma wszystkie znaki starego stringa bez ostatniego
    // slice(0,-1) - ze starego stringa wytnij od 0 znaku do 1 od końca i zwróć to co wycięte(czyli bez ostatniego)
    //  jeżeli nie ma wartości w displayValue to przekaż do wyświetlenia null
    this.changeDisplayValue(this.displayValue ? this.displayValue.slice(0, -1) : null);
  }

  //  -----------------------zmień znak--------------------------
  inversion() {
    //  wywołaj funkcję wyświetlającą w wyświetlaczu i jeżeli
    //  wartość do wyświetlenia jest większa lub równa 0 to wyświetl jej wartość absolutną z minusem
    //  a jeżeli jest odwrotnie to wyświetl wartość absolutną
    this.changeDisplayValue(this.displayValue >= 0 ? -Math.abs(this.displayValue) : Math.abs(this.displayValue));
  }

  //  -----------------------dodaj przecinek--------------------------
  addComma() {
    //  sprawdzamy czy nasza wartość wpisana w kalkulator nie zawiera już kropki, jeśli zawiera to nic się nie stanie
    //  includes sprawdza czy jest taki znak i zwraca true jak znajdzie i false jak nie znajdzie
    if (!this.display.textContent.includes('.')) {
      //  do funkcji wyświetlającej przekazujemy string z warunekiem i kropka będzie albo po zerze albo po całym wyrażeniu
      //  jeżeli w displayValue jest jakaś wartość to przekaż do wyświetlania tę wartość z kropką na koncu np "34."
      //  jeżeli w displayValue jest null albo psuty string przekaż '0.'
      this.changeDisplayValue(`${this.displayValue ? this.displayValue : '0'}.`)
    }

  }



  callPreviousFunctionAndAssignNew(previousFunction, hasRepeatedValue) {
    // jeżeli wybrana operacja jest inna niż dodawanie i wybrana operacja ma jąkąkolwiek wartość (nie jest nullem)
    if (this.selectedFunction !== previousFunction && this.selectedFunction) {
      //   //  to wykonaj tę inną operację
      this.selectedFunction(hasRepeatedValue);
    }
    //  wybrana operacja
    this.selectedFunction = previousFunction;
  };

  setValuesForIsFunctionDone() {
    //  jeżeli wciśnięto przycisk "+" dwa razy z rzedu to wartość jaka jest w wyświetlaczu wpisuje jako wartość do powtarzania sparsowana w number
    this.repeatedValue = this.getRepeatedVaule(null, this.previousValue);
    this.displayValue = '0';
    this.wasEqualClicked = false;

  };


  getDisplayAndPreviousValue(hasRepeatedValue) {
    //  jeżeli to nie było ponowne wciśnięcie
    //  do nowej zmiennej która będzie przechowywać wartość z wyświetlacza przypisz obecnie wyświetlaną wartość
    const displayValue = Number(this.display.textContent);
    //  jeżeli nie było wcześniej zmiennej do powtarzania to do tej nowej zmiennej przechwoującej poprzednią wartość wstaw poprzednią wartość jaka była wpisana. Jeżeli była podana wartość do powtarzanie to do zmiennej wstaw tę wartość do powtarzania
    const previousValue = hasRepeatedValue ? this.repeatedValue : Number(this.previousValue);
    return [displayValue, previousValue]
  };



  getRepeatedVaule(hasRepeatedValue, newValue) {
    // //  zmień zmienną na zakończoną aktualną operację
    this.isFunctionDone = true;
    // //  do zmienej przechowującej wartość do powtarzania
    // // jeżeli jest jakaś wartość do powtarzania to przypisz tę wartość
    // //  jeżeli nie ma to sprawdź czy wciśnięto "równa się"
    // //      jeżeli wciśnięto to przypisz zmienną przechowującą nową wartość (spowoduje to ze klikanie równa się będzie powtarzało jakąs operację na tej wartości)
    // //      jeżeli nie to przypisz wartość jaka jest obecnie wyświetlana(po sparsowaniu)
    this.repeatedValue = hasRepeatedValue
      ? this.repeatedValue
      : this.wasEqualClicked
        ? newValue
        : Number(this.display.textContent);
  }



  setValuesAfterSettingNewValue(newValue) {
    this.isFunctionDone = true;
    //  zmień flagę czy znak równości został kliknięty
    this.wasEqualClicked = false;
    //  do zmiennej przechowująca wartość z wyświetlacza wpisz null
    this.displayValue = null;
    //  do wyświetlacza jeżeli poprzednui wpisana cyfra nie jest nullem wpisz wynik operacji a jeżeli jest to wpisz aktualną cyfrę
    this.display.textContent = this.previousValue !== null ? newValue : this.display.textContent;
    //  jako poprzednia wartość ustaw jeżeli poprzednia wartość nie była nullem wynik operacji a jesli była to wpisz aktualna wartość
    this.previousValue = this.previousValue !== null ? newValue : this.display.textContent;
  };



  //  funkcja wpisująca do wyświetlania, parsuje do stringa
  changeDisplayValue(value) {
    // zmienna która równa się null lub pusty string
    //  działa to na zasadzie że jeżeli w value jest null (jedna strona wyrażenia) lub pusty string (druga strona wyrażenia) to zwraca true, jeżeli wyrażenie logiczne jest nieprawdziwe zwraca false
    const isNoValue = value === null || value === '';
    this.displayValue = value;
    //  jeżeli isNoValue jest true czyli  wyświetl string z 0 a jak nie to zamień wartość w string i wyświetl
    this.display.textContent = isNoValue ? '0' : value.toString();
  }

};

new Calculator();