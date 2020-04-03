// aby móc używać tego interface gdzie indziej trzeba go najpierw eksportować
// tworzenie własnego typu danych
 export interface Movie {
    id: Number; // ID będzie typem Number
    title: String; // Movie musi mieć title a title będzie typem String
    year?: Number; // Year będzie typem Number, ? - oznacza, że typ jest opcjonalny
    note?: String; // Note będzie typem String, ? - oznacza, że typ jest opcjonalny
  } 