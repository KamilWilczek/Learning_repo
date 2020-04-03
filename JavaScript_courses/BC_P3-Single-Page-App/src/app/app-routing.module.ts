import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { ListaComponent } from './lista/lista.component';
import { DetailsComponent } from './details/details.component';


const routes: Routes = [
  {path: '', component: ListaComponent}, // jak nie bedzie nic na końcu localhost:4200 to wyświelti ListComponent czyli listę filmów
  {path: 'movie/:id', component: DetailsComponent} // jeżeli url będzie zawierał movie/:id wyświetl DetailsComponent
];

@NgModule({
  declarations: [],
  imports: [CommonModule, RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
