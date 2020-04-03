import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { ListaComponent } from './lista/lista.component';
import { DetailsComponent } from './details/details.component';

import { MoviesService } from './movies.service';
import { AppRoutingModule } from './app-routing.module'; // importujemy stworzony service

@NgModule({
  declarations: [
    AppComponent,
    ListaComponent,
    DetailsComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule
  ],
  providers: [MoviesService], // umieszczany service w providers
  bootstrap: [AppComponent]
})
export class AppModule { }
