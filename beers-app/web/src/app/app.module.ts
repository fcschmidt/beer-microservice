import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';

import {BeerService} from "./beer.service";
import { AppComponent } from './app.component';
import { BeersListComponent } from './beers-list/beers-list.component';
import { BeerDetailComponent } from './beer-detail/beer-detail.component';
import { BeerEditComponent } from './beer-edit/beer-edit.component';
import { SearchBeerComponent } from './search-beer/search-beer.component';

@NgModule({
  declarations: [
    AppComponent,
    BeersListComponent,
    BeerDetailComponent,
    BeerEditComponent,
    SearchBeerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [BeerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
