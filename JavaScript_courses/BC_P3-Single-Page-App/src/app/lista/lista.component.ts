import { Component, OnInit } from '@angular/core';
import { MoviesService } from '../movies.service';
import { Movie } from '../modele/movie';


@Component({
  selector: 'app-lista',
  templateUrl: './lista.component.html',
  styleUrls: ['./lista.component.css']
})
export class ListaComponent implements OnInit {

  // movies: String - blad
  movies: Movie[]; // movies ma byc typu Movie

  constructor( private ms: MoviesService) { } // można tu dodać bo zostało dodane w providers w app.modules.ts

  ngOnInit(): void {
    this.movies = this.ms.allMovies(); // tutaj wrzucamy do moives filmy z metody allMovies stworzonej w movies.service.ts
    console.table(this.movies);
  }

}
