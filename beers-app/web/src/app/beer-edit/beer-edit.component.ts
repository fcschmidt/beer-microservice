import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { Location } from "@angular/common";
import { FormBuilder, FormGroup, NgForm, Validators } from "@angular/forms";

import { Beer } from "../beer";
import { Ingredient } from "../ingredient";
import { BeerService } from "../beer.service";
import { IngredientService } from "../ingredient.service";

@Component({
  selector: 'app-beer-edit',
  templateUrl: './beer-edit.component.html',
  styleUrls: ['./beer-edit.component.css']
})
export class BeerEditComponent implements OnInit {

  @Input() beer: Beer;
  // @Input() beerUpdate: BeerUpdate;
  @Input() ingredient: Ingredient;

  ingredientForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private location: Location,
    private route: ActivatedRoute,
    private router: Router,
    private beerService: BeerService,
    private ingredientService: IngredientService,
  ) { }


  ngOnInit() {
    this.getBeer();
    this.ingredientForm = this.formBuilder.group({
      'ingredient_name': [null, Validators.required],
      'beer_id': [null, Validators.required]
    });
  }

  /*
  *  Beer Methods
  * */

  // GET: Get beer
  getBeer(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.beerService.getBeer(id)
      .subscribe(beer => this.beer = beer);
      console.log(this.beer);
  }

  // UPDATE: Update Beer
  /*updateBeer(form: NgForm) {

  }*/

  /*
  *  Ingredient Methods
  * */

  // ADD: Add a new ingredient
   addIngredient(form: NgForm) {
     this.ingredientService.addIngredient(form)
       .subscribe((ingredient: Ingredient) => {
         console.log(ingredient);
       });
     location.reload();
   }

  // DELETE: Delete the ingredient
  deleteIngredient(ingredient): void{
    this.ingredientService.deleteIngredient(ingredient).subscribe();
    location.reload();
    this.getBeer()
  }
}
