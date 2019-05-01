import {Component, Input, OnInit} from '@angular/core';
import { FormGroup, FormControl} from "@angular/forms";


@Component({
  selector: 'app-ingredient-create',
  templateUrl: './ingredient-create.component.html',
  styleUrls: ['./ingredient-create.component.css']
})
export class IngredientCreateComponent implements OnInit {

  ingredientForm = new FormGroup({
    ingredientName: new FormControl('')
  });



  constructor() { }

  ngOnInit() {
  }

  onSubmit(){
    console.warn(this.ingredientForm.value)
  }
}
