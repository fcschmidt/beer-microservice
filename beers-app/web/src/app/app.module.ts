import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from "@angular/forms";

import { BeerService } from "./beer.service";
import { IngredientService } from "./ingredient.service";
import { AppComponent } from './app.component';
import { BeersListComponent } from './beers-list/beers-list.component';
import { BeerDetailComponent } from './beer-detail/beer-detail.component';
import { BeerEditComponent } from './beer-edit/beer-edit.component';
import { SearchBeerComponent } from './search-beer/search-beer.component';
import { BeerCreateComponent } from './beer-create/beer-create.component';
import { IngredientCreateComponent } from './ingredient-create/ingredient-create.component';

@NgModule({
  declarations: [
    AppComponent,
    BeersListComponent,
    BeerDetailComponent,
    BeerEditComponent,
    SearchBeerComponent,
    BeerCreateComponent,
    IngredientCreateComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [BeerService, IngredientService],
  bootstrap: [AppComponent]
})
export class AppModule { }
