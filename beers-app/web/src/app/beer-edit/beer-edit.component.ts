import {Component, Input, OnInit} from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { Location } from "@angular/common";
// import { FormControl, FormGroupDirective, FormBuilder, FormGroup, NgForm, Validators } from "@angular/forms";

import { Beer } from "../beer";
import { BeerService } from "../beer.service";
import {NgForm} from "@angular/forms";

@Component({
  selector: 'app-beer-edit',
  templateUrl: './beer-edit.component.html',
  styleUrls: ['./beer-edit.component.css']
})
export class BeerEditComponent implements OnInit {

  @Input() beer: Beer;

  constructor(
    // private formBuilder: FormBuilder,
    private location: Location,
    private route: ActivatedRoute,
    private beerService: BeerService,
  ) { }

  /*beerForm: FormGroup;
  beer_name:string='';
  description:string='';*/


  ngOnInit() {
    this.getBeer();
  }

  getBeer(): void {
    const id = +this.route.snapshot.paramMap.get('id');

    /*this.beerForm = this.formBuilder.group({
      'beer_name': [null, Validators.required],
      'description': [null, Validators.required],
    });*/

    this.beerService.getBeer(id)
      .subscribe(beer => this.beer = beer);
      console.log(this.beer);
  }

  save(form: NgForm){

  }

  goBack(): void {
    this.location.back();
  }
}
