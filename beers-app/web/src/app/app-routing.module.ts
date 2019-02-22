import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BeersListComponent} from "./beers-list/beers-list.component";
import { BeerDetailComponent} from "./beer-detail/beer-detail.component";
import { BeerEditComponent } from "./beer-edit/beer-edit.component";

const routes: Routes = [
  { path: '', redirectTo: '/cervejas', pathMatch: 'full' },
  { path: 'cervejas', component: BeersListComponent },
  { path: 'cervejas/:id/:beer_name', component: BeerDetailComponent },
  { path: 'cervejas/:id/:beer_name/edit', component: BeerEditComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
