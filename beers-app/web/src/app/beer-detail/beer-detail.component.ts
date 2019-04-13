import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

import { Beer } from "../beer";
import { BeerService } from "../beer.service";

@Component({
  selector: 'app-beer-detail',
  templateUrl: './beer-detail.component.html',
  styleUrls: ['./beer-detail.component.css']
})
export class BeerDetailComponent implements OnInit {

  @Input() beer: Beer;

  constructor(
    private route: ActivatedRoute,
    private beerService: BeerService,
  ) { }

  ngOnInit() {
    this.getBeer();
  }

  getBeer(): void {
    const id = +this.route.snapshot.paramMap.get('id');

    this.beerService.getBeer(id)
      .subscribe(beer => this.beer = beer);
      console.log(this.beer);
  }

  deleteBeer(beer): void{
    this.beerService.deleteBeer(beer).subscribe();
    location.reload()
  }
}
