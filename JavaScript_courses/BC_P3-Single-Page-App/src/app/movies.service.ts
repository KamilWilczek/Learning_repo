// ten service ma zwracać listę filmów
import { Injectable } from '@angular/core';
import { Movie } from './modele/movie'; // aby używać tu własnoręcznie utworzonego typu Movie trzeba go importować modele->movie.ts


@Injectable({
  providedIn: 'root'
})
export class MoviesService {

  // movies: Movie[] = [{id: 0, title: '123'}];  jaki typ danych mają mieć filmy, będzie to własny typ: Movie i będzie zawierał tablice [], trzeba podać wymagane parametry
  // private - zmienna prywata, dostęp do niej jest tylko przez metode
  private movies: Movie[] = [
    {id: 0, title: 'Titanic', note: 'Rok 1912, brytyjski statek Titanic wyrusza w swój dziewiczy rejs do USA. Na pokładzie emigrant Jack przypadkowo spotyka arystokratkę Rose.', year: 1997},
    {id: 1, title: 'Terminator', note: 'Elektroniczny morderca zostaje wysłany z przyszłości do roku 1984, by zabić matkę przyszłego lidera rewolucji. W ślad za nim rusza Kyle Reese, który ma chronić kobietę.', year: 1984},
    {id: 2, title: 'Avatar', note: 'Jake, sparaliżowany były komandos, zostaje wysłany na planetę Pandora, gdzie zaprzyjaźnia się z lokalną społecznością i postanawia jej pomóc.', year: 2009}
  ]

  constructor() { }

  // metoda do zwracania filmów które są w private movies do lista.component
  allMovies(): Movie[] { // Movie[] - zwracane będzie tablica z obiektami typu Movie
    return this.movies;
  }
  // metoda do zwracania jednego filmu dla details.component
  getMovie(id: number): Movie[] {
    return this.movies[id];
  }
}
