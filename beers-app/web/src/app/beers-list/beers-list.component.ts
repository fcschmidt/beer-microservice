import { Component, OnInit } from '@angular/core';

import { Beer } from "../beer";
import { BeerService } from "../beer.service";



@Component({
  selector: 'app-beers-list',
  templateUrl: './beers-list.component.html',
  styleUrls: ['./beers-list.component.css'],
})
export class BeersListComponent implements OnInit {

  beers: Beer[];

  constructor(private beersService: BeerService) { }

  ngOnInit() {
    this.getBeers();
  }

  getBeers(): void {
    this.beersService.getBeers()
      .subscribe(beers => this.beers = beers);
  }
}
