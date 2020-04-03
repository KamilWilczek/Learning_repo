import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Movie } from '../modele/movie';
import { MoviesService } from '../movies.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {

  movie: Movie;

  constructor( // zmienne
    private route: ActivatedRoute,
    private fs: MoviesService,
    private location: Location
  ) {}
  

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id'); // dostęp do ID z app-routing.module.ts
    console.log('id', id);
    this.movie = this.fs.getMovie(Number(id));
  }

  return() {
    this.location.back();
  }

}
