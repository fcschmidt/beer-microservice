import { Component, Input, OnInit } from '@angular/core';
import { Location } from "@angular/common";
// import { Router } from "@angular/router";
import {FormGroup, FormBuilder, NgForm, Validators} from "@angular/forms";

import { BeerService} from "../beer.service";
import { Beer } from "../beer";


@Component({
  selector: 'app-beer-create',
  templateUrl: './beer-create.component.html',
  styleUrls: ['./beer-create.component.css']
})
export class BeerCreateComponent implements OnInit {

  @Input() bee: Beer;

  beerForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private location: Location,
    private beerService: BeerService,
    // private router: Router
  ) { }

  ngOnInit() {
    this.beerForm  = this.formBuilder.group({
      'beer_name': [null, Validators.required],
      'description': [null, [Validators.required, Validators.minLength(10)]],
      'color': [null, Validators.required],
      'alcohol': [null, Validators.required],
      'temperature': [null, Validators.required],
      'harmonization': [null, Validators.required],
      'ingredients': [null, Validators.required],
    });
    console.log(this.beerForm);
  }

  /*addBeer(form: NgForm) {
    console.log(form.value);
  }*/


  addBeer(form: NgForm) {
    this.beerService.addBeer(form)
      .subscribe((beer: Beer) => {
        console.log(beer);
      });
  }


  goBack(): void {
    this.location.back();
  }
}
