import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BeersListComponent} from "./beers-list/beers-list.component";
import { BeerDetailComponent} from "./beer-detail/beer-detail.component";
import { BeerEditComponent } from "./beer-edit/beer-edit.component";
import { BeerCreateComponent } from "./beer-create/beer-create.component";

const routes: Routes = [
  { path: '', redirectTo: '/cervejas', pathMatch: 'full' },
  { path: 'cervejas', component: BeersListComponent },
  { path: 'cervejas/:id/:beer_name', component: BeerDetailComponent },
  { path: 'cervejas/edit/:id/:beer_name', component: BeerEditComponent},
  { path: 'cervejas/create', component: BeerCreateComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
