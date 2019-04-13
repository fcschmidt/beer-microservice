import { Component, OnInit } from '@angular/core';
import { Location } from "@angular/common";
import { FormGroup } from "@angular/forms";

// import { Beer } from "../beer";
import { BeerService } from "../beer.service";

@Component({
  selector: 'app-beer-create',
  templateUrl: './beer-create.component.html',
  styleUrls: ['./beer-create.component.css']
})
export class BeerCreateComponent implements OnInit {

  beer: any;

  constructor(
    private location: Location,
    private beerService: BeerService,
  ) { }

  ngOnInit() {
    this.beer = {};
    // this.create();
  }

  create(frm: FormGroup){
    this.beerService.createBeer(this.beer).subscribe();
  }
  goBack(): void {
    this.location.back();
  }
}
